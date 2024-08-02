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
    path('interaction/post/', views.InteractionPost.as_view() ),

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

    path('bodymassindex/', views.BodyMassIndexList.as_view() ),
    path('bodymassindex/<int:pk>/', views.BodyMassIndexDetail.as_view() ),

    path('glycatedhaemoglobin/', views.GlycatedHemoglobinList.as_view() ),
    path('glycatedhaemoglobin/<int:pk>/', views.GlycatedHemoglobinDetail.as_view() ),

    path('condition/', views.ConditionList.as_view() ),
    path('condition/<int:pk>/', views.ConditionDetail.as_view() ),
    
    path('callmembers/', views.callMembersList.as_view() ),
    path('callmembers/<int:pk>/', views.callMembersDetail.as_view() ),

    path('completeonboarding/', views.CompleteOnboardingList.as_view() ),
    path('completeonboarding/<int:pk>/', views.CompleteOnboardingDetail.as_view() ),

    path('schedulevitalscollection/', views.ScheduleVitalsCollectionList.as_view() ),
    path('schedulevitalscollection/<int:pk>/', views.ScheduleVitalsCollectionDetail.as_view() ),

    path('collectandsubmitvitals/', views.CollectandSubmitVitalsList.as_view() ),
    path('collectandsubmitvitals/<int:pk>/', views.CollectandSubmitVitalsDetail.as_view() ),

    path('initialconsultationdoctor/', views.InitialConsultationDoctorList.as_view() ),
    path('initialconsultationdoctor/<int:pk>/', views.InitialConsultationDoctorDetail.as_view() ),

    path('initialconsultationnutritionist/', views.InitialConsultationNutritionistList.as_view() ),
    path('initialconsultationnutritionist/<int:pk>/', views.InitialConsultationNutritionistDetail.as_view() ),

    path('initialconsultationpsychologist/', views.InitialConsultationPsychologistList.as_view() ),
    path('initialconsultationpsychologist/<int:pk>/', views.InitialConsultationPsychologistDetail.as_view() ),

    path('initialMentalHealthAssessment/', views.InitialMentalHealthScreeningList.as_view() ),
    path('initialMentalHealthAssessment/<int:pk>/', views.InitialMentalHealthScreeningDetail.as_view() ),

    path('generatecareplan/', views.GenerateCarePlanList.as_view() ),
    path('generatecareplan/<int:pk>/', views.GenerateCarePlanDetail.as_view() ),

    path('generatelabrequest/', views.GenerateLabRequestList.as_view() ),
    path('generatelabrequest/<int:pk>/', views.GenerateLabRequestDetail.as_view() ),

    path('generateLabRequest/', views.GenerateLabRequestList.as_view() ),
    path('generateLabRequest/<int:pk>/', views.GenerateLabRequestDetail.as_view() ),

    path('scheduleannuallabtest/', views.ScheduleAnnualLabTestList.as_view() ),
    path('scheduleannuallabtest/<int:pk>/', views.ScheduleAnnualLabTestDetail.as_view() ),

    path('scheduleresultreview/', views.ScheduleResultsReviewList.as_view() ),
    path('scheduleresultreview/<int:pk>/', views.ScheduleResultsReviewDetail.as_view() ),

    path('doctorssecondconsultation/', views.DoctorsSecondConsultationList.as_view() ),
    path('doctorssecondconsultation/<int:pk>/', views.DoctorsSecondConsultationDetail.as_view() ),

    path('task/', views.TaskList.as_view() ),
    path('task/post/', views.TaskListPost.as_view() ),
    path('task/<int:pk>/', views.TaskDetail.as_view() ),
]
urlpatterns = format_suffix_patterns(urlpatterns)