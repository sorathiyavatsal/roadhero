from rest_framework import views, response, permissions
from rest_framework.status import *
from api.utils import *
from django.utils import timezone
from math import sin, cos, sqrt, atan2, radians
import time
from pyfcm import FCMNotification
from api.models import (
    VehicleModel, VehicleCompany, VehicleInfo, VehicleColor,
    BookingHistory, serviceRequest, Service, PaymentAccount,
    VerificationCode, PackageDelivery, VenderDetails, Offer
)
from api.serializers import (
    getVehicleModelSerializer, VehicleCompanySerializer,
    VehicleInfoSerializer, VehicleColorSerializer, BookingHistorySerializer,
    getBookingHistorySerializer, ServiceRequestSerializer, getServiceRequestSerializer,
    ServiceSerializer, PaymentAccountSerializer, VehicleModelSerializer,
    PackageDeliverySerializer
)
from django.contrib.auth import get_user_model
User = get_user_model()
push_service = FCMNotification(api_key=config("FCM_SERVER_KEY"))


class AddCompany(views.APIView):
    """
    This is service class to manage trips methods.
    """
    permission_classes = [permissions.AllowAny]
    def post(self, request, format=None):
        serializer = VehicleCompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {'data': serializer.data, "status": 200, "code": 200, 'message': "All colors."}
        else:
            data = {'data': serializer.errors, "status": 400, "code": 400, 'message': "Failed"}
        return views.Response(data, status=HTTP_200_OK)
class AddCompanyModel(views.APIView):
    """
    This is service class to manage trips methods.
    """
    permission_classes = [permissions.AllowAny]
    def post(self, request, format=None):
        serializer = VehicleModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {'data': serializer.data, "status": 200, "code": 200, 'message': "data added."}
        else:
            data = {'data': serializer.errors, "status": 400, "code": 400, 'message': "Failed"}
        return views.Response(data, status=HTTP_200_OK)
        
class AddColors(views.APIView):
    """
    This is service class to manage trips methods.
    """
    permission_classes = [permissions.AllowAny]
    def post(self, request, format=None):
        serializer = VehicleColorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        data = {"status": 200, "code": 200, 'message': "data added."}
        return views.Response(data, status=HTTP_200_OK)

class AddYear(views.APIView):
    """
    This is service class to manage trips methods.
    """
    permission_classes = [permissions.AllowAny]
    def post(self, request, format=None):
        serializer = VehicleInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

        data = {"status": 200, "code": 200, 'message': "data added."}
        return views.Response(data, status=HTTP_200_OK)
        
class getVehicleColors(views.APIView):
    """
    This is service class to manage trips methods.
    """
    permission_classes = [permissions.AllowAny]
    def get(self, request, model_id=None):
        instance = VehicleColor.objects.all()
        serializer = VehicleColorSerializer(instance, many=True)
        data = {'data': serializer.data, "status": 200, "code": 200, 'message': "All colors."}
        return views.Response(data, status=HTTP_200_OK)

class getVehicleColor(views.APIView):
    """
    This is service class to manage trips methods.
    """
    permission_classes = [permissions.AllowAny]
    def get(self, request, id=None):
        instance = VehicleColor.objects.filter(id=id)
        serializer = VehicleColorSerializer(instance, many=True)
        data = {'data': serializer.data, "status": 200, "code": 200, 'message': "All colors."}
        return views.Response(data, status=HTTP_200_OK)

class getVehicleModels(views.APIView):
    """
    This is service class to manage trips methods.
    """
    permission_classes = [permissions.AllowAny]
    def get(self, request, company_id=None):
        if company_id:
            # making filter set on basis of requested search
            instance = VehicleModel.objects.filter(vehicle_company=company_id)

            # searialize queryset data
            serializer = getVehicleModelSerializer(instance, many=True)
            data = {'data': {"array": serializer.data}, "status": 200, "code": 200, 'message': "All required models."}
        else:
            data = {"status": 400, "code": 400, 'message': "error occurred."}
        return views.Response(data, status=HTTP_200_OK)

class getVehicleModel(views.APIView):
    """
    This is service class to manage trips methods.
    """
    permission_classes = [permissions.AllowAny]
    def get(self, request, id=None):
        if id:
            # making filter set on basis of requested search
            instance = VehicleModel.objects.filter(id=id)

            # searialize queryset data
            serializer = getVehicleModelSerializer(instance, many=True)
            data = {'data': {"array": serializer.data}, "status": 200, "code": 200, 'message': "All required models."}
        else:
            data = {"status": 400, "code": 400, 'message': "error occurred."}
        return views.Response(data, status=HTTP_200_OK)

class getVehicleCompany(views.APIView):
    """
    This is service class to manage trips methods.
    """
    permission_classes = [permissions.AllowAny]
    def get(self, request, id=None):
        # making filter set on basis of requested search
        instance = VehicleCompany.objects.filter(id=id)
        # searialize queryset data
        serializer = VehicleCompanySerializer(instance, many=True)
        data = {'data': {"array": serializer.data}, "status": 200, "code": 200, 'message': "All company."}
        return views.Response(data, status=HTTP_200_OK)
class getVehicleCompanies(views.APIView):
    """
    This is service class to manage trips methods.
    """
    permission_classes = [permissions.AllowAny]
    def get(self, request, format=None):
        # making filter set on basis of requested search
        instance = VehicleCompany.objects.all()
        # searialize queryset data
        serializer = VehicleCompanySerializer(instance, many=True)
        data = {'data': {"array": serializer.data}, "status": 200, "code": 200, 'message': "All company."}
        return views.Response(data, status=HTTP_200_OK)

