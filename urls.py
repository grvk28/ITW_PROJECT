from django.conf.urls import url
from hsp import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/',views.index, name='about'),
url(r'^about1/',views.about1, name='about1'),
url(r'^about2/',views.about2, name='about2'),
url(r'^about3/',views.about3, name='about3'),
url(r'^about4/',views.about4, name='about4'),
url(r'^about5/',views.about5, name='about5'),
url(r'^about6/',views.about6, name='about6'),
url(r'^about7/',views.about7, name='about7'),
url(r'^search/',views.search, name='search'),
url(r'^Injury Type.Amputation/',views.InjuryTypeAmputation, name='Injury Type.Amputation'),
url(r'^Injury Type.Arm/',views.InjuryTypeArm, name='Injury Type.Arm'),
url(r'^Injury Type.Asbestos/',views.InjuryTypeAsbestos, name='Injury Type.Asbestos'),
url(r'^Injury Type.Back/',views.InjuryTypeBack, name='Injury Type.Back'),
url(r'^Injury Type.Broken/',views.InjuryTypeBroken, name='Injury Type.Broken'),
url(r'^Injury Type.Burn/',views.InjuryTypeBurn, name='Injury Type.Burn'),
url(r'^Injury Type.Carpel/',views.InjuryTypeCarpel, name='Injury Type.Carpel'),
url(r'^Injury Type.Chemical/',views.InjuryTypeChemical, name='Injury Type.Chemical'),
url(r'^Injury Type.Eye/',views.InjuryTypeEye, name='Injury Type.Eye'),
url(r'^Injury Type.Fatal/',views.InjuryTypeFatalaccident, name='Injury Type.Fatal'),
url(r'^Injury Type.Groin/',views.InjuryTypeGroin, name='Injury Type.Groin'),
url(r'^Injury Type.Hand/',views.InjuryTypeHand, name='Injury Type.Hand'),
url(r'^Injury Type.Head/',views.InjuryTypeHead, name='Injury Type.Head'),
url(r'^Injury Type.Head and/',views.InjuryTypeHeadand, name='Injury Type.Head and'),
url(r'^Injury Type.Hearing/',views.InjuryTypeHearing, name='Injury Type.Hearing'),
url(r'^Injury Type.Hip/',views.InjuryTypeHip, name='Injury Type.Hip'),
url(r'^Injury Type.Knee/',views.InjuryTypeKnee, name='Injury Type.Knee'),
url(r'^Injury Type.Leg/',views.InjuryTypeLeg, name='Injury Type.Leg'),
url(r'^Injury Type.Neck/',views.InjuryTypeNeck, name='Injury Type.Neck'),
url(r'^Injury Type.Serious/',views.InjuryTypeSerious, name='Injury Type.Serious'),
url(r'^Injury Type.Whiplash/',views.InjuryTypeWhiplash, name='Injury Type.Whiplash'),
url(r'^Injury Type.Repetitive/',views.InjuryTypeRepetitive, name='Injury Type.Repetitive'),
url(r'^Accident Type.Bicycle/',views.AccidentTypeBicycle, name='Accident Type.Bicycle'),
url(r'^Accident Type.Car/',views.AccidentTypeCar, name='Accident Type.Car'),
url(r'^Accident Type.carbon/',views.AccidentTypecarbon, name='Accident Type.carbon'),
url(r'^Accident Type.carer/',views.AccidentTypecarer, name='Accident Type.carer'),
url(r'^Accident Type.Defective/',views.AccidentTypeDefective, name='Accident Type.Defective'),
url(r'^Accident Type.Dog/',views.AccidentTypeDog, name='Accident Type.Dog'),
url(r'^Accident Type.Factory/',views.AccidentTypeFactory, name='Accident Type.Factory'),
url(r'^Accident Type.Farm/',views.AccidentTypeFarm, name='Accident Type.Farm'),
url(r'^Accident Type.Fatal/',views.AccidentTypeFatal, name='Accident Type.Fatal'),
url(r'^Accident Type.Holiday/',views.AccidentTypeHoliday, name='Accident Type.Holiday'),
url(r'^Accident Type.Industrial/',views.AccidentTypeIndustrial, name='Accident Type.Industrial'),
url(r'^Accident Type.Machinery/',views.AccidentTypeMachinery, name='Accident Type.Machinery'),
url(r'^Accident Type.Military/',views.AccidentTypeMilitary, name='Accident Type.Military'),
url(r'^Accident Type.Motorcycle/',views.AccidentTypeMotorcycle, name='Accident Type.Motorcycle'),
url(r'^Accident Type.Needlestick/',views.AccidentTypeNeedlestick, name='Accident Type.NeedleStick'),
url(r'^Accident Type.Office/',views.AccidentTypeOffice, name='Accident Type.Office'),
url(r'^Accident Type.Passenger/',views.AccidentTypePassenger, name='Accident Type.Passenger'),
url(r'^Accident Type.Pavement/',views.AccidentTypePavement, name='Accident Type.Pavement'),
url(r'^Accident Type.Public/',views.AccidentTypePublic, name='Accident Type.Public'),
url(r'^Accident Type.sport/',views.AccidentTypesport, name='Accident Type.sport'),
url(r'^Accident Type.Supermarket/',views.AccidentTypeSupermarket, name='Accident Type.Supermarket'),
url(r'^newsfeed/',views.newsfeed, name='newsfeed'),
url(r'new/',views.new_view),

]