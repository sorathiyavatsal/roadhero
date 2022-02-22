from rest_framework import views, response, permissions
from django.shortcuts import HttpResponse
from rest_framework.status import *
from api.utils import *
from roadhero import settings
from math import sin, cos, sqrt, atan2, radians
from api.serializers import (
    getUserSerializer, crudUserSerializer, ReviewSerializer,
    getReviewSerializer, getBookingHistorySerializer, VendorDetailSerializer
)
from api.models import Review, VerificationCode, BookingHistory, VenderDetails
from django.contrib.auth import get_user_model
from django.contrib.auth import login, logout, authenticate
from rest_framework_jwt.settings import api_settings
from twilio.rest import Client
import random, sys
import stripe

User = get_user_model()
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

# twilio API Key
accountSid = config('accountSid')
authToken = config('authToken')
SenderMobile = config('SenderMobile')
stripe_key = config('STRIPE_LIVE_SECRET_KEY')

class register_view(views.APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request,  format=None):
        obJH = user_services()
        data = obJH.user_registration(request)
        return views.Response(data, status=HTTP_200_OK)

class verifyPhone(views.APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request, phone=None):
        obJH = user_services()
        data = obJH.phone_verification_code(request, phone)
        return views.Response(data, status=HTTP_200_OK)

class verifyCode(views.APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request, phone=None, code=None):
        obJH = user_services()
        data = obJH.verify_code(request, phone, code)
        return views.Response(data, status=HTTP_200_OK)

class verifyPhoneNumber(views.APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request, format=None):
        obJH = user_services()
        data = obJH.verify_mobile_number(request)
        return views.Response(data, status=HTTP_200_OK)

class verifyPhoneNumberGetMethod(views.APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request, mobile=None):
        client = Client(accountSid, authToken)
        code = random.randint(1000, 9000)
        instance = VerificationCode.objects.filter(mobile=mobile)
        if len(instance) > 0:
            is_active = instance[0].is_active
            instance[0].code = code
            instance[0].save()
            if is_active:
                data = {
                    "status": 200, "message": "Mobile number already verified.", "code": 200
                }
            else:
                try:
                    client.messages.create(
                        body=f'Your Phone Verification Code is {code}',
                        from_=SenderMobile,
                        to=mobile
                    )

                    data = {
                        "status": 201, "message": "A verification code has been sent to your phone number.", "code": 201
                    }
                except:
                    data = {
                        "status": 400, "message": "Unable to send verification code.", "code": 400
                    }

        else:
            try:
                VerificationCode.objects.create(mobile=mobile, code=code)
                client.messages.create(
                    body=f'Your Phone Verification Code is {code}',
                    from_=SenderMobile,
                    to=mobile
                )
                data = {
                    "status": 201, "message": "A verification code has been sent to your phone number.", "code": 201
                }
            except:
                data = {
                    "status": 400, "message": "Unable to send verification code.", "code": 400
                }
        return views.Response(data, status=HTTP_200_OK)

class verifyOtpCode(views.APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request,  mobile=None, code=None):
        obJH = user_services()
        data = obJH.verify_otp_code(request, mobile, code)
        return views.Response(data, status=HTTP_200_OK)

class chargePayment(views.APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request,  format=None):
        obJH = user_services()
        data = obJH.charge_payment(request)
        return views.Response(data, status=HTTP_200_OK)

class generateCardToken(views.APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request,  format=None):
        obJH = user_services()
        data = obJH.generate_card_token(request)
        return views.Response(data, status=HTTP_200_OK)

class createCustomer(views.APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request,  format=None):
        obJH = user_services()
        data = obJH.create_customer(request)
        return views.Response(data, status=HTTP_200_OK)

class makePayment(views.APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request,  format=None):
        obJH = user_services()
        data = obJH.make_payment(request)
        return views.Response(data, status=HTTP_200_OK)

class login_view(views.APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request,  format=None):
        print("login data : ", request.data)
        obJH = user_services()
        data = obJH.user_login(request)
        return views.Response(data, status=HTTP_200_OK)

class logout_view(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request,  format=None):
        obJH = user_services()
        data = obJH.user_logout(request)
        return views.Response(data, status=HTTP_200_OK)