class getVehicleInfo(views.APIView):
    """
    This is service class to manage trips methods.
    """
    permission_classes = [permissions.AllowAny]
    def get(self, request, id=None):
        if id:
            # making filter set on basis of requested search
            instance = VehicleInfo.objects.filter(id=id)
            # searialize queryset data
            serializer = VehicleInfoSerializer(instance, many=True)
            data = {'data': {"array": serializer.data}, "status": 200, "code": 200, 'message': "All Vehicle info.."}
        else:
            data = {'status': 400, 'message': "No records found"}
        return views.Response(data, status=HTTP_200_OK)

class getVehicleInfoes(views.APIView):
    """
    This is service class to manage trips methods.
    """
    permission_classes = [permissions.AllowAny]
    def get(self, request, format=None):
        instance = VehicleInfo.objects.all().order_by('-id')
        # searialize queryset data
        serializer = VehicleInfoSerializer(instance, many=True)
        data = {'data': {"array": serializer.data}, "status": 200, "code": 200, 'message': "All Vehicle Year.."}
        return views.Response(data, status=HTTP_200_OK)

class setVehicleInfo(views.APIView):
    """
    This is service class to manage trips methods.
    """
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        request_data = request.data.get("details", None)
        if request_data:
            user_id = request_data.get("user_id", None)
            company_id = request_data.get("company_id", None)
            model_id = request_data.get("model_id", None)
            year = request_data.get("year", None)
            color_id = request_data.get("color_id", None)
            name = request_data.get("name", None)
            serialize_data = {
                'vehicle_model': model_id, 'user': user_id, "vehicle_color": color_id,
                "vehicle_company": company_id, "name": name, "year": year
            }
            instance = VehicleInfo.objects.filter(
                vehicle_model=model_id, user=user_id, vehicle_color=color_id,
                vehicle_company=company_id, year=year
            )
            if len(instance) > 0:
                data = {'status': 400, 'message': "VehicleInfo already exists."}
            else:
                # searialize queryset data
                serializer = VehicleInfoSerializer(data=serialize_data)
                if serializer.is_valid():
                    serializer.save()
                    data = {'data': {"array": serializer.data}, "status": 200, "code": 200, 'message': "All Vehicle info.."}
                else:
                    data = {'status': 400, 'message': "Error in adding VehicleInfo."}
        else:
            data = {'status': 400, 'message': "Error in adding VehicleInfo."}
        return views.Response(data, status=HTTP_200_OK)

class addServiceRequest(views.APIView):
    """
    This is service class to manage trips methods.
    """
    permission_classes = [permissions.AllowAny]
    def post(self, request, format=None):
        vehicle = request.data.get("vehicle", None)
        vehicle_color = request.data.get("vehicle_color", None)
        vehicle_year = request.data.get("vehicle_year", None)
        service = request.data.get("service", None)
        name = request.data.get("name", None)
        mobile = request.data.get("mobile", None)
        email = request.data.get("email", None)
        latitude = request.data.get("latitude", None)
        longitude = request.data.get("longitude", None)
        promo_code = request.data.get("promo_code", None)
        service_note = request.data.get("service_note", None)
        delivery_from = request.data.get("delivery_from", None)
        delivery_to = request.data.get("delivery_to", None)
        delivery_details = request.data.get("delivery_details", None)
        if name and mobile and service and latitude and longitude and service_note:
            serialize_data = {
                'vehicle': vehicle, 'service': service,  'vehicle_year': vehicle_year, 'vehicle_color': vehicle_color,
                'name': name, 'mobile': mobile, 'email': email, 'service_note': service_note,
                'latitude': latitude, 'longitude': longitude, 'promo_code': promo_code
            }
            serializer = BookingHistorySerializer(data=serialize_data)
            if serializer.is_valid():
                serializer.save()
                if delivery_to and delivery_from:
                    package_serialized_data = {
                        "delivery_to": delivery_to, "delivery_from": delivery_from,
                        "details": delivery_details, "request_id": serializer.data["id"]
                    }
                    package_serializer = PackageDeliverySerializer(data=package_serialized_data)
                    if package_serializer.is_valid():
                        package_serializer.save()
                        lat, lng = get_delivery_lat_lng(delivery_to)
                        b_instance = BookingHistory.objects.get(id=serializer.data["id"])
                        b_instance.latitude = lat
                        b_instance.longitude = lng
                        b_instance.save()
                    else:
                        b_instance = BookingHistory.objects.get(id=serializer.data["id"])
                        b_instance.delete()
                # send_notification(serializer.data)
                data = {'data': serializer.data, "status": 200, "code": 200, 'message': "Service request Added."}
            else:
                data = {'data': serializer.errors, 'status': 400, 'code': 400, 'message': "Error in adding service request."}
        else:
            data = {'status': 400, 'code': 400, 'message': "Invalid service request."}
        print(data)
        return views.Response(data, status=HTTP_200_OK)

class getBookingSummary(views.APIView):
    """
    This is service class to manage trips methods.
    """
    permission_classes = [permissions.AllowAny]
    def get(self, request, id=None):
        instance = BookingHistory.objects.get(id=id)
        serializer = getBookingHistorySerializer(instance)

        serialized_data = serializer.data
        if instance.service.id == 4:
            instance2 = PackageDelivery.objects.get(request_id=id)
            serialized_data["delivery_from"] = instance2.delivery_from
            serialized_data["delivery_to"] = instance2.delivery_to
            serialized_data["delivery_details"] = instance2.details
        else:
            serialized_data["price"] = instance.service.price
        data = {'data': [serialized_data], "status": 200, "code": 200, 'message': "Fetched booking summary"}
        return views.Response(data, status=HTTP_200_OK)

