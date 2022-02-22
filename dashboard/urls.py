from django.contrib import admin
from django.urls import path, include
from .views import *
app_name = 'dashboard'
urlpatterns = [
    path("", login, name="login"),
    path("tos", tos, name="terms of services"),
    path("login", login, name="login"),
    path("logout", logout, name="logout"),
    path("index", index, name="home"),
    path("services", services, name="services"),
    path("user_request", user_request, name="user_request"),
    path("waiting_requests", waiting_requests, name="requests"),
    path("accept_request", accept, name="accept_request"),
    path("reject_request", reject, name="reject_request"),
    path("active_requests", active_requests, name="active_requests"),
    path("update_roadhero", update_roadhero, name="update_roadhero"),
    path("update_time", update_time, name="update_time"),
    path("upload_documents", active_requests, name="upload_documents"),
    path("completed_requests", completed_requests, name="completed_requests"),
    path("requests", AllRequests, name="requests"),
    path("view_request", view_request_details, name="view_request"),
    path("update_request", update_request, name="requests"),
    path("vehicle", vehicle, name="vehicle"),
    path("view_vehicle_make", view_vehicle_make, name="view_vehicle_make"),
    path("view_vehicle_models", view_vehicle_models, name="view_vehicle_models"),
    path("view_vehicle_colors", view_vehicle_colors, name="view_vehicle_colors"),
    path("view_vehicle_years", view_vehicle_years, name="view_vehicle_years"),
    path("view_roadhero", view_roadhero, name="view_roadhero"),
    path("view_motorist", view_motorist, name="view_motorist"),
    path("edit_roadhero", edit_roadhero, name="edit_roadhero"),
    path("edit_motorist", edit_motorist, name="edit_motorist"),
    path("terms_conditions", terms_conditions, name="terms-and-conditions"),
    path("AddDocument", AddDocument, name="AddDocuments"),
    path("view_roadhero_documents", view_roadhero_documents, name="view_roadhero_documents"),

]