from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('members/', views.MemberList.as_view()),
    path('members/<int:pk>/', views.MemberDetail.as_view()),
    
    path('dependants/', views.DependantList.as_view()),
    path('dependants/<int:pk>/', views.DependantDetail.as_view()),
    
    path('surgery/', views.SurgeryList.as_view()),
    path('surgery/<int:pk>/', views.SurgeryDetail.as_view()),
    
    path('overview/', views.OverviewList.as_view()),
    path('overview/<int:pk>/', views.OverviewDetail.as_view()),
    
    path('allergy/', views.AllergyList.as_view()),
    path('allergy/<int:pk>/', views.AllergyDetail.as_view()),
    
    path('notes/', views.NoteList.as_view() ),
    path('notes/<int:pk>/', views.NoteDetail.as_view() ),
    
    path('admission/', views.AdmissionList.as_view() ),
    path('admission/<int:pk>/', views.AdmissionDetail.as_view() ),
    
    path('family/', views.FamilyList.as_view() ),
    path('family/<int:pk>/', views.FamilyDetail.as_view() ),
    
    path('social/', views.SocialList.as_view() ),
    path('social/<int:pk>/', views.SocialDetail.as_view() ),

    path('interaction/', views.InteractionList.as_view() ),
    path('interaction/<int:pk>/', views.InteractionDetail.as_view() ),

    path('bloodpressure/', views.BloodPressureList.as_view() ),
    path('bloodpressure/<int:pk>/', views.BloodPressureDetail.as_view() ),

    path('temperature/', views.TemperatureList.as_view() ),
    path('temperature/<int:pk>/', views.TemperatureDetail.as_view() ),

    path('oxygensaturation/', views.OxygenList.as_view() ),
    path('oxygensaturation/<int:pk>/', views.OxygenDetail.as_view() ),

    path('pulse/', views.PulseList.as_view() ),
    path('pulse/<int:pk>/', views.PulseDetail.as_view() ),

    path('respiratoryrate/', views.RespiratoryRateList.as_view() ),
    path('respiratoryrate/<int:pk>/', views.RespiratoryRateDetail.as_view() ),

    path('randombloodsugar/', views.RandomBloodSugarList.as_view() ),
    path('randombloodsugar/<int:pk>/', views.RandomBloodSugarDetail.as_view() ),

    path ('fastingbloodsugar/', views.FastingBloodSugarList.as_view() ),
    path ('fastingbloodsugar/<int:pk>/', views.FastingBloodSugarDetail.as_view() ),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)