class updateServiceRequest(views.APIView):
    """
    This is service class to manage trips methods.
    """
    permission_classes = [permissions.AllowAny]
    def put(self, request, format=None):
        request_id = request.data.get("id", None)
        if request_id:
            instance = BookingHistory.objects.get(id=id)
            serializer = BookingHistorySerializer(instance, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                data = {"data": serializer.data, "code": 200, "status": 200, "message": "Request updated."}
            else:
                data = {"data": serializer.errors, "code": 400, "status": 400, "message": "Request updated."}
        else:
            data = {"code": 400, "status": 400, "message": "Request updated."}
        return views.Response(data, status=HTTP_200_OK)

class deleteServiceRequest(views.APIView):
    """
    This is service class to manage trips methods.
    """
    permission_classes = [permissions.AllowAny]
    def get(self, request, id=None):
        if id:
            # making filter set on basis of requested search
            try:
                instance = BookingHistory.objects.get(id=id)
                instance.delete()
                data = {"status": 200, "code": 200, 'message': "Request deleted.."}
            except:
                data = {'status': 400, 'code': 400, 'message': "Error in deleting request."}
        else:
            data = {'status': 400, 'code': 400, 'message':  "Error in deleting request."}
        return views.Response(data, status=HTTP_200_OK)

class getBookingHistory(views.APIView):
    """
    This is service class to manage trips methods.
    """
    permission_classes = [permissions.AllowAny]
    def get(self, request, mobile=None):
        instance = BookingHistory.objects.filter(mobile=mobile).order_by('-id')[:20]
        if len(instance) > 0:
            serializer = getBookingHistorySerializer(instance, many=True)
            serialized_data = []
            for i_data in serializer.data:
                if i_data["service"]["id"] == 4:
                    instance2 = PackageDelivery.objects.get(request_id=i_data["id"])
                    i_data["delivery_from"] = instance2.delivery_from
                    i_data["delivery_to"] = instance2.delivery_to
                    i_data["delivery_details"] = instance2.details
                else:
                    pass
                serialized_data.append(i_data)
            data = {"data": serialized_data, "status": 200, "code": 200, 'message': "Booking histories"}
        else:
            data = {'status': 400, 'code': 400, 'message': "No Booking History Found"}
        return views.Response(data, status=HTTP_200_OK)

class servicePrice(views.APIView):
    """
    This is service class to manage trips methods.
    """
    permission_classes = [permissions.AllowAny]
    def get(self, request, request_id=None):
        instance = BookingHistory.objects.filter(id=request_id)
        if len(instance) > 0:
            booking_id = instance[0].id
            service_id = instance[0].service.id
            price = instance[0].service.price
            discount_offer = Offer.objects.filter(promo_code=instance[0].promo_code)
            if len(discount_offer) > 0:
                discount = int(discount_offer[0].discount)
            else:
                discount = 0
            if int(service_id) == 3:
                u_lat = instance[0].latitude
                u_lng = instance[0].longitude
                instances = User.objects.filter(services_id__icontains=str(service_id))
                distances = []
                loc_range = 0
                while len(distances) < 1:
                    loc_range += 30
                    dist = nearby_roadhero(instances, u_lat, u_lng, loc_range)
                    distances += dist
                    if loc_range == 120:
                        break
                print(distances)
                try:
                    max_distance = max(distances)
                    real_distance = max_distance - 30
                    if real_distance < 1:
                        extra_price = 0
                    else:
                        extra_price = real_distance * 1
                    price = price + extra_price
                except:
                    price = price
                total_discount = round(price * (discount / 100))
                amount = price - total_discount
            else:
                total_discount = round(price * (discount/100))
                amount = price - total_discount
            instance[0].price = amount
            instance[0].save()

            serialize_data = {"request_id": booking_id, "amount": amount}
            data = {"data": serialize_data, "status": 200, "code": 200, 'message': "Total amount"}
        else:
            data = {'status': 400, 'code': 400, 'message': "Request id is not valid"}
        return views.Response(data, status=HTTP_200_OK)

class updateRequest(views.APIView):
    """
    This is service class to manage trips methods.
    """
    permission_classes = [permissions.AllowAny]
    def post(self, request, format=None):
        request_id = request.data.get("request_id", None)
        rating = request.data.get("rating", None)
        review = request.data.get("review", None)
        instance = serviceRequest.objects.filter(request_id=request_id)
        if len(instance) > 0:
            serialize_data = {
                "rating": rating, "review": review,
                "request_status": True
            }
            booking_instance = BookingHistory.objects.get(id=request_id)
            serializer = ServiceRequestSerializer(instance[0], data=serialize_data, partial=True)
            if serializer.is_valid():
                serializer.save()
                booking_instance.rating = rating
                booking_instance.save()
                data = {"data": serializer.data, "status": 200, "code": 200, 'message': "Request is updated."}
            else:
                data = {'status': 400, 'code': 400, 'message': "Error in updating request."}

        else:
            data = {'status': 400, 'code': 400, 'message': "Request id is not valid"}
        return views.Response(data, status=HTTP_200_OK)

class AcceptVendorServiceRequest(views.APIView):
    """
    This is service class to manage trips methods.
    """
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, format=None):
        request_id = request.data.get("request_id")
        eta = request.data.get("eta", None)
        doc_verify = request.user.doc_verify
        if not doc_verify:
            data = {'status': 400, 'code': 400, 'message': "Please verify your document first."}
            return views.Response(data, status=HTTP_200_OK)
        instance = serviceRequest.objects.filter(request_id=request_id)
        if len(instance) > 0:
            data = {'status': 400, 'code': 400, 'message': "Request already accepted."}
        else:
            serialize_data = {
                'request_id': request_id, "vendor_id": request.user.id, "eta": eta
            }
            serializer = ServiceRequestSerializer(data=serialize_data)
            booking_instance = BookingHistory.objects.get(id=request_id)
            if serializer.is_valid():
                serializer.save()
                booking_instance.vendor = request.user
                booking_instance.save()
                enroute_msg = f"Your RoadHero is in enroute and arrived at {eta}."
                send_motorist_notification(serializer.data["id"], enroute_msg)
                data = {'data': serializer.data, 'status': 200, 'code': 200, 'message': "Request is confirmed."}
            else:
                data = {'status': 400, 'code': 400, 'message': "error in creating service request"}
        return views.Response(data, status=HTTP_200_OK)