class update_admin_user(views.APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request,  format=None):
        obJH = user_services()
        data = obJH.update_user_admin(request)
        return views.Response(data, status=HTTP_200_OK)

class update_login_user(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request,  format=None):
        obJH = user_services()
        data = obJH.login_user_update(request)
        return views.Response(data, status=HTTP_200_OK)

class edit_profile(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request,  format=None):
        obJH = user_services()
        data = obJH.login_user_update(request)
        return views.Response(data, status=HTTP_200_OK)

class update_phone(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request,  format=None):
        obJH = user_services()
        data = obJH.UpdatePhoneNumber(request)
        return views.Response(data, status=HTTP_200_OK)

class get_users(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, user_id=None):
        obJH = user_services()
        data = obJH.get_users(request, user_id)
        return views.Response(data, status=HTTP_200_OK)

class reset_password_mail(views.APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request,  format=None):
        obJH = user_services()
        data = obJH.send_reset_password_mail(request)
        return views.Response(data, status=HTTP_200_OK)

class reset_password(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, email=None, role=None, ):
        obJH = user_services()
        data = obJH.update_password_reset(request)
        return views.Response(data, status=HTTP_200_OK)

class email_update_password(views.APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request, email=None, role=None, password=None):
        obJH = user_services()
        data = obJH.updateEmailPassword(request, email, role, password)
        return views.Response(data, status=HTTP_200_OK)

class update_password(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, oldPassword=None, newPassword=None):
        obJH = user_services()
        data = obJH.updateUserPassword(request, oldPassword, newPassword)
        return views.Response(data, status=HTTP_200_OK)

class verify_device(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request,  format=None):
        obJH = user_services()
        data = obJH.verify_auth_device(request)
        return views.Response(data, status=HTTP_200_OK)

class verify_code(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request,  format=None):
        obJH = user_services()
        data = obJH.verify_auth_code(request)
        return views.Response(data, status=HTTP_200_OK)

class setRating(views.APIView):
    """
    This is service class to manage trips methods.
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):

        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {"status": 200, "message": "Rating Review added.", "data": serializer.data}
        else:
            data = {"status": 500, "message": "Unable to update trip image.", "data": serializer.errors}
        return views.Response(data, status=HTTP_200_OK)

class setDeviceToken(views.APIView):
    """
    This is service class to manage trips methods.
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, device_token=None):
        try:
            instance = User.objects.get(id=request.user.id)
            serializer = crudUserSerializer(instance, data={"device_token": device_token}, partial=True)
            if serializer.is_valid():
                serializer.save()
                data = {"status": 200, "message": "Device_token updated.", "data": serializer.data}
            else:
                data = {"status": 500, "message": "Error in updating device_token.", "data": serializer.errors}
        except:
            data = {"status": 500, "message": "Error in updating device_token."}
        return views.Response(data, status=HTTP_200_OK)

class getRatingReview(views.APIView):
    """
    This is service class to manage trips methods.
    """
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, format=None):
        instance = Review.objects.filter(review_for=request.user.id)
        serializer = getReviewSerializer(instance, many=True)
        data = {'data': {'array': serializer.data}, 'code': 200, 'status': 200,
                'message': OK}
        return views.Response(data, status=HTTP_200_OK)

def index(request):
    return HttpResponse("<h1>Welcome to Road Hero</h1>")

