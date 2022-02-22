from rest_framework import views, response, permissions
from django.shortcuts import HttpResponse
from rest_framework.status import *
from api.utils import *
from api.serializers import (
    ServiceSerializer, ServiceRequestSerializer, getServiceRequestSerializer,
    OfferSerializer, getQNASerializer, FAQSerializer
)
from api.models import Service, serviceRequest, Offer, AppDetail, QNaModel, FAQ

class getServices(views.APIView):
    """
    This method is to list services.

    """
    permission_classes = [permissions.AllowAny]
    def get(self, request, format=None):
        instance = Service.objects.all()
        serializer = ServiceSerializer(instance, many=True)
        data = {"status": 200, "code": 200, "message": "All services.", "data": serializer.data}
        return views.Response(data, status=HTTP_200_OK)

class getServicesRequest(views.APIView):
    """
    This method is to list services.
    """
    permission_classes = [permissions.AllowAny]
    def get(self, request, format=None):
        instance = serviceRequest.objects.filter(vendor_id=None)
        serializer = getServiceRequestSerializer(instance, many=True)
        data = {"status": 200, "code": 200, "message": "All services.", "data": {"array": serializer.data}}
        return views.Response(data, status=HTTP_200_OK)

class cancelRequest(views.APIView):
    """
    This method is to list services.
    """
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, req_id=None, id=None, role=None):
        try:
            instance = serviceRequest.objects.get(id=req_id)
            instance.is_deleted = True
            instance.save()
            data = {"status": 200, "code": 200, "message": "Request Canceled."}
        except:
            data = {"status": 500, "code": 500, "message": "Error in Deleting Service Request."}
        return views.Response(data, status=HTTP_200_OK)

class getOffer(views.APIView):
    """
    This method is to list services.
    """
    permission_classes = [permissions.AllowAny]
    def get(self, request, format=None):
        try:
            instance = Offer.objects.filter(is_active=True)
            serializer = OfferSerializer(instance, many=True)

            data = {"data": serializer.data, "status": 200, "code": 200, "message": "All Offers."}
        except:
            data = {"status": 400, "code": 400, "message": "Error in Deleting Service Request."}
        return views.Response(data, status=HTTP_200_OK)

class getAboutUs(views.APIView):
    """
    This method is to list services.
    """
    permission_classes = [permissions.AllowAny]
    def get(self, request, format=None):
        try:
            instance = AppDetail.objects.all()
            details = {
                "about_us": instance[0].about_us,
                "contact": instance[0].office_number,
                "email": instance[0].about_email
            }

            data = {"data": details, "status": 200, "code": 200, "message": "About Us."}
        except:
            data = {"status": 400, "code": 400, "message": "Error in Deleting Service Request."}
        return views.Response(data, status=HTTP_200_OK)

class getHelpUs(views.APIView):
    """
    This method is to list services.
    """
    permission_classes = [permissions.AllowAny]
    def get(self, request, format=None):
        try:
            instance = AppDetail.objects.all()
            faq_instance = FAQ.objects.filter(faq_type=2)
            serializer = FAQSerializer(faq_instance, many=True)
            details = {
                "help": instance[0].help,
                "contact": instance[0].help_number,
                "email": instance[0].help_email,
                "faq": serializer.data
            }


            data = {
                "data": details,
                "status": 200,
                "code": 200,
                "message": "Help"
            }
        except:
            data = {"status": 400, "code": 400, "message": "Error in Deleting Service Request."}
        return views.Response(data, status=HTTP_200_OK)

class RoadHeroHelp(views.APIView):
    """
    This method is to list services.
    """
    permission_classes = [permissions.AllowAny]
    def get(self, request, format=None):
        try:
            instance = AppDetail.objects.all()
            faq_instance = FAQ.objects.filter(faq_type=1)
            serializer = FAQSerializer(faq_instance, many=True)
            details = {
                "help": instance[0].help,
                "contact": instance[0].help_number,
                "email": instance[0].help_email,
                "faq": serializer.data
            }

            data = {
                "data": details,
                "status": 200,
                "code": 200,
                "message": "Help"
            }
        except:
            data = {"status": 400, "code": 400, "message": "Error in Deleting Service Request."}
        return views.Response(data, status=HTTP_200_OK)

class getBookingText(views.APIView):
    """
    This method is to list services.
    """
    permission_classes = [permissions.AllowAny]
    def get(self, request, format=None):
        try:
            instance = AppDetail.objects.all()
            details = {
                "booking_text": instance[0].booking_text
            }

            data = {"data": details, "status": 200, "code": 200, "message": "booking_text"}
        except:
            data = {"status": 400, "code": 400, "message": "Error in Deleting Service Request."}
        return views.Response(data, status=HTTP_200_OK)

class getQNA(views.APIView):
    """
    This method is to list services.
    """
    permission_classes = [permissions.AllowAny]
    def get(self, request, service=None):
        instance = QNaModel.objects.filter(service=service)
        serializer = getQNASerializer(instance, many=True)
        data = {"data": serializer.data, "status": 200, "code": 200, "message": "Qna options"}
        return views.Response(data, status=HTTP_200_OK)

class getTerms(views.APIView):
    """
    This method is to list services.
    """
    permission_classes = [permissions.AllowAny]
    def get(self, request, format=None):
        try:
            instance = AppDetail.objects.all()
            details = {
                "terms": instance[0].terms
            }
            data = {"data": details, "status": 200, "code": 200, "message": "Terms and conditions."}
        except:
            data = {"status": 400, "code": 400, "message": "Error in getting Terms and conditions."}
        return views.Response(data, status=HTTP_200_OK)