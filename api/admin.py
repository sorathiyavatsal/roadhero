from django.contrib import admin
from api.models import (
    Role, User, Service, Trip, VehicleColor, VehicleCompany,
    VehicleModel, VerificationCode, VenderLocation, VehicleInfo, Review, serviceRequest,
    chatModel, BookingHistory, Offer, AppDetail, QNaModel, QnaOptionModel, PaymentAccount,
    PackageDelivery, VenderDetails, FAQ
)
class UserdAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "email", "role", "phone")

class ServicedAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image', 'detail', 'price')

class TripdAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'vendor', 'service', 'source_lat_lng',
            'source_address', 'destination_lat_lng', 'destination_address',
            'start_time', 'end_time', 'trip_path', 'map_image')

class VehicleColordAdmin(admin.ModelAdmin):
    list_display = ('id', 'color', 'name')

class VehicleCompanydAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'icon')

class VehicleModeldAdmin(admin.ModelAdmin):
    list_display = ('id', 'vehicle_company', 'name')


class VehicleInfoCompanydAdmin(admin.ModelAdmin):
    list_display = ('id', "year")


class VenderLocationdAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'latitude', 'longitude', 'address')

class BookingHistoryAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'vehicle', 'vehicle_color', 'vehicle_year', 'vendor', 'name',
        'service', 'rating', 'mobile', 'payment_status', 'price',
    )

class OfferdAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'promo_code', 'discount', 'detail')

class QNAdAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'service')

class QnaOptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'option', 'qna')

class PaymentAccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'account_name', 'account_number', 'routing_number',
                    'personal_id', 'address', 'zip_code')

class serviceRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'request_id',  "vendor_id", "request_status", "service_status", "rating", "review")

# Register your models here.
admin.site.register(Role)
admin.site.register(User, UserdAdmin)
admin.site.register(Service, ServicedAdmin)
admin.site.register(Trip, TripdAdmin)
admin.site.register(VehicleColor, VehicleColordAdmin)
admin.site.register(VehicleCompany, VehicleCompanydAdmin)
admin.site.register(VehicleModel, VehicleModeldAdmin)
admin.site.register(VerificationCode)
admin.site.register(VenderLocation, VenderLocationdAdmin)
admin.site.register(VehicleInfo, VehicleInfoCompanydAdmin)
admin.site.register(Review)
admin.site.register(serviceRequest, serviceRequestAdmin)
admin.site.register(chatModel)
admin.site.register(BookingHistory, BookingHistoryAdmin)
admin.site.register(Offer, OfferdAdmin)
admin.site.register(AppDetail)
admin.site.register(QNaModel, QNAdAdmin)
admin.site.register(QnaOptionModel, QnaOptionAdmin)
admin.site.register(PaymentAccount, PaymentAccountAdmin)
admin.site.register(PackageDelivery)
admin.site.register(VenderDetails)
admin.site.register(FAQ)