from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.contrib.auth import login as login_view, logout as logout_view, authenticate
from django.contrib.auth.decorators import login_required
from api.models import (
    BookingHistory, Service, serviceRequest, User, PackageDelivery,
    VehicleColor, VehicleInfo, VehicleCompany, VehicleModel, VerificationCode, VenderDetails
    
)
from api.serializers import ServiceSerializer, ServiceRequestSerializer, BookingHistorySerializer, getVendorDetailSerializer

login_error = "Please enter the correct email and password for a staff account. Note that both fields may be case-sensitive."

# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)

        if username and password:
            valid_user = validate_user(username, password)
            if valid_user:
                user = authenticate(username=username, password=password)
                login_view(request, user)
                return render(request, "home.html")
            else:
                return render(request, "login.html", {"error": login_error})
        else:
            return render(request, "login.html", {"error": login_error})
    else:
        return render(request, "login.html")

@login_required()
def logout(request):
    logout_view(request)
    return render(request, "login.html")

def validate_user(username, password):
    try:
        user = User.objects.get(email=username, is_active=True, is_staff=True)
        if user.check_password(password):
            user = user
        else:
            user = None
    except:
        user = None
    return user


@login_required()
def index(request):

    return render(request, 'home.html')

@login_required()
def user_request(request):
    waiting_request = BookingHistory.objects.filter(vendor=None).count()
    active_requests = serviceRequest.objects.filter(service_status=False).count()
    completed_requests = serviceRequest.objects.filter(service_status=True).count()
    data = {
        "waiting_requests": waiting_request,
        "active_requests": active_requests,
        "completed_requests": completed_requests
    }
    return render(request, "request.html", data)

@login_required()
def services(request):
    instances = Service.objects.all()
    serializer = ServiceSerializer(instances, many=True)
    return render(request, "services.html", {"data": serializer.data})

def tos(request):
    return render(request, "tos.html")