class updateVendorServiceRequest(views.APIView):
    """
    This is service class to manage trips methods.
    """
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, format=None):
        request_id = request.data.get("request_id")
        service_status = request.data.get("service_status", True)
        instance = serviceRequest.objects.filter(request_id=request_id)
        if len(instance) > 0:
            serialize_data = {
                "service_status": service_status
            }
            serializer = ServiceRequestSerializer(instance[0], data=serialize_data, partial=True)
            if serializer.is_valid():
                serializer.save()
                data = {"data": serializer.data, "status": 200, "code": 200, 'message': "Request service is completed.."}
            else:
                data = {'status': 400, 'code': 400, 'message': "Error in updating request."}

        else:
            data = {'status': 400, 'code': 400, 'message': "Request id is not valid"}
        return views.Response(data, status=HTTP_200_OK)

class VendorServiceRequestStatus(views.APIView):
    """
    This is service class to manage trips methods.
    """
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, request_id=None):
        instance = serviceRequest.objects.filter(request_id=request_id)
        if len(instance) > 0:
            serialize_data = {
                "service_status": True
            }
            serializer = ServiceRequestSerializer(instance[0], data=serialize_data, partial=True)
            if serializer.is_valid():
                serializer.save()
                data = {"data": serializer.data, "status": 200, "code": 200, 'message': "Request is updated."}
            else:
                data = {'status': 400, 'code': 400, 'message': "Error in updating request."}

        else:
            data = {'status': 400, 'code': 400, 'message': "Request id is not valid"}
        return views.Response(data, status=HTTP_200_OK)

class getAllRequests(views.APIView):
    """
    This is service class to manage trips methods.
    """
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, format=None):
        service_ids = str(request.user.services_id).split(",")
        instances = BookingHistory.objects.filter(
            vendor=None, service__id__in=service_ids, payment_status=True
        ).exclude(cancelled_by__icontains=str(request.user.id)).order_by('-id')[:10]
        serializer = getBookingHistorySerializer(instances, many=True)
        open = []
        for open_data in serializer.data:
            if open_data["service"]["id"] == 4:
                instance2 = PackageDelivery.objects.get(request_id=open_data["id"])
                open_data["delivery_from"] = instance2.delivery_from
                open_data["delivery_to"] = instance2.delivery_to
                open_data["delivery_details"] = instance2.details
            else:
                pass
            open.append(open_data)

        instance1 = serviceRequest.objects.filter(vendor_id=request.user.id, service_status=False)[:10]
        serializer1 = getServiceRequestSerializer(instance1, many=True)
        inprogress = []
        for inprogress_data in serializer1.data:
            if inprogress_data["request_id"]["service"]["id"] == 4:
                instance2 = PackageDelivery.objects.get(request_id=inprogress_data["request_id"]["id"])
                inprogress_data["delivery_from"] = instance2.delivery_from
                inprogress_data["delivery_to"] = instance2.delivery_to
                inprogress_data["delivery_details"] = instance2.details
            else:
                pass
            inprogress.append(inprogress_data)

        instance2 = serviceRequest.objects.filter(vendor_id=request.user.id, service_status=True)[:10]
        serializer2 = getServiceRequestSerializer(instance2, many=True)
        completed = []
        for completed_data in serializer2.data:
            if completed_data["request_id"]["service"]["id"] == 4:
                instance2 = PackageDelivery.objects.get(request_id=completed_data["request_id"]["id"])
                completed_data["delivery_from"] = instance2.delivery_from
                completed_data["delivery_to"] = instance2.delivery_to
                completed_data["delivery_details"] = instance2.details
            else:
                pass
            completed.append(completed_data)
        # completed = serializer2.data

        instance3 = BookingHistory.objects.filter(cancelled_by__icontains=str(request.user.id))[:10]
        serializer3 = getBookingHistorySerializer(instance3, many=True)
        # cancelled = serializer3.data
        cancelled = []
        for cancelled_data in serializer3.data:
            if cancelled_data["service"]["id"] == 4:
                instance2 = PackageDelivery.objects.get(request_id=cancelled_data["id"])
                cancelled_data["delivery_from"] = instance2.delivery_from
                cancelled_data["delivery_to"] = instance2.delivery_to
                cancelled_data["delivery_details"] = instance2.details
            else:
                pass
            cancelled.append(cancelled_data)
        data = {
                "open": open,
                "in_progess": inprogress,
                "completed": completed,
                "cancelled": cancelled
            }
        data = {"data": data, "status": 200, "code": 200, 'message': "All requests."}
        return views.Response(data, status=HTTP_200_OK)

