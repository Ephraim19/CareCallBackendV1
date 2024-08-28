from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from . import consumers

urlpatterns = [
    path('search/', views.SearchMember.as_view()),
    
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
    path('interaction/analytics/', views.InteractionAnalytics.as_view() ),

    path('bloodpressure/', views.BloodPressureList.as_view() ),
    path('bloodpressure/<int:pk>/', views.BloodPressureDetail.as_view() ),
    path('bloodpressure/post/', views.BloodPressurePost.as_view() ),

    path('temperature/', views.TemperatureList.as_view() ),
    path('temperature/<int:pk>/', views.TemperatureDetail.as_view() ),
    path('temperature/post/', views.TemperaturePost.as_view() ),

    path('oxygen/', views.OxygenList.as_view() ),
    path('oxygen/<int:pk>/', views.OxygenDetail.as_view()),
    path('oxygen/post/', views.OxygenPost.as_view() ),

    path('pulse/', views.PulseList.as_view() ),
    path('pulse/<int:pk>/', views.PulseDetail.as_view() ),
    path('pulse/post/', views.PulsePost.as_view() ),

    path('respiratory/', views.RespiratoryRateList.as_view() ),
    path('respiratory/<int:pk>/', views.RespiratoryRateDetail.as_view() ),
    path('respiratory/post/', views.RespiratoryRatePost.as_view()),

    path('randombloodsugar/', views.RandomBloodSugarList.as_view() ),
    path('randombloodsugar/<int:pk>/', views.RandomBloodSugarDetail.as_view() ),
    path('randombloodsugar/post/', views.RandomBloodSugarPost.as_view() ),

    path ('fastingbloodsugar/', views.FastingBloodSugarList.as_view() ),
    path ('fastingbloodsugar/<int:pk>/', views.FastingBloodSugarDetail.as_view() ),
   path('fastingbloodsugar/post/', views.FastingBloodSugarPost.as_view() ),

    path('bodymassindex/', views.BodyMassIndexList.as_view() ),
    path('bodymassindex/<int:pk>/', views.BodyMassIndexDetail.as_view() ),
    path('bodymassindex/post/', views.BodyMassIndexPost.as_view() ),

    path('glycatedhaemoglobin/', views.GlycatedHemoglobinList.as_view() ),
    path('glycatedhaemoglobin/<int:pk>/', views.GlycatedHemoglobinDetail.as_view() ),
    path('glycatedhaemoglobin/post/', views.GlycatedHemoglobinPost.as_view() ),

    path('condition/', views.ConditionList.as_view() ),
    path('condition/<int:pk>/', views.ConditionDetail.as_view() ),

    path('journey/', views.MemberJourneyList.as_view() ),
    path('journey/<int:pk>/', views.MemberJourneyDetail.as_view() ),

    path('task/', views.TaskList.as_view() ),
    path('task/post/', views.TaskListPost.as_view() ),
    path('task/<int:pk>/', views.TaskDetail.as_view() ),
    path('mytasks/', views.MyTasks.as_view() ),

    path('appointment/', views.AppointmentsList.as_view() ),
    path('appointment/post/', views. AppointmentsPost.as_view() ),
    path('appointment/<int:pk>/', views.AppointmentsDetail.as_view() ),

    path('new/', views.NewMemberAdd.as_view() ),

    #Analytics
    path('tasks/analytics/', views.TasksAnalytics),
    path('member/analytics/', views.MemberAnalytics),
    path('member/analytics/fbs/', views.MemberAnalyticsFbs),
    path('member/analytics/hba1c/', views.MemberAnalyticsHba1c),

    path('member/analytics/rbs/', views.MemberAnalyticsRbs),
    path('appointment/analytics/', views.AppointmentAnalytics),

    path('send-whatsapp/', views.send_whatsapp_message.as_view(), name='send_whatsapp'),
    path('whatsapp/', views.getWhatsapp.as_view(), name='get_whatsapp'),
    path('webhook/', views.Whatsapp_Webhook.as_view() , name='whatsapp_webhook'),
    
    path("hr/",views.HR.as_view()),
    # path('chats/', consumers.YourConsumer.as_asgi()),

]
urlpatterns = format_suffix_patterns(urlpatterns)