import operator
import os, requests
from datetime import datetime
from datetime import timedelta, date, time
from functools import reduce
import jwt
from django.db.models import Q
from roadhero import settings
import requests, json
from decouple import config
import base64
from django.core.files.base import ContentFile

jwt_key = settings.SECRET_KEY
FCM_SERVER_KEY = config("FCM_SERVER_KEY")

def send_push_notification(device_tokens, title, body, screen_type, screen_data):
    data = {
        "registration_ids": device_tokens,
        "notification": {
            "body": body,
            "title": title,
            "content_available": True,
            "priority": "high",
            "sound": "sound.mp3",
            "android_channel_id": "new_email_arrived_channel"
        },
        "data": {
            "sound": "sound.mp3",
            "type": screen_type,
            "title": title,
            "body": body,
            "content_available": True,
            "priority": "high",
            "android_channel_id": "roadhero_channel"
        }
    }
    if screen_data:
        data["data"].update(screen_data)
    headers = {
        'Authorization': f'key={FCM_SERVER_KEY}',
        'Content-Type': 'application/json'
    }
    url = "https://fcm.googleapis.com/fcm/send"
    data = json.dumps(data)
    res = requests.post(url=url, data=data, headers=headers)
    status = res.status_code
    return status

def decode_jwt(encoded):
    """
    This is common method to decode the encoded jwt token
    """
    try:
        decoded = jwt.decode(encoded, jwt_key, algorithms='HS256')
    except jwt.ExpiredSignatureError:
        decoded = None
    except jwt.InvalidTokenError:
        decoded = None
    return decoded

def encode_user_jwt(encoded_data):
    """
    This method is used to encoded the user id and pcr id a jwt token
    :argument encoded_data= {'user_id': user, 'password': password, "exp": dt}
    """
    encoded = jwt.encode(encoded_data, jwt_key, algorithm='HS256')
    return encoded

def decode_base64(image_data, file_type, user_id):
    if image_data:
        format, imgstr = image_data.split(';base64,')
        ext = format.split('/')[-1]
        data = ContentFile(base64.b64decode(imgstr), name=f'{file_type}_{user_id}.' + ext)
    else:
        data = None
    return data


def path_and_rename(instance, filename):
    """
    This function is used to rename filename and add folder path.
    """
    current_time = datetime.now()
    year = current_time.year
    month = current_time.month
    upload_to = f'documents/{year}/{month}/'
    file_name, extn = filename.rsplit('.', 1)
    today = date.today()
    now = datetime.now()
    this_time = time(now.hour, now.minute, now.second)
    file_name = str(file_name) + str(datetime.combine(today, this_time))
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}-{}.{}'.format(instance.pk, str(now), ext)
    else:
        # set filename as random string
        filename = '{}-{}.{}'.format(file_name, str(now), ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)

def filter_and_pagination(request, model_refrence, search_keys):
    length = request.data['length']
    start = request.data['start']
    from_date = request.data['search']['from_date']
    to_date = request.data['search']['to_date']

    kwargs = []
    start = int(start) + 1

    if len(search_keys) > 0:
        for keyname in search_keys:
            values = search_keys[keyname]
            if values == None or values == '':
                pass
            elif values == "null":
                kwargs.append(Q(**{keyname: None}))
            else:
                kwargs.append(Q(**{keyname: values}))
    if from_date:
        from_date = str(from_date).split('-')
        start_date = datetime(int(from_date[0]), int(from_date[1]), int(from_date[2]))
        if to_date:
            to_date = str(to_date).split('-')
            try:
                end_date = datetime(int(to_date[0]), int(to_date[1]), int(to_date[2]) + 1)
            except:
                end_date = datetime(int(to_date[0]), int(to_date[1]), int(to_date[2]))
        else:
            end_date = datetime.now()
        if len(kwargs) > 0:
            queryset_filter = model_refrence.objects.filter(
                reduce(operator.and_, kwargs), created_at__range=[start_date, end_date]
            )
        else:
            queryset_filter = model_refrence.objects.filter(created_at__range=[start_date, end_date])
    else:
        if len(kwargs) > 0:
            queryset_filter = model_refrence.objects.filter(reduce(operator.and_, kwargs))
        else:
            queryset_filter = model_refrence.objects.all()
    order_by = '-id'

    start_limit = ((int(length) * int(start)) - int(length))
    end_limit = int(length) * int(start)
    total_object_count = queryset_filter.count()
    total_pages = int(total_object_count) // int(length)

    queryset = queryset_filter.order_by(order_by)[start_limit:end_limit]

    dataset = {
            'queryset': queryset,
            'total_records': total_object_count,
            'pagination': {
                'per_page': length,
                'current_page': start,
                'total_records': total_object_count,
                'total_pages': total_pages
            }
        }
    return dataset

def send_doc_invite(email):
    bearer_token= ""
    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "Content-Type": "application/json"
    }

    document_ids = [
        "5a163aa7f9fa41e8a300d64c505541ff66b10bdc",
        "9da80086b3684fd5928a41cd1a24165e0eb285a0",
        "5a163aa7f9fa41e8a300d64c505541ff66b10bdc"
    ]
    for document_id in document_ids:
        url = f'https://api.signnow.com/document/{document_id}/invite'
        data = {
            "document_id": document_id,
            "subject": "RoadHero service document verification.",
            "message": "Please sign and verify the RoadHero service document.",
            "from": "paolomazza26@yahoo.com",
            "to": email
        }
        res = requests.post(url=url, data=data, headers=headers)

    return