class getOpenRequests(views.APIView):
    """
    This is service class to manage trips methods.
    """
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, format=None):
        service_ids = str(request.user.services_id).split(",")
        instances = BookingHistory.objects.filter(
            vendor=None, service__id__in=service_ids, payment_status=True
        ).exclude(cancelled_by__icontains=str(request.user.id)).order_by('-id')[:10]
        serializer = getBookingHistorySerializer(instances, many=True)
        open = []
        for open_data in serializer.data:
            if open_data["service"]["id"] == 4:
                instance2 = PackageDelivery.objects.get(request_id=open_data["id"])
                open_data["delivery_from"] = instance2.delivery_from
                open_data["delivery_to"] = instance2.delivery_to
                open_data["delivery_details"] = instance2.details
            else:
                pass
            open.append(open_data)
        data = {"data": open, "status": 200, "code": 200, 'message': "Active requests."}
        return views.Response(data, status=HTTP_200_OK)

class getWaitingRequests(views.APIView):
    """
    This is service class to manage trips methods.
    """
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, format=None):
        service_ids = str(request.user.services_id).split(",")
        instances = BookingHistory.objects.filter(
            vendor=None, service__id__in=service_ids, payment_status=True
        ).exclude(cancelled_by__icontains=str(request.user.id)).order_by('-id')[:10]
        serializer = getBookingHistorySerializer(instances, many=True)
        open = []
        for open_data in serializer.data:
            if open_data["service"]["id"] == 4:
                instance2 = PackageDelivery.objects.get(request_id=open_data["id"])
                open_data["delivery_from"] = instance2.delivery_from
                open_data["delivery_to"] = instance2.delivery_to
                open_data["delivery_details"] = instance2.details
            else:
                pass
            open.append(open_data)
        data = {
                "open": open
            }
        data = {"data": data, "status": 200, "code": 200, 'message': "waiting requests."}
        return views.Response(data, status=HTTP_200_OK)

class getActiveRequests(views.APIView):
    """
    This is service class to manage trips methods.
    """
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, format=None):

        instance1 = serviceRequest.objects.filter(vendor_id=request.user.id, service_status=False)[:10]
        serializer1 = getServiceRequestSerializer(instance1, many=True)
        inprogress = []
        for inprogress_data in serializer1.data:
            if inprogress_data["request_id"]["service"]["id"] == 4:
                instance2 = PackageDelivery.objects.get(request_id=inprogress_data["request_id"]["id"])
                inprogress_data["delivery_from"] = instance2.delivery_from
                inprogress_data["delivery_to"] = instance2.delivery_to
                inprogress_data["delivery_details"] = instance2.details
            else:
                pass
            inprogress.append(inprogress_data)
        data = {
                "in_progess": inprogress,
            }
        data = {"data": data, "status": 200, "code": 200, 'message': "All requests."}
        return views.Response(data, status=HTTP_200_OK)

class getCompletedRequests(views.APIView):
    """
    This is service class to manage trips methods.
    """
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, format=None):

        instance2 = serviceRequest.objects.filter(vendor_id=request.user.id, service_status=True)[:10]
        serializer2 = getServiceRequestSerializer(instance2, many=True)
        completed = []
        for completed_data in serializer2.data:
            if completed_data["request_id"]["service"]["id"] == 4:
                instance2 = PackageDelivery.objects.get(request_id=completed_data["request_id"]["id"])
                completed_data["delivery_from"] = instance2.delivery_from
                completed_data["delivery_to"] = instance2.delivery_to
                completed_data["delivery_details"] = instance2.details
            else:
                pass
            completed.append(completed_data)
        # completed = serializer2.data

        data = {
                "completed": completed
            }
        data = {"data": data, "status": 200, "code": 200, 'message': "All requests."}
        return views.Response(data, status=HTTP_200_OK)

class getCancelRequests(views.APIView):
    """
    This is service class to manage trips methods.
    """
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, format=None):

        instance3 = BookingHistory.objects.filter(cancelled_by__icontains=str(request.user.id))[:10]
        serializer3 = getBookingHistorySerializer(instance3, many=True)
        # cancelled = serializer3.data
        cancelled = []
        for cancelled_data in serializer3.data:
            if cancelled_data["service"]["id"] == 4:
                instance2 = PackageDelivery.objects.get(request_id=cancelled_data["id"])
                cancelled_data["delivery_from"] = instance2.delivery_from
                cancelled_data["delivery_to"] = instance2.delivery_to
                cancelled_data["delivery_details"] = instance2.details
            else:
                pass
            cancelled.append(cancelled_data)
        data = {
                "cancelled": cancelled
            }
        data = {"data": data, "status": 200, "code": 200, 'message': "All requests."}
        return views.Response(data, status=HTTP_200_OK)

class getRequest(views.APIView):
    """
    This is service class to manage trips methods.
    """
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, format=None):
        instances = BookingHistory.objects.filter(vendor=None).order_by('-id')
        if len(instances) > 0:
            service_ids = str(request.user.services_id).split(",")
            service_requests = []
            for instance in instances:
                booking_id = instance.id
                service_id = instance.service.id
                cancelled_by = instance.cancelled_by
                cancelled_by = str(cancelled_by).split(",")
                if str(service_id) in service_ids:
                    if str(request.user.id) not in cancelled_by:
                        service_requests.append(booking_id)
                    else:
                        pass
                else:
                    pass
            booking_instance = BookingHistory.objects.filter(id__in=service_requests)
            serializer = getBookingHistorySerializer(booking_instance, many=True)
            data = {"data": serializer.data[0], "status": 200, "code": 200, 'message': "All requests."}

        else:
            data = {"data": [], 'status': 200, 'code': 200, 'message': "No New Request found."}
        return views.Response(data, status=HTTP_200_OK)

