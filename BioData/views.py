from .models import Member,Task,Dependant,memberTaskBase,Appointments,Condition,Whatsapp,Overview,Allergy,HumanResource,Surgery,Othernote,BodyMassIndex,RespiratoryRate,GlycatedHaemoglobin,FastingBloodSugar,RandomBloodSugar,Admission,Family,Social,PulseRate,InteractionLog,BloodPressure,Temperature,Oxygen
from .serializers import MemberSerializer,NewMemberSerializer,WhatsappSerializer,AppointmentsSerializer,TaskSerializer,HrSerializer,MemberJourneySerializer,DependantSerializer,OverviewSerializer,ConditionSerializer,BodyMassIndexSerializer,GlycateHaemoglobinSerializer,RespiratorySerializer,FastingBloodSugarSerializer,RandomBloodSugarSerializer,AllergySerializer,PulseSerializer,OxygenSerializer,TemperatureSerializer,BloodPressureSerializer,SurgerySerializer,OthernoteSerializer,AdmissionSerializer,FamilySerializer,SocialSerializer,InteractionSerializer
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from datetime import datetime, timedelta
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .MyFunctions import MemberMoM
import calendar
from django.http import JsonResponse,HttpResponse
from django.db.models import Count
import requests
from django.views.decorators.csrf import csrf_exempt
import json

access_token = 'EAAEqkG7cBtQBO7ZCb1ZCBoIJpp0uNdccKQY04z4JQhA41QEkvbwStRV0pYAj55aASiZBC9kPJXQpRgZC6ZAAfCNC3Pnid3dvxqHSVgzNY2xrzw707cfz1u0FUIPuOJzhDv8mIOSJHx1UM8PYfLbHbINAdWAjBF1SuCrelytb5CLM7oOgsyvQONfseQZBwjZC0nVIgp3kVIbvHpS6rmomvkZD'

class SearchMember(APIView):

    def post(self, request, *args, **kwargs):
        search_term = request.data.get('name', None)
        print(search_term)
        if search_term is not None:
            members = Member.objects.filter(memberName__icontains=search_term)
            serializer = MemberSerializer(members, many=True)
            return Response(serializer.data)
        else:
            return Response({'error': 'No search term provided'}, status=status.HTTP_400_BAD_REQUEST)


class MemberList(generics.ListCreateAPIView):
    
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    
    
