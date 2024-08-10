from .models import Member,Task,Dependant,memberTaskBase,Condition,Overview,Allergy,Surgery,Othernote,BodyMassIndex,RespiratoryRate,GlycatedHaemoglobin,FastingBloodSugar,RandomBloodSugar,Admission,Family,Social,PulseRate,InteractionLog,BloodPressure,Temperature,Oxygen
from .serializers import MemberSerializer,NewMemberSerializer,TaskSerializer,MemberJourneySerializer,DependantSerializer,OverviewSerializer,ConditionSerializer,BodyMassIndexSerializer,GlycateHaemoglobinSerializer,RespiratorySerializer,FastingBloodSugarSerializer,RandomBloodSugarSerializer,AllergySerializer,PulseSerializer,OxygenSerializer,TemperatureSerializer,BloodPressureSerializer,SurgerySerializer,OthernoteSerializer,AdmissionSerializer,FamilySerializer,SocialSerializer,InteractionSerializer
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from datetime import datetime, timedelta

class MemberList(generics.ListCreateAPIView):
    
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    
    
class MemberDetail(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class NewMemberAdd(generics.CreateAPIView):
    serializer_class = NewMemberSerializer

    def perform_create(self, serializer):

        memberDOB = self.request.data.get('memberDOB', None)
        memberName = self.request.data.get('memberName', None)
        memberFacility = self.request.data.get('memberFacility', None)
        memberPhone = self.request.data.get('memberPhone', None)
        memberGender = self.request.data.get('memberGender', None)
        memerEmail = self.request.data.get('memerEmail', None)
        
        serializer.save(memberDOB=memberDOB, memberName=memberName, memberFacility=memberFacility, memberPhone=memberPhone, memberGender=memberGender,memerEmail=memerEmail)


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

#BLOOD PRESSURE
class BloodPressureList(generics.ListAPIView):
    serializer_class = BloodPressureSerializer

    def get_queryset(self):

        member_id = self.request.query_params.get('memberId', None)
        if member_id is not None:
            return BloodPressure.objects.filter(memberId=member_id)
        else:
            return BloodPressure.objects.none() 
    

    
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
        
        
        if int(systolic) > clinical_info[0] or  int(diastolic) > clinical_info[2]:

            Task.objects.create(
                memberId= member,
                taskDueDate=date_string,
                taskStatus='Not started',
                taskDepartment='Clinical',  
                taskAssignedTo=updatedBy  ,
                task = 'Follow up for hypertension for member blood pressure reading on' + ' ' + readingDate ,
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
                taskDepartment='Clinical',  
                taskAssignedTo=updatedBy  ,
                task = 'Follow up for hypotension for member blood pressure reading on' +" " + readingDate, 
                taskName = "Hypertension Follow up"
            )
        #Save the task

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

        #Save the task
        if float(temperature) > 38.0 and float(temperature) < 41.5:

            Task.objects.create(
                memberId= member,
                taskDueDate=date_string,
                taskStatus='Not started',
                taskDepartment='Clinical',  
                taskAssignedTo=updatedBy  ,
                task = 'Follow up for Fever for member temperature reading on' + ' ' + readingDate ,
                taskName = " Fever follow up"
            )
            interpretation = 'Fever'
        elif float(temperature) > 41.5:

            Task.objects.create(
                memberId= member,
                taskDueDate=date_string,
                taskStatus='Not started',
                taskDepartment='Clinical',  
                taskAssignedTo=updatedBy  ,
                task = 'Follow up for Hyperpyrexia for member temperature reading on' + ' ' + readingDate ,
                taskName = " Hyperpyrexia follow up"
            )
            interpretation = 'Hyperpyrexia'

        elif float(temperature) < 35.0:
            Task.objects.create(
                memberId= member,
                taskDueDate=date_string,
                taskStatus='Not started',
                taskDepartment='Clinical',  
                taskAssignedTo=updatedBy  ,
                task = 'Follow up for Hypothermia for member temperature reading on' + ' ' + readingDate ,
                taskName = " Hypothermia follow up"
            )
            interpretation = 'Hypothermia'
        else:
            interpretation = 'Normal'       

        serializer.save(interpretation = interpretation)

class TemperatureDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Temperature.objects.all()
    serializer_class = TemperatureSerializer

class OxygenList(generics.ListCreateAPIView):
    queryset = Oxygen.objects.all()
    serializer_class = OxygenSerializer

class OxygenDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Oxygen.objects.all()
    serializer_class = OxygenSerializer

class PulseList(generics.ListCreateAPIView):
    queryset = PulseRate.objects.all()
    serializer_class = PulseSerializer

class PulseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PulseRate.objects.all()
    serializer_class = PulseSerializer

class RespiratoryRateList(generics.ListCreateAPIView):
    queryset = RespiratoryRate.objects.all()
    serializer_class = RespiratorySerializer

class RespiratoryRateDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RespiratoryRate.objects.all()
    serializer_class = RespiratorySerializer

class RandomBloodSugarList(generics.ListCreateAPIView):
    queryset = RandomBloodSugar.objects.all()
    serializer_class = RandomBloodSugarSerializer

class RandomBloodSugarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RandomBloodSugar.objects.all()
    serializer_class = RandomBloodSugarSerializer

class FastingBloodSugarList(generics.ListCreateAPIView):
    queryset = FastingBloodSugar.objects.all()
    serializer_class = FastingBloodSugarSerializer

class FastingBloodSugarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FastingBloodSugar.objects.all()
    serializer_class = FastingBloodSugarSerializer

class GlycatedHemoglobinList(generics.ListCreateAPIView):
    queryset = GlycatedHaemoglobin.objects.all()
    serializer_class = GlycateHaemoglobinSerializer

class GlycatedHemoglobinDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = GlycatedHaemoglobin.objects.all()
    serializer_class = GlycateHaemoglobinSerializer

class BodyMassIndexList(generics.ListAPIView):
    queryset = BodyMassIndex.objects.all()
    serializer_class = BodyMassIndexSerializer


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
            return memberTaskBase.objects.none()
        
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
            return Task.objects.none()  

class TaskListPost(generics.CreateAPIView):
    
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