class AddPaymentAccount(views.APIView):
    """
    To add bank account of road hero.
    """
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, format=None):
        ac_name = request.data.get("account_name", None)
        ac_number = request.data.get("account_number", None)
        routing_number = request.data.get("routing_number", None)
        personal_id = request.data.get("personal_id", None)
        address = request.data.get("address", None)
        zip_code = request.data.get("zip_code", None)
        front = request.data.get("front_image", None)
        back = request.data.get("back_image", None)
        instance = PaymentAccount.objects.filter(user=request.user.id)
        serialize_data = {
            'user': request.user.id, 'account_name': ac_name, 'account_number': ac_number,
            'routing_number': routing_number, 'personal_id': personal_id, 'address': address,
            'zip_code': zip_code, 'front_image': front, 'back_image': back
        }
        if len(instance) > 0:
            if ac_name and ac_number and routing_number and address and zip_code and front:
                ac_status = instance[0].status
                print(ac_status)
                if not ac_status:
                    serializer = PaymentAccountSerializer(instance[0], serialize_data, partial=True)
                    if serializer.is_valid():
                        serializer.save()
                        data = {"data": serializer.data, "status": 201, "code": 201, 'message': "Account updated."}
                    else:
                        data = {"data": serializer.errors, "status": 400, "code": 400,
                                'message': "Error in updating account."}
                else:
                    data = {"status": 400, "code": 400, 'message': "Error in updating account."}
            else:
                serializer = PaymentAccountSerializer(instance[0])
                data = {"data": serializer.data, "status": 200, "code": 200, 'message': "Account details."}
        else:
            if ac_name and ac_number and routing_number and address and zip_code and front:
                serializer = PaymentAccountSerializer(data=serialize_data)
                if serializer.is_valid():
                    serializer.save()
                    data = {"data": request.data, "status": 200, "code": 200, 'message': "Account added."}
                else:
                    data = {"data": serializer.errors, "status": 400, "code": 400, 'message': "Error in adding account."}

            else:
                data = {'status': 400, 'code': 400, 'message': "No account attached."}
        return views.Response(data, status=HTTP_200_OK)

class vendorServices(views.APIView):
    """
    This is service class to manage trips methods.
    """
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, format=None):
        instances = Service.objects.all()
        serializer = ServiceSerializer(instances, many=True)
        if len(instances) > 0:
            service_ids = str(request.user.services_id).split(",")
            services = []
            for instance in serializer.data:
                service_id = instance["id"]
                if str(service_id) in service_ids:
                    instance["status"] = True
                else:
                    instance["status"] = False
                services.append(instance)
            data = {"data": services, "status": 200, "code": 200, 'message': "All vendor services"}

        else:
            data = {'status': 400, 'code': 400, 'message': "Request id is not valid"}
        return views.Response(data, status=HTTP_200_OK)

class updateVendorServices(views.APIView):
    """
    This is service class to manage trips methods.
    """
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, format=None):
        service_ids = request.data.get("service_ids", None)
        try:
            instance = User.objects.get(id=request.user.id)
            instance.services_id = service_ids
            instance.save()
            data = {"status": 200, "code": 200, 'message': "Services updated."}
        except:
            data = {'status': 400, 'code': 400, 'message': "Error in updating services."}
        return views.Response(data, status=HTTP_200_OK)

class RejectVendorServiceRequest(views.APIView):
    """
    This is service class to manage trips methods.
    """
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, format=None):
        request_id = request.data.get("request_id")
        instance = BookingHistory.objects.filter(id=request_id)
        if len(instance) > 0:
            cancelled_by = instance[0].cancelled_by
            if cancelled_by:
                instance[0].cancelled_by = str(cancelled_by) + f"{request.user.id},"
            else:
                instance[0].cancelled_by = f"{request.user.id},"
            instance[0].save()
            data = {"status": 200, "code": 200, 'message': "Request is cancelled."}
        else:
            data = {'status': 400, 'code': 400, 'message': "Request id is not valid."}
        return views.Response(data, status=HTTP_200_OK)

class getServiceHistory(views.APIView):
    """
    This is service class to manage trips methods.
    """
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, format=None):
        instance = serviceRequest.objects.filter(vendor_id=request.user.id)
        if len(instance) > 0:
            serializer = getServiceRequestSerializer(instance, many=True)
            inprogress = []
            for inprogress_data in serializer.data:
                if inprogress_data["request_id"]["service"]["id"] == 4:
                    instance2 = PackageDelivery.objects.get(request_id=inprogress_data["request_id"]["id"])
                    inprogress_data["delivery_from"] = instance2.delivery_from
                    inprogress_data["delivery_to"] = instance2.delivery_to
                    inprogress_data["delivery_details"] = instance2.details
                else:
                    pass
                inprogress.append(inprogress_data)
            data = {"data": inprogress, "status": 200, "code": 200, 'message': "All service requests."}
        else:
            data = {'status': 400, 'code': 400, 'message': "No records available."}
        return views.Response(data, status=HTTP_200_OK)

class getVendorServiceRequest(views.APIView):
    """
    This is service class to manage trips methods.
    """
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, format=None):
        id = request.data.get("id", None)
        try:
            instance = serviceRequest.objects.get(id=id)
            serializer = getServiceRequestSerializer(instance)
            serialized_data = serializer.data
            if instance.request_id.service.id == 4:
                instance2 = PackageDelivery.objects.get(request_id=instance.request_id.id)
                serialized_data["delivery_from"] = instance2.delivery_from
                serialized_data["delivery_to"] = instance2.delivery_to
                serialized_data["delivery_details"] = instance2.details
            data = {"data": serialized_data, "status": 200, "code": 200, 'message': "service request."}
        except:
            data = {'status': 400, 'code': 400, 'message': "No records available."}
        return views.Response(data, status=HTTP_200_OK)