@login_required()
def waiting_requests(request):
    page = request.GET.get("pg", 1)
    page = int(page)
    page_limit = 10
    total_count = BookingHistory.objects.filter(vendor=None).count()
    previous_page = (page - 1) * page_limit
    next_page = page * page_limit
    total_pages = (total_count // page_limit) + 1
    if page > total_pages-10:
        last_page = total_pages
    else:
        last_page = page + 10
    if page > 10:
        start_page = page
    else:
        start_page = 1

    if page == 1:
        instance = BookingHistory.objects.filter(vendor=None).order_by('-id')[previous_page:next_page]
    else:
        instance = BookingHistory.objects.all().order_by('-id')[previous_page:next_page]
    return render(request, "waiting_requests.html",
                  {"data": instance, "pages": [x for x in range(start_page, last_page)], "next": page + 1})

@login_required()
def accept(request):
    if request.method == "POST":
        request_id = request.POST.get("request_id")
        eta = request.POST.get("eta")
        vendor = request.POST.get("vendor")
        serialize_data = {
            'request_id': request_id, "vendor_id": vendor, "eta": eta
        }
        serializer = ServiceRequestSerializer(data=serialize_data)
        booking_instance = BookingHistory.objects.get(id=request_id)
        if serializer.is_valid():
            serializer.save()
            booking_instance.vendor = request.user
            booking_instance.save()
            return HttpResponseRedirect('active_requests')
        else:
            return render(request, "accept.html", {"error": "Error occured in accepting the request."})
    else:
        request_id = request.GET.get("id", None)
        instance = BookingHistory.objects.get(id=request_id)
        if instance.service.id == 4:
            instance2 = PackageDelivery.objects.get(request_id=request_id)
        else:
            instance2 = None
        users = User.objects.all()
        return render(request, "accept.html", {"data": instance, "data2": instance2, "users": users})

@login_required()
def reject(request):
    if request.method == "POST":
        request_id = request.POST.get("request_id")
        booking_instance = BookingHistory.objects.get(id=request_id)
        booking_instance.delete()
        return HttpResponseRedirect('waiting_requests')
    else:
        request_id = request.GET.get("id", None)
        instance = BookingHistory.objects.get(id=request_id)
        users = User.objects.all()
        return render(request, "reject.html", {"data": instance, "users": users})

@login_required()
def active_requests(request):
    page = request.GET.get("pg", 1)
    page = int(page)
    page_limit = 10
    total_count = serviceRequest.objects.filter(service_status=False).count()
    previous_page = (page - 1) * page_limit
    next_page = page * page_limit
    total_pages = (total_count // page_limit) + 1
    if page > total_pages-10:
        last_page = total_pages
    else:
        last_page = page + 10
    if page > 10:
        start_page = page
    else:
        start_page = 1

    if page == 1:
        instance = serviceRequest.objects.filter(service_status=False).order_by('-id')[previous_page:next_page]
    else:
        instance = serviceRequest.objects.filter(service_status=False).order_by('-id')[previous_page:next_page]
    return render(request, "active_requests.html",
                  {"data": instance, "pages": [x for x in range(start_page, last_page)], "next": page + 1})

@login_required()
def update_roadhero(request):
    if request.method == "POST":
        request_id = request.POST.get("request_id")
        eta = request.POST.get("eta")
        vendor = request.POST.get("vendor")
        serialize_data = {
            'request_id': request_id, "vendor_id": vendor, "eta": eta
        }
        instance = serviceRequest.objects.get(request_id=request_id)
        serializer = ServiceRequestSerializer(instance, data=serialize_data, partial=True)
        booking_instance = BookingHistory.objects.get(id=request_id)
        if serializer.is_valid():
            serializer.save()
            booking_instance.vendor = request.user
            booking_instance.save()
            return HttpResponseRedirect('active_requests')
        else:
            return render(request, "update_roadhero.html", {"error": "Error occured in accepting the request."})
    else:
        request_id = request.GET.get("id", None)
        instance = serviceRequest.objects.get(request_id=request_id)
        if instance.request_id.service.id == 4:
            instance2 = PackageDelivery.objects.get(request_id=request_id)
        else:
            instance2 = None
        users = User.objects.all()
        return render(request, "update_roadhero.html", {"data": instance, "data2": instance2, "users": users})

@login_required()
def update_time(request):
    if request.method == "POST":
        request_id = request.POST.get("request_id")
        arrived = request.POST.get("arrived")
        completed = request.POST.get("completed")

        if arrived and not completed:
            serialize_data = {
                'request_id': request_id, "arrived": timezone.now().time()
            }
        elif completed:
            serialize_data = {
                'request_id': request_id, "completed": timezone.now().time()
            }
        else:
            serialize_data = None
        instance = serviceRequest.objects.get(request_id=request_id)
        serializer = ServiceRequestSerializer(instance, data=serialize_data, partial=True)
        booking_instance = BookingHistory.objects.get(id=request_id)
        if serializer.is_valid():
            serializer.save()
            booking_instance.vendor = request.user
            booking_instance.save()
            return HttpResponseRedirect('active_requests')
        else:
            request_id = request.GET.get("id", None)
            instance = serviceRequest.objects.get(request_id=request_id)
            if instance.request_id.service.id == 4:
                instance2 = PackageDelivery.objects.get(request_id=request_id)
            else:
                instance2 = None
            users = User.objects.all()
            data = {
                "data": instance, "data2": instance2, "users": users,
                "error": serializer.errors
            }
            return render(request, "update_time.html", data)
    else:
        request_id = request.GET.get("id", None)
        instance = serviceRequest.objects.get(request_id=request_id)
        if instance.request_id.service.id == 4:
            instance2 = PackageDelivery.objects.get(request_id=request_id)
        else:
            instance2 = None
        users = User.objects.all()
        return render(request, "update_time.html", {"data": instance, "data2": instance2, "users": users})

@login_required()
def completed_requests(request):
    page = request.GET.get("pg", 1)
    page = int(page)
    page_limit = 10
    total_count = serviceRequest.objects.filter(service_status=True).count()
    previous_page = (page - 1) * page_limit
    next_page = page * page_limit
    total_pages = (total_count // page_limit) + 1
    if page > total_pages-10:
        last_page = total_pages
    else:
        last_page = page + 10
    if page > 10:
        start_page = page
    else:
        start_page = 1

    if page == 1:
        instance = serviceRequest.objects.filter(service_status=True).order_by('-id')[previous_page:next_page]
    else:
        instance = serviceRequest.objects.filter(service_status=True).order_by('-id')[previous_page:next_page]
    return render(request, "completed_requests.html",
                  {"data": instance, "pages": [x for x in range(start_page, last_page)], "next": page + 1})

@login_required()
def AllRequests(request):
    page = request.GET.get("pg", 1)
    page = int(page)
    page_limit = 10
    total_count = BookingHistory.objects.all().count()
    previous_page = (page - 1) * page_limit
    next_page = page * page_limit
    total_pages = (total_count//page_limit) + 1
    if page > total_pages-10:
        last_page = total_pages
    else:
        last_page = page + 10
    if page > 10:
        start_page = page
    else:
        start_page = 1

    if page == 1:
        instance = BookingHistory.objects.all().order_by('-id')[previous_page:next_page]
    else:
        instance = BookingHistory.objects.all().order_by('-id')[previous_page:next_page]
    return render(request, "requests.html", {"data": instance, "pages": [x for x in range(start_page, last_page)], "next": page+1})

@login_required()
def update_request(request):
    if request.method == "POST":
        request_id = request.POST.get("request_id", None)
        vendor = request.POST.get("vendor", None)
        vendor = request.POST.get("vendor", None)
        vendor = request.POST.get("vendor", None)
        vendor = request.POST.get("vendor", None)
        vendor = request.POST.get("vendor", None)
        vendor = request.POST.get("vendor", None)
        vendor = request.POST.get("vendor", None)
        vendor = request.POST.get("vendor", None)
        vendor = request.POST.get("vendor", None)
        vendor = request.POST.get("vendor", None)
        vendor = request.POST.get("vendor", None)
        print(request.POST)
    request_id = request.GET.get("id", None)
    vendor = request.GET.get("vendor", None)
    if request_id and vendor and vendor != "None":
        instance = serviceRequest.objects.get(request_id=request_id)
        data = {
            "data": instance.request_id,
            "data1": instance,
            "users": User.objects.all()
        }
    else:
        instance = BookingHistory.objects.get(id=request_id)
        data = {
            "data": instance,
            "users": User.objects.all()
        }

    return render(request, 'update_request.html', data)

@login_required()
def view_request_details(request):
    request_id = request.GET.get("id")
    instance = serviceRequest.objects.get(request_id=request_id)
    images = []
    check_base64 = "data:image/jpeg;base64,"
    if check_base64 in instance.image1:
        images.append({
            "src": instance.image1,
            "name": "image1"
        })
    elif check_base64 not in instance.image1 and instance.image1:
        images.append({
            "src": check_base64 + str(instance.image1),
            "name": "image1"
        })
    else:
        pass
    if check_base64 in instance.image2:
        images.append({
            "src": instance.image2,
            "name": "image1"
        })
    elif check_base64 not in instance.image2 and instance.image2:
        images.append({
            "src": check_base64 + str(instance.image2),
            "name": "image2"
        })
    else:
        pass
    if check_base64 in instance.image3:
        images.append({
            "src": instance.image3,
            "name": "image3"
        })
    elif check_base64 not in instance.image3 and instance.image3:
        images.append({
            "src": check_base64 + str(instance.image3),
            "name": "image3"
        })
    else:
        pass
    if check_base64 in instance.image4:
        images.append({
            "src": instance.image4,
            "name": "image4"
        })
    elif check_base64 not in instance.image4 and instance.image4:
        images.append({
            "src": check_base64 + str(instance.image4),
            "name": "image4"
        })
    else:
        pass
    return render(request, 'view.html', {"data": instance, "images": images})

@login_required()
def vehicle(request):
    make = VehicleCompany.objects.all().count()
    models = VehicleModel.objects.all().count()
    colors = VehicleColor.objects.all().count()
    years = VehicleInfo.objects.all().count()
    data = {
        "make": make, "models": models,
        "colors": colors, "years": years
    }
    return render(request, "vehicle.html", data)

@login_required()
def view_vehicle_make(request):
    if request.method == "POST":
        make = request.POST["make"]
        VehicleCompany(name=make)
        return HttpResponseRedirect('view_vehicle_make')
    else:
        make = pagination(request, VehicleCompany)
        return render(request, "vehicle_make.html", make)

@login_required()
def view_vehicle_models(request):
    if request.method == "POST":
        make = request.POST["make"]
        model = request.POST["model"]
        VehicleModel(name=model, vehicle_company=make)
        return HttpResponseRedirect('view_vehicle_models')
    else:
        page = request.GET.get("pg", 1)
        id = request.GET.get("id", 1)
        page = int(page)
        page_limit = 10
        total_count = VehicleModel.objects.filter(vehicle_company=id).count()
        previous_page = (page - 1) * page_limit
        next_page = page * page_limit
        total_pages = (total_count // page_limit) + 1
        if page > total_pages - 10:
            last_page = total_pages
        elif page == total_pages:
            last_page = total_pages
        else:
            last_page = page + 10
        if page > 10:
            start_page = page
        else:
            start_page = 1

        if page == 1:
            instance = VehicleModel.objects.filter(vehicle_company=id).order_by('id')[previous_page:next_page]
        else:
            instance = VehicleModel.objects.filter(vehicle_company=id).order_by('id')[previous_page:next_page]
        data = {
            "data": instance, "pages": [x for x in range(start_page, last_page)],
            "next": page + 1
        }
        # make = pagination(request, VehicleModel)
        return render(request, "vehicle_model.html", data)

@login_required()
def view_vehicle_colors(request):
    if request.method == "POST":
        color = request.POST["color"]
        VehicleColor(name=color)
        return HttpResponseRedirect('view_vehicle_colors')
    else:
        make = pagination(request, VehicleColor)
        return render(request, "vehicle_color.html", make)

@login_required()
def view_vehicle_years(request):
    if request.method == "POST":
        year = request.POST["year"]
        VehicleInfo(year=year)
        return HttpResponseRedirect('view_vehicle_years')
    else:
        make = pagination(request, VehicleInfo)
        return render(request, "vehicle_year.html", make)

@login_required()
def view_roadhero(request):
    users = pagination(request, User)
    return render(request, "roadheroes.html", users)

@login_required()
def edit_roadhero(request):
    if request.method == "POST":
        id = request.POST.get("id")
        edit_type = request.POST.get("type")
        if edit_type == "edit":
            first_name = request.POST["first_name"]
            last_name = request.POST["last_name"]
            phone = request.POST["phone"]
            email = request.POST["email"]
            password = request.POST["password"]
            instance = User.objects.get(id=id)
            instance.first_name = first_name
            instance.last_name = last_name
            instance.phone = phone
            instance.email = email
            if str(password).strip():
                instance.set_password(password)
            else:
                pass
            instance.save()
            return render(request, "edit_roadhero.html", {"data": instance, "type": 1})
        elif edit_type == "delete":
            instance = User.objects.get(id=id)
            instance.delete()
            return HttpResponseRedirect('view_roadhero')
    else:
        id = request.GET.get("id")
        edit_type = request.GET.get("type")
        instance = User.objects.get(id=id)
        if edit_type == "edit":
            return render(request, "edit_roadhero.html", {"data": instance, "type": 1})
        elif edit_type == "delete":
            instance.delete()
            return HttpResponseRedirect('view_roadhero')
        elif edit_type == "verify":
            instance.doc_verify = True
            instance.save()
            return HttpResponseRedirect('view_roadhero')

@login_required()
def view_motorist(request):
    users = pagination(request, VerificationCode)
    return render(request, "motorists.html", users)

@login_required()
def edit_motorist(request):
    if request.method == "POST":
        id = request.POST.get("id")
        edit_type = request.POST.get("type")
        if edit_type == "edit":
            name = request.POST["name"]
            email = request.POST["email"]
            mobile = request.POST["mobile"]
            code = request.POST["otp"]
            instance = VerificationCode.objects.get(id=id)
            instance.name = name
            instance.mobile = mobile
            instance.code = code
            instance.email = email
            instance.save()
            return render(request, "edit_motorist.html", {"data": instance, "type": 1})
        elif edit_type == "delete":
            instance = VerificationCode.objects.get(id=id)
            instance.delete()
            return HttpResponseRedirect('view_motorist')
    else:
        id = request.GET.get("id")
        edit_type = request.GET.get("type")
        instance = VerificationCode.objects.get(id=id)
        if edit_type == "edit":
            return render(request, "edit_motorist.html", {"data": instance, "type": 1})
        elif edit_type == "delete":
            return render(request, "edit_motorist.html", {"data": instance, "type": 2})

def pagination(request, model):
    page = request.GET.get("pg", 1)
    page = int(page)
    page_limit = 10
    total_count = model.objects.all().count()
    previous_page = (page - 1) * page_limit
    next_page = page * page_limit
    total_pages = (total_count // page_limit) + 1
    if page > total_pages-10:
        last_page = total_pages
    elif page == total_pages:
        last_page = total_pages
    else:
        last_page = page + 10
    if page > 10:
        start_page = page
    else:
        start_page = 1

    if page == 1:
        instance = model.objects.all().order_by('id')[previous_page:next_page]
    else:
        instance = model.objects.all().order_by('id')[previous_page:next_page]
    data = {
        "data": instance, "pages": [x for x in range(start_page, last_page)],
        "next": page+1, "start_page": start_page, "last_page": last_page
    }
    return data

def terms_conditions(request):
    return render(request, "terms.html")

def AddDocument(request):
    if request.method == "POST":
        w9_form = request.FILES["w9_form"]
        driver_licence_back = request.FILES["driver_licence_back"]
        driver_licence_front = request.FILES["driver_licence_front"]
        reg_insurence = request.FILES["reg_insurence"]
        background_check = request.FILES["background_check"]
        authorization_form = request.FILES["authorization_form"]
        return render(request, "document.html", {"success": "OK"})

    return render(request, "document.html")

def view_roadhero_documents(request):
    page = request.GET.get("pg", 1)
    page = int(page)
    page_limit = 10
    total_count = VenderDetails.objects.all().count()
    previous_page = (page - 1) * page_limit
    next_page = page * page_limit
    total_pages = (total_count // page_limit) + 1
    if page > total_pages - 10:
        last_page = total_pages
    elif page == total_pages:
        last_page = total_pages
    else:
        last_page = page + 10
    if page > 10:
        start_page = page
    else:
        start_page = 1

    if page == 1:
        instance = VenderDetails.objects.all().order_by('id')[previous_page:next_page]
    else:
        instance = VenderDetails.objects.all().order_by('id')[previous_page:next_page]
    serializer = getVendorDetailSerializer(instance, many=True)
    serialize_data = serializer.data
    print([x for x in range(start_page, last_page)], last_page, start_page)
    data = {
        "data": serialize_data, "pages": [x for x in range(start_page, last_page)],
        "next": page + 1, "start_page": start_page, "last_page": last_page
    }
    return render(request, "roadhero_documents.html", data)