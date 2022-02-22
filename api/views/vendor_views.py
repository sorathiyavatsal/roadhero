from rest_framework import views, response, permissions
from rest_framework.status import *
from api.utils import *
from api.models import VenderLocation
from api.serializers import VenderLocationSerializer, crudUserSerializer, getUserSerializer, getVenderLocationSerializer, getServiceRequestSerializer, ServiceRequestSerializer
from django.contrib.auth import get_user_model
import googlemaps
from math import sin, cos, sqrt, atan2, radians
User = get_user_model()

class getVendorLocation(views.APIView):
    """
    This is service class to manage trips methods.
    """
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, id=None):
        vendor_id = id
        if vendor_id:
            instance = VenderLocation.objects.get(user=vendor_id, user__role=2)
            serializer = getVenderLocationSerializer(instance)
            data = {'data': serializer.data, "status": 200, "code": 200, 'message': "Vendor Location found."}
        else:
            data = {"status": 500, "code": 500, 'message': "Unable to find Vendor Location."}
        return views.Response(data, status=HTTP_200_OK)

class setVendorStatus(views.APIView):
    """
    This is service class to manage trips methods.
    """
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, format=None):
        status = request.data.get("status", True)
        instance = User.objects.get(id=request.user.id)
        serializer = crudUserSerializer(instance, data={"status": status}, partial=True)
        if serializer.is_valid():
            serializer.save()
            data = {'data': serializer.data, "status": 200, "code": 200, 'message': "vendor status set."}
        else:
            data = {"status": 400, "code": 400, 'message': "Error occurred."}
        return views.Response(data, status=HTTP_200_OK)

class setVendorLocation(views.APIView):
    """
    This is service class to manage trips methods.
    """
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, id=None, lat=None, lng=None, address=None):
        vendor_id = id
        instance = VenderLocation.objects.filter(user=vendor_id)
        serialize_data = {
            "user": vendor_id, "latitude": lat,
            "longitude": lng, "address": address
        }
        if len(instance) > 0:
            serializer = VenderLocationSerializer(instance[0], data=serialize_data, partial=True)
            if serializer.is_valid():
                serializer.save()
                data = {'data': serializer.data, "status": 200, "code": 200, 'message': "Location Updated."}
            else:
                data = {"status": 400, "code": 400, 'message': "Error in updating Location."}
        else:
            serializer = VenderLocationSerializer(data=serialize_data)
            if serializer.is_valid():
                serializer.save()
                data = {'data': serializer.data, "status": 200, "code": 200, 'message': "Location Added."}
            else:
                data = {"status": 400, "code": 400, 'message': "Error in adding Location."}
        return views.Response(data, status=HTTP_200_OK)

class getAllVendors(views.APIView):
    """
    This is service class to manage trips methods.
    """
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, format=None):
        instance = User.objects.filter(role=2)
        serializer = getUserSerializer(instance, many=True)
        data = {'data': serializer.data, "status": 200, "code": 200, 'message': "All Vendor found."}
        return views.Response(data, status=HTTP_200_OK)

class getVendor(views.APIView):
    """
    This is service class to manage trips methods.
    """
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, vendor_id=None):
        if vendor_id:
            instance = VenderLocation.objects.get(user=vendor_id)
            serializer = getVenderLocationSerializer(instance)
            data = {'data': {"array": serializer.data}, "status": 200, "code": 200, 'message': "vendor found."}
        else:
            data = {"status": 500, "code": 500, "message": "Unable to find Vendor and Vendor Location."}
        return views.Response(data, status=HTTP_200_OK)

class getNearbyVendors(views.APIView):
    """
    This is service class to manage trips methods.
    """
    permission_classes = [permissions.AllowAny]
    def get(self, request, latitude=None, longitude=None):
        range = float(500 / 1.609)
        instance = VenderLocation.objects.all()
        vendors = []
        for vendor in instance:
            v_id = vendor.user.id
            v_lat = float(vendor.latitude)
            v_lng = float(vendor.longitude)
            distance = get_distance_between_two_locations(latitude, longitude, v_lat, v_lng, range)
            print(distance, range)
            if distance <= range:
                vendors.append(v_id)
            else:
                pass
        v_instance = VenderLocation.objects.filter(user__id__in=vendors)
        serializer = VenderLocationSerializer(v_instance, many=True)
        data = {'data': serializer.data, "status": 200, "code": 200, 'message': "Nearby Vendors."}
        return views.Response(data, status=HTTP_200_OK)

class getNearestVendor(views.APIView):
    """
    This is service class to manage trips methods.
    """
    permission_classes = [permissions.AllowAny]
    def get(self, request, u_lat=None, u_lng=None, range=None, id=None):
        range = float(range / 1.609)
        instance = VenderLocation.objects.all()
        vendors = []
        for vendor in instance:
            v_id = vendor.user.id
            v_lat = vendor.latitude
            v_lng = vendor.longitude
            distance = get_distance_between_two_locations(u_lat, u_lng, v_lat, v_lng, range)
            if distance <= range:
                vendors.append(v_id)
            else:
                pass
        v_instance = VenderLocation.objects.filter(user__id__in=vendors)
        serializer = VenderLocationSerializer(v_instance, many=True)
        data = {'data': {"array": serializer.data}, "status": 200, "code": 200, 'message': "Nearby Vendors."}
        return views.Response(data, status=HTTP_200_OK)

class requestVendor(views.APIView):
    """
    This is service class to manage trips methods.
    """
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, format=None):
        request_data = request.data.get('request', None)
        if request_data:
            serializer = ServiceRequestSerializer(data=request_data)
            if serializer.is_valid():
                serializer.save()
                data = {'data': serializer.data, "status": 200, "code": 200, 'message': "Service request added."}
            else:
                data = {'data': serializer.errors, "status": 500, "code": 500, 'message': "Error in adding Service Request."}
        else:
            data = {"status": 500, "code": 500, 'message': "Error in adding Service Request."}
        return views.Response(data, status=HTTP_200_OK)

class UpdateVendorServices(views.APIView):
    """
    This is service class to manage trips methods.
    """
    permission_classes = [permissions.IsAuthenticated]
    def put(self, request, format=None):
        request_data = request.data.get('data', None)
        if request_data:
            service_id = request_data.get("service_id", None)
            vendor_id = request_data.get("id", None)
            instance = User.objects.get(id=vendor_id)
            serialize_data = {"services_id": service_id}
            serializer = crudUserSerializer(instance, data=serialize_data, partial=True)
            if serializer.is_valid():
                serializer.save()
                data = {'data': serializer.data, "status": 200, "code": 200, 'message': "data sent"}
            else:
                data = {"status": 500, "code": 500, 'message': "data not saved."}
        else:
            data = {"status": 500, "code": 500, 'message': "data not saved."}
        return views.Response(data, status=HTTP_200_OK)

def find_nearby_vendor(lat, lng):
    gmaps = googlemaps.Client(key='AIzaSyBb2vs6drBrCboni9DWaW_CVtcSd6_U4SE')
    reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))
    print(reverse_geocode_result)
    return

def get_distance_between_two_locations(lat1, lon1, lat2, lon2, range=None):
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