def send_notification(request_data):
    try:
        service_id = request_data["service"]
        request_id = request_data["id"]
        instances = User.objects.filter(services_id__icontains=str(service_id))
        device_tokens = [x.device_token for x in instances]
        message_title = "Welcome to RoadHero"
        message_body = f"New Request #{request_id} Received."
        screen_type = "History"
        result = send_push_notification(device_tokens, message_title, message_body, screen_type, False)
    except:
        result = 400
    return result

class AddSignature(views.APIView):
    """
    This is service class to manage trips methods.
    """
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, format=None):
        signature = request.data.get("signature", None)
        id = request.data.get("id", None)
        try:
            instance = serviceRequest.objects.get(id=id)
            serialize_data = {
                "signature": signature,
                "service_status": True
            }
            serializer = ServiceRequestSerializer(instance, data=serialize_data, partial=True)
            if serializer.is_valid():
                serializer.save()
                data = {"data": serializer.data, "status": 200, "code": 200, 'message': "Signature added."}
            else:
                data = {"data": serializer.errors, "status": 400, "code": 400, 'message': "Signature not added."}
        except:
            data = {'status': 400, 'code': 400, 'message': "Signature not added."}
        return views.Response(data, status=HTTP_200_OK)

class AddImages(views.APIView):
    """
    This is service class to manage trips methods.
    """
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, format=None):
        id = request.data.get("id", None)
        image1 = request.data.get("image1", None)
        image2 = request.data.get("image2", None)
        image3 = request.data.get("image3", None)
        image4 = request.data.get("image4", None)
        try:
            serialize_data = {
                "image1": image1,
                "image2": image2,
                "image3": image3,
                "image4": image4
            }
            instance = serviceRequest.objects.get(id=id)
            serializer = ServiceRequestSerializer(instance, data=serialize_data, partial=True)
            if serializer.is_valid():
                serializer.save()
                data = {"data": serializer.data, "status": 200, "code": 200, 'message': "Images added."}
            else:
                data = {"data": serializer.errors, "status": 400, "code": 400, 'message': "Images not added."}
        except:
            data = {'status': 400, 'code': 400, 'message': "Images not added."}
        return views.Response(data, status=HTTP_200_OK)

class UpdateTime(views.APIView):
    """
    This is service class to manage trips methods.
    """
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, format=None):
        id = request.data.get("id", None)
        arrived = request.data.get("arrived", False)
        completed = request.data.get("completed", False)
        if arrived:
            data = update_arrival_time(id)
        elif completed:
            data = update_completed_time(id)
        elif arrived and not completed:
            data = update_arrival_time(id)
        elif arrived and completed:
            data = update_completed_time(id)
        else:
            data = {'status': 400, 'code': 400, 'message': "Time not added."}
        return views.Response(data, status=HTTP_200_OK)
class UpdateArrivedTime(views.APIView):
    """
    This is service class to manage trips methods.
    """
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, format=None):
        id = request.data.get("id", None)
        arrived = request.data.get("arrived", None)
        if arrived:
            data = update_arrival_time(id)
        else:
            data = {'status': 400, 'code': 400, 'message': "Time not added."}
        return views.Response(data, status=HTTP_200_OK)

class UpdateCompletedTime(views.APIView):
    """
    This is service class to manage trips methods.
    """
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, format=None):
        id = request.data.get("id", None)
        completed = request.data.get("completed", None)
        if completed:
            data = update_completed_time(id)
        else:
            data = {'status': 400, 'code': 400, 'message': "Time not added."}
        return views.Response(data, status=HTTP_200_OK)