class user_services():
    def user_validation(self, email, device_token, latitude, longitude):
        try:
            user = User.objects.get(email=email, verified=True)
            user.device_token = device_token
            user.latitude = latitude
            user.longitude = longitude
            user.save()
        except User.DoesNotExist:
            user = None
        return user

    def user_login_validation(self, email, password, device_token, latitude, longitude):
        data = {}
        user = self.user_validation(email, device_token, latitude, longitude)
        if user:
            if user.check_password(password):
                data["data"] = user
            else:
                data['error'] = USER_DETAILS_INCORRECT
        else:
            data['error'] = USER_DETAILS_INCORRECT
        return data

    def user_login(self, request):
        email = request.data.get("email", None)
        password = request.data.get("password", None)
        device_token = request.data.get("device_token", None)
        latitude = request.data.get("latitude", None)
        longitude = request.data.get("longitude", None)
        data = self.user_login_validation(email, password, device_token, latitude, longitude)
        user_data = data.get("data", None)
        if user_data:
            user = authenticate(username=email, password=password)
            login(request, user)
            payload = jwt_payload_handler(user)
            token = jwt.encode(payload, settings.SECRET_KEY)
            serializer = getUserSerializer(user_data)
            serialized_data = serializer.data
            serialized_data["token"] = token
            response_data = {
                "status": 200, "message": "User found.",
                "data": serialized_data, "code": 200
            }
        else:
            response_data = {
                "status": 400, "code": 400, "message": USER_DETAILS_INCORRECT
            }
        return response_data

    def user_logout(self, request):
        logout(request)
        response_data = {
            "status": 200, "message": "User logout.", "code": 200
        }
        return response_data

    def user_registration(self, request):
        """
        This method is used to validate new user creation
        """
        email = request.data.get("email", None)
        phone = request.data.get("phone", None)
        first_name = request.data.get("first_name", None)
        last_name = request.data.get("last_name", None)
        password = request.data.get("password", None)

        code = random.randint(1000, 9000)
        # code = 1234
        serialize_data = {
            "first_name": first_name, "last_name": last_name, "email": email,
            "phone": phone, "password": password, 'code': code
        }
        if phone and email:
            instance = User.objects.filter(phone=phone, email=email)
            if len(instance) > 0:
                if instance[0].verified:
                    response_data = {'code': 400, 'status': 400, 'message': "User already exist."}
                else:
                    status = self.verify_auth_code(phone, code)
                    if status:
                        instance[0].code = code
                        instance[0].save()
                        response_data = {'code': 401, 'status': 401, 'message': "User is not verified."}
                    else:
                        response_data = {'code': 400, 'status': 400, 'message': "Unable to send otp code"}
            else:
                status = self.verify_auth_code(phone, code)
                if status:
                    serializer = crudUserSerializer(data=serialize_data)
                    if serializer.is_valid():
                        serializer.save()
                        response_data = {'data': serializer.data, 'code': 200, 'status': 200,
                                         'message': "User registered successfully."}
                    else:
                        response_data = {'data': serializer.errors, 'code': 400, 'status': 400,
                                         'message': "Unable to register user."}

                else:
                    response_data = {'code': 400, 'status': 400,
                                     'message': "Unable to register user."}

        return response_data

    def verify_code(self, request, phone, code):
        instance = User.objects.filter(phone=phone, code=code)
        if len(instance) > 0:
            instance[0].code = 0
            instance[0].verified = True
            instance[0].save()
            serializer = getUserSerializer(instance, many=True)
            data = {
                "status": 200, "message": "Code Verified.", "data": serializer.data, "code": 200
            }
        else:
            data = {
                "status": 400, "message": "Invalid Code or Number.", "code": 400
            }
        return data

    def verify_otp_code(self, request, phone, code):
        instance = VerificationCode.objects.filter(mobile=phone, code=code, is_active=False)
        if len(instance) > 0:
            instance[0].code = 0
            instance[0].is_active = True
            instance[0].save()
            data = {
                "status": 200, "message": "Code Verified.", "code": 200
            }
        else:
            data = {
                "status": 500, "message": "Invalid Code or Number.", "code": 500
            }
        return data

    def charge_payment(self, request, format=None):
        card_number = request.data.get("card_number", None)
        card_cvc = request.data.get("card_cvc", None)
        exp_month = request.data.get("exp_month", None)
        exp_year = request.data.get("exp_year", None)
        request_id = request.data.get("request_id", None)
        amount = request.data.get("amount", None)
        tip = request.data.get("tip", False)
        if request_id and card_number and card_cvc and amount:
            try:
                instance = BookingHistory.objects.get(id=request_id)
                stripe.api_key = stripe_key
                card_token = self.generate_card_token(card_number, exp_month, exp_year, card_cvc)
                if card_token:
                    default_source, customer_id = self.create_customer(instance.email, instance.mobile, instance.name, card_token)
                    print(default_source, customer_id)
                    if default_source and customer_id:
                        charge_data = self.make_payment(default_source, instance.price, customer_id)
                        if tip:
                            instance.tip = amount
                        else:
                            instance.payment_status = True
                        instance.save()
                        serializer = getBookingHistorySerializer(instance)
                        message = f"Your card is charged {amount} $"
                        self.send_payment_notification(serializer.data, message)
                        data = {"data": serializer.data, "charge_data": charge_data, "code": 201, "status": 201,
                                "message": message}
                    else:
                        data = {"code": 400, "status": 400, "message": "Payment is not charged. please try again!"}

                else:
                    data = {"code": 400, "status": 400, "message": "Invalid card"}
            except:
                data = {"code": 400, "status": 400, "message": "Invalid request id."}
        else:
            data = {"code": 400, "status": 400, "message": "Invalid data received."}
        return data

    def create_card_token(self, number, exp_month, exp_year, cvc, request_id):

        stripe.api_key = config("STRIPE_KEY")
        try:
            card_token = stripe.Token.create(
                card={
                    "number": number,
                    "exp_month": exp_month,
                    "exp_year": exp_year,
                    "cvc": cvc,
                },
            )
            card_token_id = card_token["id"]
            instance = BookingHistory.objects.get(id=request_id)
            instance.card_token = card_token_id
            instance.save()

        except:
            card_token_id = None
        return card_token_id

    def generate_card_token(self, card_number, exp_month, exp_year, card_cvc):

        stripe.api_key = stripe_key
        try:
            card_token = stripe.Token.create(
                card={
                    "number": card_number,
                    "exp_month": exp_month,
                    "exp_year": exp_year,
                    "cvc": card_cvc,
                },
            )
            card_token_id = card_token["id"]
        except:
            card_token_id = None
        return card_token_id

    def make_payment(self, default_source, amount, customer):
        stripe.api_key = stripe_key
        try:
            charge_data = stripe.Charge.create(
                amount=amount,
                currency="usd",
                customer=customer,
                source=default_source,
                description="Service request change",
            )

        except:
            charge_data = None
        return charge_data

    def create_customer(self, email, phone, name, source):
        stripe.api_key = stripe_key
        try:
            charge_data = stripe.Customer.create(
                name=name,
                email=email,
                phone=phone,
                source=source,
                description="My First Test Customer ",
                )
            defalt_source = charge_data["default_source"]
            customer_id = charge_data["id"]

        except:
            defalt_source = None
            customer_id = None
        return defalt_source, customer_id

    def phone_verification_code(self, request, phone):
        instance = User.objects.filter(phone=phone)
        client = Client(accountSid, authToken)
        code = random.randint(1000, 9000)
        if len(instance) > 0:
            try:
                instance[0].code = code
                instance[0].save()
                client.messages.create(
                    body=f'Your Phone Verification Code is {code}',
                    from_=SenderMobile,
                    to=phone
                )

                data = {
                    "status": 200, "message": "A verification code has been sent to your phone number.", "code": 200
                }
            except:
                data = {
                    "status": 400, "message": "Unable to send verification code.", "code": 400
                }

        else:
            data = {
                "status": 400, "message": "Phone number not exists.", "code": 400
            }
        return data

    def verify_mobile_number(self, request):
        mobile = request.data.get("mobile", None)
        device_token = request.data.get("device_token", None)
        client = Client(accountSid, authToken)
        code = random.randint(1000, 9000)
        instance = VerificationCode.objects.filter(mobile=mobile)
        if len(instance) > 0:
            is_active = instance[0].is_active
            if str(instance[0].device_token).strip().lower() == str(device_token).strip().lower():
                device_verify = True
            else:
                instance[0].device_token = device_token
                instance[0].code = code
                instance[0].is_active = False
                instance[0].save()
                device_verify = False
            user_data = {
                "first_name": instance[0].first_name,
                "last_name": instance[0].last_name,
                "mobile": instance[0].mobile,
                "email": instance[0].email
            }
            if is_active and device_verify:
                data = {
                    "status": 200, "message": "Mobile number already verified.", "code": 200,
                    "data": user_data
                }
            else:
                try:
                    client.messages.create(
                        body=f'Your Phone Verification Code is {code}',
                        from_=SenderMobile,
                        to=mobile
                    )

                    data = {
                        "status": 201, "message": "A verification code has been sent to your phone number.", "code": 201,
                        "data": user_data
                    }
                except:
                    data = {
                        "status": 400, "message": "Unable to send verification code.", "code": 400
                    }

        else:
            try:
                VerificationCode.objects.create(mobile=mobile, code=code, device_token=device_token)
                client.messages.create(
                    body=f'Your Phone Verification Code is {code}',
                    from_=SenderMobile,
                    to=mobile
                )
                data = {
                    "status": 201, "message": "A verification code has been sent to your phone number.", "code": 201,
                    "data": {
                    "first_name": None,
                    "last_name": None,
                    "mobile": mobile,
                    "email": None
                }
                }
            except:
                data = {
                    "status": 400, "message": "Unable to send verification code.", "code": 400
                }
        return data

    def login_user_update(self, request):
        """
        This method is used to update logged in user details.
        """
        # serialize logged in user details
        serializer = crudUserSerializer(
            request.user, data=request.data, partial=True
        )
        # update user details if serializer valid
        if serializer.is_valid():
            serializer.save()
            result = {'data': serializer.data, 'code': HTTP_200_OK, 'message': OK, "status": 200}
        else:
            result = {'data': serializer.errors, 'code': 500, 'message': FAIL, "status": 500}
        return result

    def UpdatePhoneNumber(self, request):
        """
        This method is used to update logged in user details.
        """
        phone = request.data.get("phone", None)
        instance = User.objects.filter(id=request.user.id)
        code = random.randint(1000, 9999)
        if len(instance) > 0:
            status = self.verify_auth_code(phone, code)
            if status:
                instance[0].phone = phone
                instance[0].code = 1234
                instance[0].verified = False
                instance[0].save()
                data = {"code": 200, "status": 200, "message": "Phone number updated."}
            else:
                data = {"code": 400, "status": 400, "message": "Unable to update phone number."}
        else:
            data = {"code": 400, "status": 400, "message": "Error occurred."}
        return data

    def editProfile(self, request):
        """
        This method is used to update logged in user details.
        """
        request_data = request.data.get("user", None)
        role = request_data.get("role", None)
        user_id = request_data.get("id", None)
        phone = request_data.get("phone", None)
        instance = User.objects.get(id=user_id, role=role)
        # serialize logged in user details
        serializer = crudUserSerializer(
            instance, data=request_data, partial=True
        )
        # update user details if serializer valid
        if serializer.is_valid():
            serializer.save()
            result = {'data': serializer.data, 'code': HTTP_200_OK, 'message': 'User profile edited.', "status": 200}
        else:
            result = {'data': serializer.errors, 'code': 500, 'message': 'Error in updating user.', "status": 500}
        return result

    def logoutUser(self, request):
        """
        This method is used to logout authenticated user.
        """
        logout(request)
        result = {'code': HTTP_200_OK, 'message': OK, "status": 200}
        return result

    def get_users(self, request, user_id):
        """
        This method is used to retreive all users.
        """
        if user_id:
            queryset = User.objects.filter(id=user_id, role=1)
        else:
            queryset = User.objects.all(role=1)
        serializer = getUserSerializer(queryset, many=True)
        data = {
            "data": serializer.data, "code": HTTP_200_OK, "message": OK, "status": 200
        }
        return data

    def update_user_admin(self, request):
        """
        This method is used to update users password.
        """
        user_id = request.data.get('user_id', None)
        # check user id exists in request or not
        if user_id:
            user = User.objects.get(id=user_id)
            # serialize user details on basis of user id
            serializer = crudUserSerializer(
                user, data=request.data, partial=True
            )
            if serializer.is_valid():
                serializer.save()
                result = {'data': serializer.data, 'code': HTTP_200_OK, 'message': OK, "status": 200}
            else:
                result = {'data': serializer.errors, 'code': 500, 'message': FAIL, "status": 500}
        else:
            result = {'data': 'Invalid parameters', 'code': 500, 'message': FAIL, "status": 500}
        return result

    def updateUserPassword(self, request, oldPassword, newPassword):
        """
        This method is used to update users password.
        """
        user_data = User.objects.get(id=request.user.id)
        if user_data.check_password(oldPassword):
            # serialize logged in user details
            password = {'password': newPassword}
            serializer = crudUserSerializer(
                request.user, data=password, partial=True
            )
            # update user details if serializer valid
            if serializer.is_valid():
                serializer.save()
                result = {'data': serializer.data, 'code': HTTP_200_OK, 'message': 'password updated.', 'status': 200}
            else:
                result = {'data': serializer.errors, 'code': 500, 'message': 'Error in updating password.', 'status': 500}
        else:
            result = {'data': 'fail', 'code': 500,
                          'message': 'Your old password does not match with current password.', 'status': 500}

        return result

    def updateEmailPassword(self, request, email, role, password):
        """
        This method is used to update users password.
        """
        user_data = User.objects.get(email=email, role=role)
        # serialize logged in user details
        password_data = {'password': password}
        serializer = crudUserSerializer(
            user_data, data=password_data, partial=True
        )
        # update user details if serializer valid
        if serializer.is_valid():
            serializer.save()
            result = {'data': serializer.data, 'code': HTTP_200_OK, 'message': 'password updated.', 'status': 200}
        else:
            result = {'data': serializer.errors, 'code': 500, 'message': 'Error in updating password.', 'status': 500}
        return result

    def send_reset_password_mail(self, request):
        email = request.data.get("email", None)
        if email:
            validation_check = self.user_validation(email)
            if validation_check:
                password_token = self.encode_jwt(email)
                token = str(password_token)[1:].replace("'", "")
                main_url = ""
                password_reset_url = str(main_url) + f"reset-pwd/email/{token}"
                message_html = f"Please click on Password button to change your password <br><a class='button' href='{password_reset_url}'> Password Reset</a>"
                subject = "Password Reset"
                message = ""
                sendEmailsWithoutBroker(subject, message, [email], message_html, email)
                data = {
                    'data': 'password reset email sent successfully.', 'code': HTTP_200_OK, 'message': OK, "status": 200
                }
            else:
                data = {"data": "user is not found", 'code': 500, 'message': FAIL, "status": 500}
        else:
            data = {'code': 500, 'message': FAIL, "status": 500}
        return data

    def update_password_reset(self, request):
        """
        This method is used to update users password.
        """
        token = request.data.get('token', None)
        password = request.data.get('password', None)
        if token and password:
            decoded = self.decode_jwt(token)
            # check whether decoded data is empty on not
            if decoded:
                email = decoded["email"]
                instance = User.objects.get(email=email)
                password = {'password': password}
                serializer = crudUserSerializer(
                    instance, data=password, partial=True
                )
                # update user details if serializer valid
                if serializer.is_valid():
                    serializer.save()
                    data = {'data': serializer.data, 'code': 200, 'message': OK, "status": 200}
                else:
                    data = {'data': serializer.errors, 'code': 500, 'message': FAIL, "status": 200}
            else:
                data = {'data': {"message": "Link is not valid"}, 'code': 500, 'message': FAIL, "status": 500}
        else:
            data = {'code': 500, 'message': FAIL, "status": 500}
        return data

    def verify_auth_device(self, request):
        return

    def verify_auth_code(self, phone, code):
        client = Client(accountSid, authToken)
        try:
            if phone and code:
                client.messages.create(
                    body=f'Your Phone Verification Code is {code}',
                    from_=SenderMobile,
                    to=phone
                )
                status = True
        except:
            status = False
        return status

    def email_verification_code(self, email):
        return

    def send_notification(self, request_data):
        try:
            service_id = request_data["service"]["id"]
            request_id = request_data["id"]
            u_lat = request_data["latitude"]
            u_lng = request_data["longitude"]
            instances = User.objects.filter(services_id__icontains=str(service_id))
            # device_tokens = [x.device_token for x in instances]
            device_tokens = []
            loc_range = 0
            while len(device_tokens) < 1:
                loc_range += 30
                tokens = self.nearby_roadhero(instances, u_lat, u_lng, loc_range)
                device_tokens += tokens
                if loc_range == 120:
                    device_tokens += [x.device_token for x in instances]
                    break
            message_title = "Welcome to RoadHero"
            message_body = f"New Request #{request_id} Received."
            screen_type = "requests"
            result = send_push_notification(device_tokens, message_title, message_body, screen_type, False)
        except:
            result = 400
        return result

    def send_payment_notification(self, request_data, message):
        try:
            service_id = request_data["service"]["id"]
            request_id = request_data["id"]
            u_lat = request_data["latitude"]
            u_lng = request_data["longitude"]
            instances = User.objects.filter(services_id__icontains=str(service_id))
            # device_tokens = [x.device_token for x in instances]
            device_tokens = []
            loc_range = 0
            while len(device_tokens) < 1:
                loc_range += 30
                tokens = self.nearby_roadhero(instances, u_lat, u_lng, loc_range)
                device_tokens += tokens
                if loc_range == 120:
                    device_tokens += [x.device_token for x in instances]
                    break
            message_title = "RoadHero Payment Status"
            message_body = message
            screen_type = "requests"
            result = send_push_notification(device_tokens, message_title, message_body, screen_type, False)
        except:
            result = 400
        return result

    def get_distance_between_two_locations(self, lat1, lon1, lat2, lon2):
        R = 6373.0
        lat1 = radians(float(lat1))
        lon1 = radians(float(lon1))
        lat2 = radians(float(lat2))
        lon2 = radians(float(lon2))

        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        distance = R * c
        return distance

    def nearby_roadhero(self, instances, u_lat, u_lng, loc_range):
        range = float(loc_range / 1.609)
        vendors = []
        device_tokens = []
        for instance in instances:
            v_id = instance.id
            v_lat = instance.latitude
            v_lng = instance.longitude
            device_token = instance.device_token
            if v_lat and v_lng:
                distance = self.get_distance_between_two_locations(u_lat, u_lng, v_lat, v_lng)
                if distance <= range:
                    vendors.append(v_id)
                    device_tokens.append(device_token)
            else:
                pass
        return device_tokens

