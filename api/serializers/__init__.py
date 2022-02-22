from .RoleSerializers import RoleSerializer
from .UserSerializer import *
from .ServiceSerializers import *
from .TripSerializers import *
from .VehicleCompanySerializers import *
from .VehicleModelSerializers import *
from .VehicleColorSerializers import *
from .VehicleInfoSerializers import *
from .VerificationCodeserializers import *
from .VendorLocationSerializers import *
from .ReviewSerializers import *
from .service_request_serializers import ServiceRequestSerializer, getServiceRequestSerializer
from .chatSerializers import *
from .bookingSerializers import BookingHistorySerializer, getBookingHistorySerializer, PackageDeliverySerializer
from .offerSerializers import OfferSerializer
from .qnaSerializers import getQNASerializer
from .paymentSerializers import PaymentAccountSerializer
from .faq_serializers import FAQSerializer