class RequestStatus(views.APIView):
    """
    This is service class to manage trips methods.
    """
    permission_classes = [permissions.AllowAny]
    def post(self, request, format=None):
        id = request.data.get("id", None)
        instance = serviceRequest.objects.filter(request_id=id)
        if len(instance) > 0:
            serializer = getServiceRequestSerializer(instance[0])
            request_data = serializer.data
            request_status = request_data["request_status"]
            service_status = request_data["service_status"]
            created_at = request_data["created_at"]
            eta = request_data["eta"]
            arrived = request_data["arrived"]
            completed = request_data["completed"]
            name = request_data["vendor_id"]["first_name"] + request_data["vendor_id"]["last_name"]
            enroute_msg = f"Your RoadHero is in enroute at {time_12hr(eta)}."
            arrived_msg = f"Your RoadHero has arrived at {time_12hr(arrived)}."
            completed_msg = f"Your Request is completed at {time_12hr(completed)}. Please rate your RoadHero."
            if request_status and service_status:
                data = {
                    "status": 200, "code": 200,
                    "active": 4,
                    "data": [
                        {
                            "id": 1,
                            "message": enroute_msg,
                            "service_status": "Enroute"
                        },
                        {
                            "id": 2,
                            "message": arrived_msg,
                            "service_status": "Arrived"
                        },
                        {
                            "id": 3,
                            "message": completed_msg,
                            "service_status": "Completed"
                        },
                        {
                            "id": 4,
                            "message": "Thank you for your valuable feedback.",
                            "service_status": "Review"
                        }
                    ]
                }
            elif not request_status and service_status:
                data = {
                    "status": 200, "code": 200,
                    "active": 3,
                    "data": [
                        {
                            "id": 1,
                            "message": enroute_msg,
                            "service_status": "Enroute"
                        },
                        {
                            "id": 2,
                            "message": arrived_msg,
                            "service_status": "Arrived"
                        },
                        {
                            "id": 3,
                            "message": completed_msg,
                            "service_status": "Completed"
                        },
                        {
                            "id": 4,
                            "message": None,
                            "service_status": "Review"
                        }
                    ]
                }
            else:
                if arrived:
                    data = {
                        "status": 200, "code": 200,
                        "active": 2,
                        "data": [

                            {
                                "id": 1,
                                "message": enroute_msg,
                                "service_status": "Enroute"
                            },
                            {
                                "id": 2,
                                "message": arrived_msg,
                                "service_status": "Arrived"
                            },
                            {
                                "id": 3,
                                "message": None,
                                "service_status": "Completed"
                            },
                            {
                                "id": 4,
                                "message": None,
                                "service_status": "Review"
                            }
                        ]

                    }
                else:
                    data = {
                        "status": 200, "code": 200,
                        "active": 1,
                        "data": [

                            {
                                "id": 1,
                                "message": enroute_msg,
                                "service_status": "Enroute"
                            },
                            {
                                "id": 2,
                                "message": None,
                                "service_status": "Arrived"
                            },
                            {
                                "id": 3,
                                "message": None,
                                "service_status": "Completed"
                            },
                            {
                                "id": 4,
                                "message": None,
                                "service_status": "Review"
                            }
                        ]

                    }

        else:
            data = {
                "status": 200, "code": 200,
                "active": 1,
                "data": [
                        {
                            "id": 1,
                            "message": "Waiting for request to be accepted.",
                            "service_status": "Waiting"
                        },
                        {
                            "id": 2,
                            "message": None,
                            "service_status": "Enroute"
                        },
                        {
                            "id": 3,
                            "message": None,
                            "service_status": "Arrived"
                        },
                        {
                            "id": 4,
                            "message": None,
                            "service_status": "Completed"
                        }
                    ]
            }
        return views.Response(data, status=HTTP_200_OK)

def send_motorist_notification(request_id, msg):
    try:
        booking_instance = serviceRequest.objects.get(id=request_id)
        instance = VerificationCode.objects.get(mobile=booking_instance.request_id.mobile)
        device_tokens = [instance.device_token]
        message_title = "RoadHero Request status"
        screen_type = "status"
        screen_data = {
           "request_id": request_id
        }
        result = send_push_notification(device_tokens, message_title, msg, screen_type, screen_data)
    except:
        result = 400
    return result

def update_arrival_time(id):
    try:
        instance = serviceRequest.objects.get(id=id)
        arrived = str(timezone.now().time()).split(".")[0]
        serialize_data = {
            "arrived": arrived,
            "step": 2
        }
        serializer = ServiceRequestSerializer(instance, data=serialize_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            msg = f"Your RoadHero has arrived at {arrived}."
            send_motorist_notification(id, msg)
            data = {"data": serializer.data, "status": 200, "code": 200, 'message': "Time added."}
        else:
            data = {"data": serializer.errors, "status": 400, "code": 400, 'message': "Time not added."}
    except:
        data = {'status': 400, 'code': 400, 'message': "Time not added."}
    return data

def update_completed_time(id):
    try:
        instance = serviceRequest.objects.get(id=id)
        completed = str(timezone.now().time()).split(".")[0]
        serialize_data = {
            "completed": completed,
            "step": 3
        }
        serializer = ServiceRequestSerializer(instance, data=serialize_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            msg = f"Your Request is completed at {completed}. Please rate your RoadHero."
            send_motorist_notification(id, msg)
            data = {"data": serializer.data, "status": 200, "code": 200, 'message': "Time added."}
        else:
            data = {"data": serializer.errors, "status": 400, "code": 400, 'message': "Time not added."}
    except:
        data = {'status': 400, 'code': 400, 'message': "Time not added."}
    return data

def check_documents(request):
    try:
        instance = VenderDetails.objects.get(user=request.user)
        a1 = instance.w9_form
        a2 = instance.driver_licence_front
        a3 = instance.driver_licence_back
        a4 = instance.reg_insurence
        a5 = instance.authorization_form
        if a1 and a2 and a3 and a4 and a5:
            status = True
        else:
            status = False
    except:
        status = False
    return status

def get_distance_between_two_locations(lat1, lon1, lat2, lon2):
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

def nearby_roadhero(instances, u_lat, u_lng, loc_range):
    range = float(loc_range / 1.609)
    vendors = []
    distances = []
    for instance in instances:
        v_id = instance.id
        v_lat = instance.latitude
        v_lng = instance.longitude
        if v_lat and v_lng:
            distance = get_distance_between_two_locations(u_lat, u_lng, v_lat, v_lng)
            if distance <= range:
                vendors.append(v_id)
                distances.append(int(distance))
        else:
            pass
    return distances

def time_12hr(t1):
    if t1:
        t2 = str(t1).split(":")
        t3 = t2[0]
        if int(t3) < 12:
            t1 = f"{int(t3)}:{t2[1]} AM"
        else:
            t1 = f"{int(t3)-12}:{t2[1]} PM"
    else:
        t1 = t1
    return t1

def get_delivery_lat_lng(address):
    try:
        response = requests.get(
            f'https://maps.googleapis.com/maps/api/geocode/json?key={config("MAP_KEY")}&address={address}')

        resp_json_payload = response.json()
        loc_data = resp_json_payload['results'][0]['geometry']['location']
        latitude = loc_data["lat"]
        longitude = loc_data["lng"]
    except:
        latitude = 0
        longitude = 0
    return latitude, longitude