class addPaymentDetails(views.APIView):
    """
    This api is used to save bank payment authorization details.
    """
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        user_id = request.user.id
        w9_form = request.data.get("w9_form", None)
        driver_licence_front = request.data.get("driver_licence_front", None)
        driver_licence_back = request.data.get("driver_licence_back", None)
        reg_insurence = request.data.get("reg_insurence", None)
        background_check = request.data.get("background_check", None)
        authorization_form = request.data.get("authorization_form", None)
        serialize_data = {
            "user": request.user.id
        }
        if w9_form == 'null' or w9_form == 'None' or w9_form == None:
            pass
        else:
            serialize_data["w9_form"] = w9_form
        if driver_licence_back == 'null' or driver_licence_back == 'None' or driver_licence_back == None:
            pass
        else:
            serialize_data["ica_form"] = driver_licence_back
        if driver_licence_front == 'null' or driver_licence_front == 'None' or driver_licence_front == None:
            pass
        else:
            serialize_data["driver_licence_front"] = driver_licence_front
        if authorization_form == 'null' or authorization_form == 'None' or authorization_form == None:
            pass
        else:
            serialize_data["authorization_form"] = authorization_form
        if reg_insurence == 'null' or reg_insurence == 'None' or reg_insurence == None:
            pass
        else:
            serialize_data["reg_insurence"] = reg_insurence
        if background_check == 'null' or background_check == 'None' or background_check == None:
            pass
        else:
            serialize_data["background_check"] = background_check
        instance = VenderDetails.objects.filter(user=user_id)
        if len(instance) > 0:
            serializer = VendorDetailSerializer(instance[0], data=serialize_data, partial=True)
            if serializer.is_valid():
                serializer.save()
                data = {
                    "status": 200, "code": 200, "data": serializer.data, "message": OK
                }
            else:
                data = {
                    "status": 400, "code": 400, "data": serializer.errors, "message": FAIL
                }
        else:
            serializer = VendorDetailSerializer(data=serialize_data)
            if serializer.is_valid():
                serializer.save()
                data = {
                    "status": 200, "code": 200, "data": serializer.data, "message": OK
                }
            else:
                data = {
                    "status": 400, "code": 400, "data": serializer.errors, "message": FAIL
                }
        print("data : ", data)
        return views.Response(data, status=HTTP_200_OK)

class checkPaymentDetails(views.APIView):
    """
    This api is used to save bank payment authorization details.
    """
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        instance = VenderDetails.objects.filter(user=request.user)
        if len(instance) > 0:
            serializer = VendorDetailSerializer(instance[0])
            data = {
                "status": 200, "code": 200, "data": serializer.data, "message": OK
            }
        else:
            data = {
                "status": 400, "code": 400, "message": FAIL
            }
        return views.Response(data, status=HTTP_200_OK)
