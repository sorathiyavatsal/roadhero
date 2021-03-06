from django.urls import path, include
from api import views

app_name = 'api'

urlpatterns = [
    # User related API's url
    path("codeValidation/<str:email>/<str:code>/<int:role>", views.verifyCode.as_view()),
    path("logout", views.logout_view.as_view()),
    path("forgetPassword", views.reset_password_mail.as_view()),

    path("getUser/<int:user_id>", views.get_users.as_view()),
    path("UpdatePhoneNumber", views.update_phone.as_view()),

    path("uploadImage", views.update_login_user.as_view()),
    path("setRating", views.setRating.as_view()),
    path("setRatingReview", views.setRating.as_view()),
    path("getRatingReview", views.getRatingReview.as_view()),
    path("updatePassword/<str:email>/<int:role>/<str:password>", views.reset_password.as_view()),


    # Vendor related API's Urls
    path("getVendorLocation/<int:id>", views.getVendorLocation.as_view()),

    path("getAllVendors", views.getAllVendors.as_view()),
    path("getVendor/<int:vendor_id>", views.getVendor.as_view()),
    path("getNearbyVendors/<str:latitude>/<str:longitude>", views.getNearbyVendors.as_view()),
    path("getNearestVendor/<str:u_lat>/<str:u_lng>/<int:range>/<int:id>", views.getNearestVendor.as_view()),
    path("requestVendor", views.requestVendor.as_view()),
    path("getServicesRequest", views.getServicesRequest.as_view()),
    path("cancelRequest/<int:req_id>/<int:id>/<str:role>", views.cancelRequest.as_view()),
    path("UpdateVendorServices", views.UpdateVendorServices.as_view()),
    path("updateRequestStatus/<int:req_id>/<int:vendor_id>/<str:request_status>", views.updateRequestStatus.as_view()),

    # Trip related API's Urls
    path("AddCompany", views.AddCompany.as_view()),
    path("AddCompanyModel", views.AddCompanyModel.as_view()),
    path("AddColor", views.AddColors.as_view()),
    path("AddYear", views.AddYear.as_view()),
    path("getTrips/<int:role>/<int:id>", views.getTrips.as_view()),
    path("createTrip", views.createTrip.as_view()),
    path("updateTrip", views.updateTrip.as_view()),
    path("finishTrip/<int:trip_id>/<str:end_time>", views.finishTrip.as_view()),
    path("updateEndTime/<int:id>/<str:end_time>", views.updateEndTime.as_view()),
    path("cancelRequest/<int:req_id>/<int:user_type>", views.cancelRequest.as_view()),
    path("getChats/<int:tripId>", views.getChats.as_view()),
    path("getServices", views.getServices.as_view()),
    path("setTripRoute", views.setTripRoute.as_view()),

    # Vehicle related API's Urls
    path("getVehicleCompanies", views.getVehicleCompanies.as_view()),
    path("getVehicleCompany/<int:id>", views.getVehicleCompany.as_view()),
    path("getVehicleModels/<int:company_id>", views.getVehicleModels.as_view()),
    path("getVehicleModel/<int:id>", views.getVehicleModel.as_view()),
    path("getVehicleColors", views.getVehicleColors.as_view()),
    path("getVehicleColor/<int:id>", views.getVehicleColors.as_view()),
    path("getVehicleYear", views.getVehicleInfoes.as_view()),
    path("getVehicleYear/<int:id>", views.getVehicleInfo.as_view()),
    path("setVehicleInfo", views.setVehicleInfo.as_view()),
    path("addServiceRequest", views.addServiceRequest.as_view()),
    path("updateServiceRequest", views.updateServiceRequest.as_view()),
    path("deleteServiceRequest/<int:id>", views.deleteServiceRequest.as_view()),
    path("getBookingHistory/<str:mobile>", views.getBookingHistory.as_view()),
    path("getBookingSummary/<int:id>", views.getBookingSummary.as_view()),
    path("verifyPhoneNumber", views.verifyPhoneNumber.as_view()),
    path("verifyPhoneNumber/<str:mobile>", views.verifyPhoneNumberGetMethod.as_view()),
    path("verifyOtpCode/<str:mobile>/<int:code>", views.verifyOtpCode.as_view()),
    path("servicePrice/<int:request_id>", views.servicePrice.as_view()),
    path("chargePayment", views.chargePayment.as_view()),
    path("generateCardToken", views.generateCardToken.as_view()),
    path("createCustomer", views.createCustomer.as_view()),
    path("offers", views.getOffer.as_view()),
    path("about", views.getAboutUs.as_view()),
    path("roadhero-help", views.RoadHeroHelp.as_view()),
    path("help", views.getHelpUs.as_view()),
    path("terms", views.getTerms.as_view()),
    path("makePayment", views.makePayment.as_view()),
    path("updateRequest", views.updateRequest.as_view()),
    path("completeRequest", views.updateRequest.as_view()),
    path("requestStatus", views.RequestStatus.as_view()),
    path("bookingText", views.getBookingText.as_view()),
    path("getOptions/<int:service>", views.getQNA.as_view()),

    path("login", views.login_view.as_view()),
    path("register", views.register_view.as_view()),
    path("setDeviceToken/<str:device_token>", views.setDeviceToken.as_view()),
    path("verifyPhone/<str:phone>", views.verifyPhone.as_view()),
    path("verifyCode/<str:phone>/<int:code>", views.verifyCode.as_view()),
    path("vendorServices", views.vendorServices.as_view()),
    path("updateVendorServices", views.updateVendorServices.as_view()),
    path("getAllRequests", views.getAllRequests.as_view()),
    path("getOpenRequests", views.getOpenRequests.as_view()),
    path("waitingRequests", views.getWaitingRequests.as_view()),
    path("cancelRequests", views.getCancelRequests.as_view()),
    path("activeRequests", views.getActiveRequests.as_view()),
    path("completedRequests", views.getCompletedRequests.as_view()),
    path("getServiceHistory", views.getServiceHistory.as_view()),
    path("getServiceRequestById", views.getVendorServiceRequest.as_view()),
    path("AcceptVendorServiceRequest", views.AcceptVendorServiceRequest.as_view()),
    path("RejectVendorServiceRequest", views.RejectVendorServiceRequest.as_view()),
    path("CompleteVendorServiceRequest", views.updateVendorServiceRequest.as_view()),
    path("setVendorStatus", views.setVendorStatus.as_view()),
    path("setVendorLocation/<int:id>/<str:lat>/<str:lng>/<str:address>", views.setVendorLocation.as_view()),
    path("changePassword/<str:oldPassword>/<str:newPassword>", views.update_password.as_view()),
    path("editProfile", views.edit_profile.as_view()),
    path("updatePhoneNumber", views.update_phone.as_view()),
    path("getRequest", views.getRequest.as_view()),
    path("AddPaymentAccount", views.AddPaymentAccount.as_view()),
    path("addSignature", views.AddSignature.as_view()),
    path("updateArrivedTime", views.UpdateArrivedTime.as_view()),
    path("updateTime", views.UpdateTime.as_view()),
    path("updateCompletedTime", views.UpdateCompletedTime.as_view()),
    path("addImages", views.AddImages.as_view()),
    path("addPaymentDetails", views.addPaymentDetails.as_view()),
    path("checkPaymentDetails", views.checkPaymentDetails.as_view()),

]