class MemberDetail(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class NewMemberAdd(generics.CreateAPIView):
    serializer_class = NewMemberSerializer

    def perform_create(self, serializer):
        #Assigne care Manager and engagement officer
        HR = HumanResource.objects.filter(HRRole = "Care Manager", HRStatus = "Active")
        HR1 = HumanResource.objects.filter(HRRole = "Engagement Lead", HRStatus = "Active")

     #Set the Doctor, nutritionist or Psychologist assignee to task and add task to HR
        hr_with_lowest_tasks = HR.order_by('HRTasks').first()
        hr_with_lowest_tasks.HRTasks += 1
        hr_with_lowest_tasks.save()         

        hr_with_lowest_tasks1 = HR1.order_by('HRTasks').first()
        hr_with_lowest_tasks1.HRTasks += 1
        hr_with_lowest_tasks1.save()  
        
        serializer.save(memberCareManager = hr_with_lowest_tasks.HREmail, memberEngagementLead = hr_with_lowest_tasks1.HREmail)


class DependantList(generics.ListCreateAPIView):
    
    queryset = Dependant.objects.all()
    serializer_class = DependantSerializer
    
    
class DependantDetail(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Dependant.objects.all()
    serializer_class = DependantSerializer
    

class OverviewList(generics.ListCreateAPIView):
    
    queryset = Overview.objects.all()
    serializer_class = OverviewSerializer
    
    
    
class OverviewDetail(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Overview.objects.all()
    serializer_class = OverviewSerializer
    


class AllergyList(generics.ListCreateAPIView):
    
    queryset = Allergy.objects.all()
    serializer_class = AllergySerializer
    
    
class AllergyDetail(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Allergy.objects.all()
    serializer_class = AllergySerializer
    
    
class SurgeryList(generics.ListCreateAPIView):
    queryset = Surgery.objects.all()
    serializer_class = SurgerySerializer
    
class SurgeryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Surgery.objects.all()
    serializer_class = SurgerySerializer


class NoteList(generics.ListCreateAPIView):
    queryset = Othernote.objects.all()
    serializer_class = OthernoteSerializer
    
class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Othernote.objects.all()
    serializer_class = OthernoteSerializer
    
class AdmissionList(generics.ListCreateAPIView):
    queryset = Admission.objects.all()
    serializer_class = AdmissionSerializer
    
class AdmissionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Admission.objects.all()
    serializer_class = AdmissionSerializer
    
class FamilyList(generics.ListCreateAPIView):
    queryset = Family.objects.all()
    serializer_class = FamilySerializer
    
class FamilyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Family.objects.all()
    serializer_class = FamilySerializer
    
class SocialList(generics.ListCreateAPIView):
    queryset = Social.objects.all()
    serializer_class = SocialSerializer
    
class SocialDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Social.objects.all()
    serializer_class = SocialSerializer


#INTERACTION LOG
class InteractionPost (generics.CreateAPIView):
    queryset = InteractionLog.objects.all()
    serializer_class = InteractionSerializer

class InteractionList(generics.ListAPIView): 
    serializer_class = InteractionSerializer

    def get_queryset(self):
        """
        This view returns a list of all the interaction logs
        for the memberId passed in the request.
        """
        member_id = self.request.query_params.get('memberId', None)
        if member_id is not None:
            return InteractionLog.objects.filter(memberId=member_id)
        else:
            return InteractionLog.objects.none()
    
class InteractionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = InteractionLog.objects.all()
    serializer_class = InteractionSerializer

#INTERACTION ANALYTICS
class InteractionAnalytics(APIView):
    serialiazer_class = InteractionSerializer

    def get(self, request, *args, **kwargs):
        interactions = {}
        allInteractions = InteractionLog.objects.all()

        total = []
        total = allInteractions.count()
        interactions['total'] = total

        SMS = []
        SMS = allInteractions.filter(channel = "SMS").count()
        interactions['SMS'] = SMS

        Phone = []
        Phone = allInteractions.filter(channel = "Phone call").count()
        interactions['Phone'] = Phone

        Email = []
        Email = allInteractions.filter(channel = "Email").count()
        interactions['Email'] = Email

        WhatsApp = []
        WhatsApp = allInteractions.filter(channel = "WhatsApp").count()
        interactions['WhatsApp'] = WhatsApp

        Outbound = []
        Outbound = allInteractions.filter(channelDirection = "Outbound").count()
        interactions['Outbound'] = Outbound

        Inbound = []
        Inbound = allInteractions.filter(channelDirection = "Inbound").count()
        interactions['Inbound'] = Inbound
        return Response([interactions])
        

#BLOOD PRESSURE
class BloodPressureList(generics.ListAPIView):
    serializer_class = BloodPressureSerializer

    def get_queryset(self):

        member_id = self.request.query_params.get('memberId', None)
        if member_id is not None:
            return BloodPressure.objects.filter(memberId=member_id)
        else:
            return BloodPressure.objects.all() 
    

    
class BloodPressurePost(generics.CreateAPIView):
    serializer_class =  BloodPressureSerializer

    def perform_create(self,serializer):
        clinical_info = [130,80,120,60]
        member_id = self.request.data.get('memberId',None)
        systolic = self.request.data.get('systolic',None)
        diastolic = self.request.data.get('diastolic',None)
        readingDate = self.request.data.get('readingDate',None)
        updatedBy = self.request.data.get('updatedBy',None)

        #get member instace
        member = Member.objects.get(id=member_id)
        now = datetime.now().date() + timedelta(days=1)
        date_string = now.strftime("%a %b %d %Y")

     #+1
        HR = HumanResource.objects.filter(HREmail = member.memberCareManager)
        hr_member = HR.first()
        hr_member.HRTasks += 1
        hr_member.save()  
        
        if int(systolic) > clinical_info[0] or  int(diastolic) > clinical_info[2]:

            Task.objects.create(
                memberId= member,
                taskDueDate=date_string,
                taskStatus='Not started',
                taskAssignedTo=member.memberCareManager  ,
                task = str(member) + ' ' + 'Follow up for hypertension for member blood pressure reading on' + ' ' + readingDate ,
                taskName = "Hypertension Follow up"
            )
            interpretation = 'Hypertension'
        else:
            interpretation = 'Normal'            
        
        if int(systolic) < clinical_info[1] or  int(diastolic) < clinical_info[3]:

            Task.objects.create(
                memberId=member,
                taskDueDate=date_string,
                taskStatus='Not started',
                taskAssignedTo=member.memberCareManager  ,
                task = str(member) +' '+ 'Follow up for hypotension for member blood pressure reading on' +" " + readingDate, 
                taskName = "Hypertension Follow up"
            )

        serializer.save(interpretation = interpretation)



class BloodPressureDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BloodPressure.objects.all()
    serializer_class = BloodPressureSerializer


#TEMPERATURE
class TemperatureList(generics.ListAPIView):
    serializer_class = TemperatureSerializer

    def get_queryset(self):

        member_id = self.request.query_params.get('memberId', None)
        if member_id is not None:
            return Temperature.objects.filter(memberId=member_id)
        else:
            return Temperature.objects.none() 
        
class TemperaturePost(generics.CreateAPIView):
    serializer_class =  TemperatureSerializer

    def perform_create(self,serializer):
        clinical_info = [130,80,120,60]
        member_id = self.request.data.get('memberId',None)
        temperature = self.request.data.get('temperature',None)
        readingDate = self.request.data.get('readingDate',None)
        updatedBy = self.request.data.get('updatedBy',None)

        #get member instace
        member = Member.objects.get(id=member_id)
        now = datetime.now().date() + timedelta(days=1)
        date_string = now.strftime("%a %b %d %Y")

             #+1
        HR = HumanResource.objects.filter(HREmail = member.memberCareManager)
        hr_member = HR.first()
        hr_member.HRTasks += 1
        hr_member.save()  

        #Save the task
        if float(temperature) >= 38.0 and float(temperature) < 41.5:

            Task.objects.create(
                memberId= member,
                taskDueDate=date_string,
                taskStatus='Not started',
                taskAssignedTo=member.memberCareManager  ,
                task = str(member) +' '+ 'Follow up for Fever for member temperature reading on' + ' ' + readingDate ,
                taskName = " Fever follow up"
            )
            interpretation = 'Fever'
        elif float(temperature) >= 41.5:

            Task.objects.create(
                memberId= member,
                taskDueDate=date_string,
                taskStatus='Not started',
                taskAssignedTo=member.memberCareManager  ,
                task = str(member) +' '+ 'Follow up for Hyperpyrexia for member temperature reading on' + ' ' + readingDate ,
                taskName = " Hyperpyrexia follow up"
            )
            interpretation = 'Hyperpyrexia'

        elif float(temperature) < 35.0:
            Task.objects.create(
                memberId= member,
                taskDueDate=date_string,
                taskStatus='Not started',
                taskAssignedTo=member.memberCareManager  ,
                task = str(member) +' '+ 'Follow up for Hypothermia for member temperature reading on' + ' ' + readingDate ,
                taskName = " Hypothermia follow up"
            )
            interpretation = 'Hypothermia'
        else:
            interpretation = 'Normal'       

        serializer.save(interpretation = interpretation)

class TemperatureDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Temperature.objects.all()
    serializer_class = TemperatureSerializer

#Oxygen Saturation
class OxygenList(generics.ListAPIView):
    serializer_class = OxygenSerializer

    def get_queryset(self):

        member_id = self.request.query_params.get('memberId', None)
        if member_id is not None:
            return Oxygen.objects.filter(memberId=member_id)
        else:
            return Oxygen.objects.none() 
    

    
class OxygenPost(generics.CreateAPIView):
    serializer_class =  OxygenSerializer

    def perform_create(self,serializer):
        member_id = self.request.data.get('memberId',None)
        oxygen = self.request.data.get('oxygen',None)
        readingDate = self.request.data.get('readingDate',None)
        updatedBy = self.request.data.get('updatedBy',None)

        #get member instace
        member = Member.objects.get(id=member_id)
        now = datetime.now().date() + timedelta(days=1)
        date_string = now.strftime("%a %b %d %Y")

             #+1
        HR = HumanResource.objects.filter(HREmail = member.memberCareManager)
        hr_member = HR.first()
        hr_member.HRTasks += 1
        hr_member.save()  

        
        if float(oxygen) < 90.0:

            Task.objects.create(
                memberId= member,
                taskDueDate=date_string,
                taskStatus='Not started',
                taskAssignedTo=member.memberCareManager  ,
                task = str(member) +' '+ 'Follow up for Hypoxemia for member oxygen saturation reading on' + ' ' + readingDate ,
                taskName = "Hypoxemia Follow up"
            )
            interpretation = 'Hypoxemia'
        elif float(oxygen) > 100:

            Task.objects.create(
                memberId= member,
                taskDueDate=date_string,
                taskStatus='Not started',
                taskAssignedTo=member.memberCareManager  ,
                task = str(member) +' '+ 'Follow up for Hyperoxemia for member oxygen saturation reading on' + ' ' + readingDate ,
                taskName = "Hyperoxemia Follow up"
            )
            interpretation = 'Hyperoxemia'

        else:
            interpretation = 'Normal'            
        

        serializer.save(interpretation = interpretation)

class OxygenDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Oxygen.objects.all()
    serializer_class = OxygenSerializer

#Pulse Rate
class PulseList(generics.ListAPIView):
    serializer_class = PulseSerializer

    def get_queryset(self):

        member_id = self.request.query_params.get('memberId', None)
        if member_id is not None:
            return PulseRate.objects.filter(memberId=member_id)
        else:
            return PulseRate.objects.none() 
    

    
class PulsePost(generics.CreateAPIView):
    serializer_class =  PulseSerializer

    def perform_create(self,serializer):
        # clinical_info = [130,80,120,60]
        # member_id = self.request.data.get('memberId',None)
        # pulse = self.request.data.get('pulse',None)
        # readingDate = self.request.data.get('readingDate',None)
        # updatedBy = self.request.data.get('updatedBy',None)

        # #get member instace
        # member = Member.objects.get(id=member_id)
        # now = datetime.now().date() + timedelta(days=1)
        # date_string = now.strftime("%a %b %d %Y")
        
        
        # if int(systolic) > clinical_info[0] or  int(diastolic) > clinical_info[2]:

        #     Task.objects.create(
        #         memberId= member,
        #         taskDueDate=date_string,
        #         taskStatus='Not started',
        #         taskAssignedTo=updatedBy  ,
        #         task = 'Follow up for hypertension for member blood pressure reading on' + ' ' + readingDate ,
        #         taskName = "Hypertension Follow up"
        #     )
        #     interpretation = 'Hypertension'
        # else:
        #     interpretation = 'Normal'            


        serializer.save(interpretation = 'Normal')

class PulseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PulseRate.objects.all()
    serializer_class = PulseSerializer

#RESPIRATORY RATE
class RespiratoryRateList(generics.ListAPIView):
    serializer_class = RespiratorySerializer

    def get_queryset(self):

        member_id = self.request.query_params.get('memberId', None)
        if member_id is not None:
            return RespiratoryRate.objects.filter(memberId=member_id)
        else:
            return RespiratoryRate.objects.none() 
    

    
class RespiratoryRatePost(generics.CreateAPIView):
    serializer_class =  RespiratorySerializer

    def perform_create(self,serializer):
        member_id = self.request.data.get('memberId',None)
        respiratory =  self.request.data.get('respiratory',None)
        readingDate = self.request.data.get('readingDate',None)
        updatedBy = self.request.data.get('updatedBy',None)

        #get member instace
        member = Member.objects.get(id=member_id)
        now = datetime.now().date() + timedelta(days=1)
        date_string = now.strftime("%a %b %d %Y")
             #+1
        HR = HumanResource.objects.filter(HREmail = member.memberCareManager)
        hr_member = HR.first()
        hr_member.HRTasks += 1
        hr_member.save()  

        if int(respiratory) < 12:

            Task.objects.create(
                memberId= member,
                taskDueDate=date_string,
                taskStatus='Not started',
                taskAssignedTo=member.memberCareManager  ,
                task = str(member) +' '+ 'Follow up for Bradypnea for member respiratory rate reading on' + ' ' + readingDate ,
                taskName = "Bradypnea Follow up"
            )
            interpretation = 'Bradypnea'
        elif int(respiratory) > 20:

            Task.objects.create(
                memberId= member,
                taskDueDate=date_string,
                taskStatus='Not started',
                taskAssignedTo=member.memberCareManager  ,
                task = str(member) +' '+ 'Follow up for Tachypnea for member respiratory rate reading on' + ' ' + readingDate ,
                taskName = "Tachypnea Follow up"
            )
            interpretation = 'Tachypnea'

        else:
            interpretation = 'Normal'            
        

        serializer.save(interpretation = interpretation)

class RespiratoryRateDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RespiratoryRate.objects.all()
    serializer_class = RespiratorySerializer

#RBS
class RandomBloodSugarList(generics.ListAPIView):
    serializer_class = RandomBloodSugarSerializer

    def get_queryset(self):

        member_id = self.request.query_params.get('memberId', None)
        if member_id is not None:
            return RandomBloodSugar.objects.filter(memberId=member_id)
        else:
            return RandomBloodSugar.objects.none() 
    

    
class RandomBloodSugarPost(generics.CreateAPIView):
    serializer_class =  RandomBloodSugarSerializer

    def perform_create(self,serializer):
        member_id = self.request.data.get('memberId',None)
        rbs =  self.request.data.get('rbs',None)
        readingDate = self.request.data.get('readingDate',None)
        updatedBy = self.request.data.get('updatedBy',None)

        #get member instace
        member = Member.objects.get(id=member_id)
        now = datetime.now().date() + timedelta(days=1)
        date_string = now.strftime("%a %b %d %Y")

             #+1
        HR = HumanResource.objects.filter(HREmail = member.memberCareManager)
        hr_member = HR.first()
        hr_member.HRTasks += 1
        hr_member.save()  
        
        if int(rbs) > 140 and int(rbs) < 200:

            Task.objects.create(
                memberId= member,
                taskDueDate=date_string,
                taskStatus='Not started',
                taskAssignedTo=member.memberCareManager  ,
                task = str(member) +' '+ 'Follow up for Prediabetes for member random blood sugar reading on' + ' ' + readingDate ,
                taskName = "Prediabetes Follow up"
            )
            interpretation = 'Prediabetes'
        elif int(rbs) >= 200:

            Task.objects.create(
                memberId= member,
                taskDueDate=date_string,
                taskStatus='Not started',
                taskAssignedTo=member.memberCareManager  ,
                task = str(member) +' '+ 'Follow up for Diabetes for member random blood sugar reading on' + ' ' + readingDate ,
                taskName = "Diabetes Follow up"
            )
            interpretation = 'Diabetes'

        else:
            interpretation = 'Normal'            
        

        serializer.save(interpretation = interpretation)

class RandomBloodSugarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RandomBloodSugar.objects.all()
    serializer_class = RandomBloodSugarSerializer

#FBS
class FastingBloodSugarList(generics.ListAPIView):
    serializer_class = FastingBloodSugarSerializer

    def get_queryset(self):

        member_id = self.request.query_params.get('memberId', None)
        if member_id is not None:
            return FastingBloodSugar.objects.filter(memberId=member_id)
        else:
            return FastingBloodSugar.objects.none() 
    

    
class FastingBloodSugarPost(generics.CreateAPIView):
    serializer_class =  FastingBloodSugarSerializer

    def perform_create(self,serializer):
        member_id = self.request.data.get('memberId',None)
        fbs =  self.request.data.get('fbs',None)
        readingDate = self.request.data.get('readingDate',None)
        updatedBy = self.request.data.get('updatedBy',None)

        #get member instace
        member = Member.objects.get(id=member_id)
        now = datetime.now().date() + timedelta(days=1)
        date_string = now.strftime("%a %b %d %Y")

             #+1
        HR = HumanResource.objects.filter(HREmail = member.memberCareManager)
        hr_member = HR.first()
        hr_member.HRTasks += 1
        hr_member.save()  


        if int(fbs) < 70:

            Task.objects.create(
                memberId= member,
                taskDueDate=date_string,
                taskStatus='Not started',
                taskAssignedTo=member.memberCareManager  ,
                task = str(member) +' '+ 'Follow up for Hypoglycemia for member fasting blood sugar reading on' + ' ' + readingDate ,
                taskName = "Hypoglycemia Follow up"
            )
            interpretation = 'Hypoglycemia'
        elif int(fbs) >= 126:

            Task.objects.create(
                memberId= member,
                taskDueDate=date_string,
                taskStatus='Not started',
                taskAssignedTo=member.memberCareManager  ,
                task = str(member) +' '+ 'Follow up for Diabetes for member fasting blood sugar reading on' + ' ' + readingDate ,
                taskName = "Diabetes Follow up"
            )
            interpretation = 'Diabetes'

        elif int(fbs) > 100 and int(fbs) < 126:

            Task.objects.create(
                memberId= member,
                taskDueDate=date_string,
                taskStatus='Not started',
                taskAssignedTo=member.memberCareManager  ,
                task = str(member) +' '+ 'Follow up for Prediabetes for member fasting blood sugar reading on' + ' ' + readingDate ,
                taskName = "Prediabetes Follow up"
            )
            interpretation = 'Prediabetes'

        else:
            interpretation = 'Normal'            
        

        serializer.save(interpretation = interpretation)


class FastingBloodSugarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FastingBloodSugar.objects.all()
    serializer_class = FastingBloodSugarSerializer

#HBA1C
class GlycatedHemoglobinList(generics.ListAPIView):
    serializer_class = GlycateHaemoglobinSerializer

    def get_queryset(self):

        member_id = self.request.query_params.get('memberId', None)
        if member_id is not None:
            return GlycatedHaemoglobin.objects.filter(memberId=member_id)
        else:
            return GlycatedHaemoglobin.objects.none() 
    

    
class GlycatedHemoglobinPost(generics.CreateAPIView):
    serializer_class =  GlycateHaemoglobinSerializer

    def perform_create(self,serializer):
        member_id = self.request.data.get('memberId',None)
        hba1c =  self.request.data.get('hba1c',None)
        readingDate = self.request.data.get('readingDate',None)
        updatedBy = self.request.data.get('updatedBy',None)

        #get member instace
        member = Member.objects.get(id=member_id)
        now = datetime.now().date() + timedelta(days=1)
        date_string = now.strftime("%a %b %d %Y")

             #+1
        HR = HumanResource.objects.filter(HREmail = member.memberCareManager)
        hr_member = HR.first()
        hr_member.HRTasks += 1
        hr_member.save()  

        
        if float(hba1c) >= 5.7 and float(hba1c) <= 6.4:

            Task.objects.create(
                memberId= member,
                taskDueDate=date_string,
                taskStatus='Not started',
                taskAssignedTo=member.memberCareManager  ,
                task = str(member) +' '+ 'Follow up for Prediabetes for member glycated haemoglobin reading on' + ' ' + readingDate ,
                taskName = "Prediabetes Follow up"
            )
            interpretation = 'Prediabetes'
        elif float(hba1c) >= 6.5:

            Task.objects.create(
                memberId= member,
                taskDueDate=date_string,
                taskStatus='Not started',
                taskAssignedTo=member.memberCareManager  ,
                task = str(member) +' '+ 'Follow up for Diabetes for member glycated haemoglobin reading on' + ' ' + readingDate ,
                taskName = "Diabetes Follow up"
            )
            interpretation = 'Diabetes'

        else:
            interpretation = 'Normal'            
 
        

        serializer.save(interpretation = interpretation)


class GlycatedHemoglobinDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = GlycatedHaemoglobin.objects.all()
    serializer_class = GlycateHaemoglobinSerializer


#BODY MASS INDEX
class BodyMassIndexList(generics.ListAPIView):
    serializer_class = BodyMassIndexSerializer

    def get_queryset(self):

        member_id = self.request.query_params.get('memberId', None)
        if member_id is not None:
            return BodyMassIndex.objects.filter(memberId=member_id)
        else:
            return BodyMassIndex.objects.none() 
    

    
class BodyMassIndexPost(generics.CreateAPIView):
    serializer_class =  BodyMassIndexSerializer

    def perform_create(self,serializer):
        member_id = self.request.data.get('memberId',None)
        height =  self.request.data.get('height',None)
        weight = self.request.data.get('weight',None)
        readingDate = self.request.data.get('readingDate',None)
        updatedBy = self.request.data.get('updatedBy',None)

        #get member instace
        member = Member.objects.get(id=member_id)
        now = datetime.now().date() + timedelta(days=1)
        date_string = now.strftime("%a %b %d %Y")

             #+1
        HR = HumanResource.objects.filter(HREmail = member.memberCareManager)
        hr_member = HR.first()
        hr_member.HRTasks += 1
        hr_member.save()  

        def calculate_bmi(weight, height):
            try:
                height_m = height/ 100  # Convert height from cm to meters
                bmi1 = weight / (height_m ** 2)
                return round(bmi1, 2)
            except ZeroDivisionError:
                return "Height cannot be zero."
            
        bmi2 = calculate_bmi(int(weight), int(height))
        print(bmi2)
        if bmi2 < 18.5:

            Task.objects.create(
                memberId= member,
                taskDueDate=date_string,
                taskStatus='Not started',
                taskAssignedTo=member.memberCareManager  ,
                task = str(member) +' '+ 'Follow up for underweight for member BMI reading on' + ' ' + readingDate ,
                taskName = "Underweight Follow up"
            )
            interpretation = 'Underweight'
        elif bmi2 >= 25 and bmi2 <= 29.9:

            Task.objects.create(
                memberId= member,
                taskDueDate=date_string,
                taskStatus='Not started',
                taskAssignedTo=member.memberCareManager  ,
                task = str(member) +' '+ 'Follow up for overweight for member BMI reading on' + ' ' + readingDate ,
                taskName = "Overweight Follow up"
            )
            interpretation = 'Overweight'

        elif bmi2>= 30 and bmi2 <= 34.9:

            Task.objects.create(
                memberId= member,
                taskDueDate=date_string,
                taskStatus='Not started',
                taskAssignedTo=member.memberCareManager  ,
                task = str(member) +' '+ 'Follow up for obesity class 1 for member BMI reading on' + ' ' + readingDate ,
                taskName = "Obesity class 1 Follow up"
            )
            interpretation = 'Obesity class 1'

        elif bmi2 >= 35 and bmi2 <= 39.9:
                
                Task.objects.create(
                    memberId= member,
                    taskDueDate=date_string,
                    taskStatus='Not started',
                    taskAssignedTo=member.memberCareManager  ,
                    task = str(member) +' '+ 'Follow up for obesity class 2 for member BMI reading on' + ' ' + readingDate ,
                    taskName = "Obesity class 2 Follow up"
                )
                interpretation = 'Obesity class 2'

        elif bmi2>= 40:
                
                Task.objects.create(
                    memberId= member,
                    taskDueDate=date_string,
                    taskStatus='Not started',
                    taskAssignedTo=member.memberCareManager  ,
                    task =  str(member) +' '+ 'Follow up for obesity class 3/severe/morbid for member BMI reading on' + ' ' + readingDate ,
                    taskName = "Obesity class 3 Follow up"
                )
                interpretation = 'Obesity class 3'

        else:
            interpretation = 'Normal'            
 
        

        serializer.save(interpretation = interpretation)


class BodyMassIndexDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BodyMassIndex.objects.all()
    serializer_class = BodyMassIndexSerializer

class ConditionList(generics.ListCreateAPIView):
    queryset = Condition.objects.all()
    serializer_class = ConditionSerializer

class ConditionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Condition.objects.all()
    serializer_class = ConditionSerializer

#MEMBER JOURNEY
class MemberJourneyList(generics.ListAPIView):
    serializer_class = MemberJourneySerializer

    def get_queryset(self):
        """
        This view returns a list of all the member journey
        for the memberId passed in the request.
        """
        member_id = self.request.query_params.get('memberId', None)
        if member_id is not None:
            return memberTaskBase.objects.filter(memberId=member_id)
        else:
            return memberTaskBase.objects.all()
        
class MemberJourneyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = memberTaskBase.objects.all()
    serializer_class = MemberJourneySerializer

#TASKS
class TaskList(generics.ListAPIView): 
    serializer_class = TaskSerializer

    def get_queryset(self):

        member_id = self.request.query_params.get('memberId', None)
        
        if member_id is not None:
            mbrTasks = Task.objects.filter(memberId=member_id)

            tasks_with_dates = []
            for task in mbrTasks:
                date_string = task.taskDueDate
                date_object = datetime.strptime(date_string, "%a %b %d %Y")
                tasks_with_dates.append((task, date_object,task.taskStatus))
            
            tasks_with_dates_sorted = sorted( tasks_with_dates,  key=lambda x: (x[2] in ["complete", "cancelled"], x[1]))
            tasks_sorted = [task for task, date, status in tasks_with_dates_sorted]
            
            return tasks_sorted

        else:
            tasks = Task.objects.all()
            return tasks
 

class TaskListPost(generics.CreateAPIView):
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        #Get the dpt
        dpt = self.request.data.get('department', None)

     #Set the Doctor, nutritionist or Psychologist assignee to task and add task to HR
        HR = HumanResource.objects.filter(HRRole = dpt, HRStatus = "Active")
        hr_with_lowest_tasks = HR.order_by('HRTasks').first()
        hr_with_lowest_tasks.HRTasks += 1
        hr_with_lowest_tasks.save()  # Save the updated object

        serializer.save(taskAssignedTo = hr_with_lowest_tasks.HREmail)
        

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

   # Update appointment status
    def perform_update(self, serializer):
        serializer.save()

        if serializer.instance.taskName == "Appointment Task":

            if serializer.instance.taskStatus == "complete":
                appointment = Appointments.objects.get(id=serializer.instance.taskAppointmentId.id)
                appointment.appointmentStatus = "complete"
                appointment.save()

            elif serializer.instance.taskStatus == "cancelled":
                appointment = Appointments.objects.get(id=serializer.instance.taskAppointmentId.id)
                appointment.appointmentStatus = "cancelled"
                appointment.save()

#Tasks analytics
@api_view(['GET'])
def TasksAnalytics(request):
   
        TasksAnalytics = []
        TaskObject = {}

        allTasks = Task.objects.all()
        #All tasks 
        TaskObject['total'] = len(allTasks)
        TaskObject['complete'] = len(allTasks.filter(taskStatus="complete"))
        TaskObject['cancelled'] = len(allTasks.filter(taskStatus="cancelled"))
        TaskObject['in_progress1'] = len(allTasks.filter(taskStatus="Inprogress"))
        TaskObject['not_started1'] = len(allTasks.filter(taskStatus="Not started"))

        #BLOOD PRESSURE
        high_bp_tasks = allTasks.filter(taskName="Hypertension Follow up")
        # TasksAnalytics.append({'total_hypertension' : len(high_bp_tasks)})
        TaskObject['total_hypertension'] = len(high_bp_tasks)

        #complete bp
        complete_high_bp_tasks = high_bp_tasks.filter(taskStatus="complete")
        TaskObject['complete_hypertension'] =  len(complete_high_bp_tasks)
        
        #Cancelled bp
        cancelled_high_bp_tasks = high_bp_tasks.filter(taskStatus="cancelled")
        TaskObject['cancelled_hypertension'] =len(cancelled_high_bp_tasks)

        #Not started
        not_started_tasks = high_bp_tasks.filter(taskStatus="Not started")
        TaskObject['not_started'] =len(not_started_tasks)

        #Inprogress
        inprogress_tasks = high_bp_tasks.filter(taskStatus="Inprogress")
        TaskObject['in_progress'] = len(inprogress_tasks)

        #High BLOOD SUGAR
        
        pre_diabetis_tasks = allTasks.filter(taskName = "Prediabetes Follow up" )
        TaskObject['Prediabetes'] = len(pre_diabetis_tasks)
        pre_diabetis_tasks_complete = pre_diabetis_tasks.filter(taskStatus = "complete")
        pre_diabetis_tasks_cancelled = pre_diabetis_tasks.filter(taskStatus = "cancelled")
        # TaskObject['complete_prediabetes'] = len(pre_diabetis_tasks_complete)
        # TaskObject['cancelled_prediabetes'] = len(pre_diabetis_tasks_cancelled)
        pre_diabetis_tasks_inprogress = pre_diabetis_tasks.filter(taskStatus = "Inprogress")
        # TaskObject['in_progress_prediabetes'] = len(pre_diabetis_tasks_inprogress)
        pre_diabetis_tasks_not_started = pre_diabetis_tasks.filter(taskStatus = "Not started")

        diabetis_tasks = allTasks.filter(taskName = "Diabetes Follow up")
        TaskObject['Diabetes'] = len(diabetis_tasks)
        diabetis_tasks_complete = diabetis_tasks.filter(taskStatus = "complete")
        diabetis_tasks_cancelled = diabetis_tasks.filter(taskStatus = "cancelled")
        diabetis_tasks_inprogress = diabetis_tasks.filter(taskStatus = "Inprogress")
        diabetis_tasks_not_started = diabetis_tasks.filter(taskStatus = "Not started")

        hypoglycemia_tasks = allTasks.filter(taskName = "Hypoglycemia Follow up")
        TaskObject['Hypoglycemia']= len(hypoglycemia_tasks)
        hypoglycemia_tasks_complete = hypoglycemia_tasks.filter(taskStatus = "complete")
        hypoglycemia_tasks_cancelled = hypoglycemia_tasks.filter(taskStatus = "cancelled")
        hypoglycemia_tasks_inprogress = hypoglycemia_tasks.filter(taskStatus = "Inprogress")
        hypoglycemia_tasks_not_started = hypoglycemia_tasks.filter(taskStatus = "Not started")

        TaskObject['complete_bs'] = len(pre_diabetis_tasks_complete) + len(diabetis_tasks_complete) + len(hypoglycemia_tasks_complete)
        TaskObject['cancelled_bs'] = len(pre_diabetis_tasks_cancelled) + len(diabetis_tasks_cancelled) + len(hypoglycemia_tasks_cancelled)
        TaskObject['in_progress_bs'] = len(pre_diabetis_tasks_inprogress) + len(diabetis_tasks_inprogress) + len(hypoglycemia_tasks_inprogress)
        TaskObject['not_started_bs'] = len(pre_diabetis_tasks_not_started) + len(diabetis_tasks_not_started) + len(hypoglycemia_tasks_not_started)


        all_bs = len(pre_diabetis_tasks) + len(diabetis_tasks) + len(hypoglycemia_tasks)
        TaskObject['all_bs'] = all_bs

        TasksAnalytics.append(TaskObject)
        return Response(TasksAnalytics)

@api_view(['GET'])
def MemberAnalytics(request):
    mbrmonths = []
    systolic_list = []
    diastolic_list = []
    member_id = request.query_params.get('memberId', None)
    
    member_bp = BloodPressure.objects.filter(memberId=member_id)
    i = 1
    allMbrBp = []

    #Blood Pressure
    #GET THE MEMBER MONTHS
    for bp in member_bp:
        reading_month = datetime.strptime(bp.readingDate, "%a %b %d %Y").date().month

        if reading_month not in mbrmonths:
            mbrmonths.append(reading_month)

    for month in mbrmonths:
        a = 'month' + str(i)
        a = []

        systolic_list.clear()
        diastolic_list.clear()

        for bp in member_bp:
            reading_date = datetime.strptime(bp.readingDate, "%a %b %d %Y").date()
            if reading_date.month == month:
                systolic_list.append(bp.systolic)
                diastolic_list.append(bp.diastolic)

        avg_systolic = sum(systolic_list) / len(systolic_list)
        avg_diastolic = sum(diastolic_list) / len(diastolic_list) 

        a.append(calendar.month_name[month][:3]) 
        a.append(avg_systolic)
        a.append(avg_diastolic)
        allMbrBp.append(a)

        i = i + 1

    return Response(allMbrBp)

    
@api_view(['GET'])
def MemberAnalyticsFbs (request):
    mbrmonths = []
    fbs_list = []
    member_id = request.query_params.get('memberId', None)

    member_fbs = FastingBloodSugar.objects.filter(memberId=member_id)
    i = 1
    allMbrBs = []

    #Blood Pressure
    #GET THE MEMBER MONTHS
    for bp in member_fbs:
        reading_month = datetime.strptime(bp.readingDate, "%a %b %d %Y").date().month

        if reading_month not in mbrmonths:
            mbrmonths.append(reading_month)

    for month in mbrmonths:
        a = 'month' + str(i)
        a = []

        fbs_list.clear()

        for bp in member_fbs:
            reading_date = datetime.strptime(bp.readingDate, "%a %b %d %Y").date()
            if reading_date.month == month:
                fbs_list.append(bp.fbs)

        avg_fbs = sum(fbs_list) / len(fbs_list)

        a.append(calendar.month_name[month][:3]) 
        a.append(avg_fbs)
        allMbrBs.append(a)

        i = i + 1

    return Response(allMbrBs)

@api_view(['GET'])
def MemberAnalyticsRbs (request):
    mbrmonths = []
    fbs_list = []
    member_id = request.query_params.get('memberId', None)

    member_fbs = RandomBloodSugar.objects.filter(memberId=member_id)
    i = 1
    allMbrBs = []

    #Blood Pressure
    #GET THE MEMBER MONTHS
    for bp in member_fbs:
        reading_month = datetime.strptime(bp.readingDate, "%a %b %d %Y").date().month

        if reading_month not in mbrmonths:
            mbrmonths.append(reading_month)

    for month in mbrmonths:
        a = 'month' + str(i)
        a = []

        fbs_list.clear()

        for bp in member_fbs:
            reading_date = datetime.strptime(bp.readingDate, "%a %b %d %Y").date()
            if reading_date.month == month:
                fbs_list.append(bp.rbs)

        avg_fbs = sum(fbs_list) / len(fbs_list)

        a.append(calendar.month_name[month][:3]) 
        a.append(avg_fbs)
        allMbrBs.append(a)

        i = i + 1

    return Response(allMbrBs)

@api_view(['GET'])
def MemberAnalyticsHba1c (request):
    mbrmonths = []
    fbs_list = []
    member_id = request.query_params.get('memberId', None)
    member_fbs = GlycatedHaemoglobin.objects.filter(memberId=member_id)
    i = 1
    allMbrBs = []

    #Blood Pressure
    #GET THE MEMBER MONTHS
    for bp in member_fbs:
        reading_month = datetime.strptime(bp.readingDate, "%a %b %d %Y").date().month

        if reading_month not in mbrmonths:
            mbrmonths.append(reading_month)

    for month in mbrmonths:
        a = 'month' + str(i)
        a = []

        fbs_list.clear()

        for bp in member_fbs:
            reading_date = datetime.strptime(bp.readingDate, "%a %b %d %Y").date()
            if reading_date.month == month:
                fbs_list.append(bp.hba1c)

        avg_fbs = sum(fbs_list) / len(fbs_list)

        a.append(calendar.month_name[month][:3]) 
        a.append(avg_fbs)
        allMbrBs.append(a)

        i = i + 1

    return Response(allMbrBs)

class AppointmentsList(generics.ListAPIView):
    serializer_class = AppointmentsSerializer

    def get_queryset(self):

        member_id = self.request.query_params.get('memberId', None)
        
        if member_id is not None:
            return Appointments.objects.filter(memberId=member_id, appointmentStatus ='Not started' or 'Inprogress')
        else:
            return Appointments.objects.all()

class AppointmentsPost(generics.CreateAPIView):
    serializer_class = AppointmentsSerializer

    def perform_create(self,serializer):

        member_id = self.request.data.get('memberId',None)
        appointmentDate =  self.request.data.get('appointmentDate',None)
        appointmentTime = self.request.data.get('appointmentTime',None)
        appointmentReason = self.request.data.get('appointmentReason',None)
        dpt = self.request.data.get('appointmentDepartment',None)

        #Set the Doctor, nutritionist or Psychologist assignee to task and add task to HR
        HR = HumanResource.objects.filter(HRRole = dpt, HRStatus = "Active")
        hr_with_lowest_tasks = HR.order_by('HRTasks').first()
        hr_with_lowest_tasks.HRTasks += 1
        hr_with_lowest_tasks.save() 

        serializer.save(appointmentAssignedTo = hr_with_lowest_tasks.HREmail)

        #get member and appointment instance
        member = Member.objects.get(id=member_id)
        appointment = Appointments.objects.get(id=serializer.data['id'])
     
        
        Task.objects.create(
            memberId= member,
            taskDueDate=appointmentDate,
            taskStatus='Not started',
            taskAssignedTo=hr_with_lowest_tasks.HREmail ,
            task = str(member) +' '+ 'appointment on' + ' ' + appointmentDate + ' ' + appointmentTime + ' ' + 'for' + ' ' + appointmentReason + 'to see' + ' ' + dpt,
            taskName = "Appointment Task",
            taskAppointmentId = appointment
        )

        return Response(serializer.data)

class AppointmentsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Appointments.objects.all()
    serializer_class = AppointmentsSerializer

@api_view(['GET'])
def AppointmentAnalytics(request):
    AppointmentsAnalytics = []
    AppointmentObject = {}

    allAppointments = Appointments.objects.all()
    #All tasks len
    AppointmentObject['total'] = len(allAppointments)

    #complete bp
    complete_appointments = allAppointments.filter(appointmentStatus="complete")
    AppointmentObject['complete'] =  len(complete_appointments)
    
    #Cancelled bp
    cancelled_appointments = allAppointments.filter(appointmentStatus="cancelled")
    AppointmentObject['cancelled'] =len(cancelled_appointments)

    #Not started
    not_started_appointments = allAppointments.filter(appointmentStatus="Not started")
    AppointmentObject['not_started'] =len(not_started_appointments)

    #Inprogress
    inprogress_appointments = allAppointments.filter(appointmentStatus="Inprogress")
    AppointmentObject['in_progress'] = len(inprogress_appointments)

    #Doctor
    doctor_appointments = allAppointments.filter(appointmentDepartment ="Doctor")
    AppointmentObject['doctor'] = len(doctor_appointments)

    #Nutritionist
    nutritionist_appointments = allAppointments.filter(appointmentDepartment ="Nutritionist")
    AppointmentObject['nutritionist'] = len(nutritionist_appointments)

    #Psychologist
    psychologist_appointments = allAppointments.filter(appointmentDepartment ="Psychologist")
    AppointmentObject['psychologist'] = len(psychologist_appointments)

    AppointmentsAnalytics.append(AppointmentObject)
    return Response(AppointmentsAnalytics)


#HR
class HR(generics.ListAPIView):
    queryset = HumanResource.objects.all()
    serializer_class = HrSerializer

        
class MyTasks(generics.ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        """
        This view returns a list of all the tasks assigned to the HR
        """
        hr_email = self.request.query_params.get('hr_email', None)
        if hr_email is not None:
            return Task.objects.filter(taskAssignedTo=hr_email)
        else:
            return Task.objects.none()
        
class send_whatsapp_message(generics.ListCreateAPIView):
 serializer_class =  WhatsappSerializer
 queryset = Whatsapp.objects.all()

# @csrf_exempt
 def perform_create(self,serializer):
    print('adding message')
    #GET MEMBER ID
    member_id = self.request.data.get('memberId',None)
    message_body = self.request.data.get('message',None)
    member = Member.objects.get(id=member_id)
    phone = '+254' + str(member.memberPhone)
    print(phone)
    print(message_body)

    # Access token and phone number ID should be stored in environment variables
    phone_number_id = '391848354014987'
    recipient_number = phone
    # message_body = "Hello!  We hope you're doing well. How are you feeling today? We'd love to ensure your health records are up-to-date. Would you like to share any updates regarding your health or wellbeing? Please let us know if there's anything you'd like to change or add. Your wellbeing is our priority!"

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }

    url = f"https://graph.facebook.com/v13.0/{phone_number_id}/messages"

    payload = {
        "messaging_product": "whatsapp",
        "to": recipient_number,
        "type": "text",
        "text": {"body": message_body}
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()  # Will raise an error for 4xx/5xx responses

        if response.status_code == 200:
            serializer.save(messageTo = '254' + str(member.memberPhone))
            print('success')
            return JsonResponse({"status": "success", "message": "Message sent successfully"})
        else:
            print('error')
            return JsonResponse({"status": "error", "message": response.text}, status=response.status_code)

    except requests.exceptions.RequestException as e:
        # This will catch all exceptions, such as connectivity issues or invalid responses
        return JsonResponse({"status": "error", "message": str(e)}, status=500)
    
def get_queryset(self):
    member_id = self.request.query_params.get('memberId', None)
    if member_id is not None:
        return Whatsapp.objects.filter(memberId=member_id)
    else:
        return Whatsapp.objects.none()

@csrf_exempt
def whatsapp_webhook(request):
    if request.method == 'GET':
        # Verify token from Facebook Developer Console
        verify_token = 'ephraim'

        # Get token from the request
        mode = request.GET.get('hub.mode')
        token = request.GET.get('hub.verify_token')
        challenge = request.GET.get('hub.challenge')

        # Check if token matches
        if mode == 'subscribe' and token == verify_token:
            return HttpResponse(challenge)
        else:
            return HttpResponse('Verification token mismatch', status=403)

    elif request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))

        print(data) 
        print(" ")

        # try:
        #     messageStatus = data.entry[0].changes[0].value.statuses[0].status
        #     messageDirection = 'Outbound'

        # except Exception as e:
        #     print('Inbound to the system')
        #     print(" ")
        
        # finally:
            # messageTo = data['entry'][0]['changes'][0]['value']['metadata']['display_phone_number']
            # messageFrom = data['entry'][0]['changes'][0]['value']['contacts'][0]['wa_id']
            # message = data['entry'][0]['changes'][0]['value']['messages'][0]['text']['body']
            # messageStatus = 'received'
            # messageDirection = 'Inbound'
            # message_id = data['entry'][0]['changes'][0]['value']['messages'][0]['id']
            # member = Member.objects.get(memberPhone = messageFrom[2:])
        print('saving') 
        print(" ")
        if (data['entry'][0]['changes'][0]['value']['messages'][0]['text']['body'] is not None):
            Whatsapp.objects.create(
            memberId = Member.objects.get(id=26),
            message = data['entry'][0]['changes'][0]['value']['messages'][0]['text']['body'],
            messageStatus = 'received',
            messageFrom = data['entry'][0]['changes'][0]['value']['contacts'][0]['wa_id'],
            messageTo = data['entry'][0]['changes'][0]['value']['metadata']['display_phone_number'],
            messageDirection = 'Inbound'
    )
        print('saved') 
        print(" ")
        return JsonResponse({'status': 'success'}, status=200)

    
    return JsonResponse({'status': 'method not allowed'}, status=405)
