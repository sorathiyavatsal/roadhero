from rest_framework import views, response, permissions
from rest_framework.status import *
from api.utils import *
from api.models import Trip, serviceRequest, chatModel
from api.serializers import TripSerializer, getTripSerializer, ServiceRequestSerializer, getChatSerializer, ChatSerializer
from django.contrib.auth import get_user_model
User = get_user_model()

class getTrips(views.APIView):
    """
    This is service class to manage trips methods.
    """
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, role=None, id=None):
        if role == 0:
            instance = Trip.objects.filter(id=id)
        else:
            instance = Trip.objects.filter(user=id)
        serializer = getTripSerializer(instance, many=True)
        data = {'data': {'array': serializer.data}, "status": 200, "code": 200,
                'message': 'All trips.'}
        return views.Response(data, status=HTTP_200_OK)

class createTrip(views.APIView):
    """
    This is service class to manage trips methods.
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        try:
            trip_data = request.data.get("trip")
            nameValuePairs = trip_data.get("nameValuePairs", None)
            if nameValuePairs:
                request_data = trip_data
            else:
                request_data = nameValuePairs
            serialize_data = {
                'user': request_data['user_id'], 'vendor': request_data['vendor_id'], 'service': request_data['service_id'],
                'source_lat_lng': request_data['source_lat_lng'], 'source_address': request_data['source_address'],
                'destination_lat_lng': request_data['destination_lat_lng'], 'destination_address': request_data['destination_address'],
                'start_time': request_data['start_time'], 'end_time': request_data['end_time'], 'trip_path': request_data['trip_path'],
                'map_image': request_data['map_image']
            }
            serializer = TripSerializer(data=serialize_data)
            if serializer.is_valid():
                serializer.save()
                service_status_update(vendor_id=request_data['vendor_id'], service_status=True)
                data = {"status": 200, "code": 200, "message": "Trip created.", "data": serializer.data}
            else:
                data = {"status": 500, "code": 500, "message": "Error in adding Trip.", "data": serializer.errors}
        except:
            data = {"status": 500, "code": 500, "message": "Error in adding Trip."}
        return views.Response(data, status=HTTP_200_OK)

class updateTrip(views.APIView):
    """
    This is service class to manage trips methods.
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        trip_data = request.data.get("url", None)
        instance = Trip.objects.get(id=trip_data["id"])
        instance_data = {'map_image': trip_data["long_url"]}
        serializer = TripSerializer(
            instance, data=instance_data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            data = {"status": 200, "code": 200, "message": "Trip image updated.", "data": serializer.data}
        else:
            data = {"status": 500, "code": 500, "message": "Unable to update trip image.", "data": serializer.errors}
        return views.Response(data, status=HTTP_200_OK)

class finishTrip(views.APIView):
    """
    This is service class to manage trips methods.
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, trip_id=None, end_time=None):
        instance = Trip.objects.get(id=trip_id)
        serialize_data = {"end_time": end_time}
        serializer = TripSerializer(instance, data=serialize_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            finish_trip_update(request.user.id)
            data = {"status": 200, "code": 200, "message": "Trip finished", "data": serializer.data}
        else:
            data = {"status": 500, "code": 500, "message": "Error in updating.", "data": serializer.error}
        return views.Response(data, status=HTTP_200_OK)

def finish_trip_update(vendor_id):
    try:
        instance = User.objects.get(id=vendor_id)
        instance.service_status = False
        instance.save()
    except:
        pass
    return

def service_status_update(vendor_id, service_status):
    try:
        instance = User.objects.get(id=vendor_id, role=2)
        instance.service_status = True
        instance.save()
    except:
        pass
    return

class getChats(views.APIView):
    """
    This is service class to manage trips methods.
    """
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, tripId=None):
        instance = chatModel.objects.filter(trip_id=tripId)
        serializer = getChatSerializer(instance['queryset'], many=True)
        data = {'data': {"array": serializer.data}, "status": 200, "code": 200,
                'message': OK}
        return views.Response(data, status=HTTP_200_OK)

class updateRequestStatus(views.APIView):
    """
    This is service class to manage trips methods.
    """
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, req_id=None, vendor_id=None, request_status=True):
        search_values = request.data['search']['value']
        user_search = search_values.get('user', None)
        vendor_search = search_values.get('vendor', None)
        service_search = search_values.get('service', None)
        id_search = search_values.get('id', None)

        # making filter set on basis of requested search
        search_keys = {
            'id': id_search, 'user': user_search, 'vendor': vendor_search,
            'service': service_search
        }

        # filtering queryset on basis of search keys
        queryset = filter_and_pagination(request, Trip, search_keys)

        # searialize queryset data
        serializer = getTripSerializer(queryset['queryset'], many=True)
        data = {'data': serializer.data, 'total_records': queryset['total_records'], "status": 200, "code": 200,
                'message': OK}
        return views.Response(data, status=HTTP_200_OK)

class cancelRequest(views.APIView):
    """
    This is service class to manage trips methods.
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, req_id=None, user_type=None):
        if user_type == 1:
            instance = serviceRequest.objects.get(id=req_id)
            instance.delete()
            data = {"status": 200, "code": 200, "message": "Request Canceled."}
        elif user_type == 2:
            instance = serviceRequest.objects.get(id=req_id)
            instance.delete()
            data = {"status": 200, "code": 200, "message": "Request Canceled."}
        else:
            data = {"status": 500, "code": 500, "message": "Error in adding Trip."}
        return views.Response(data, status=HTTP_200_OK)

class updateEndTime(views.APIView):
    """
    This is service class to manage trips methods.
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, id=None, end_time=None):
        instance = Trip.objects.get(id=id)
        serialize_data = {"end_time": end_time}
        serializer = TripSerializer(instance, data=serialize_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            data = {"status": 200, "code": 200, "message": "Updated end time.", "data": serializer.data}
        else:
            data = {"status": 500, "code": 500, "message": "Error in updating end time.", "data": serializer.error}
        return views.Response(data, status=HTTP_200_OK)


class setTripRoute(views.APIView):
    """
    This is service class to manage trips methods.
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        trip_id = request.data.get("trip_id")
        trip_path = request.data.get("path")
        serializer = {
                "object": trip_path,
                "tripId": trip_id,
                "vendor_id": request.user.id
            }
        data = {"status": 200, "code": 200, "message": "Trip route set.", "data": serializer}
        return views.Response(data, status=HTTP_200_OK)