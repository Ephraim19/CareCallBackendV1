from .models import Member,Task,Dependant,memberTaskBase,Condition,Overview,Allergy,Surgery,Othernote,BodyMassIndex,RespiratoryRate,GlycatedHaemoglobin,FastingBloodSugar,RandomBloodSugar,Admission,Family,Social,PulseRate,InteractionLog,BloodPressure,Temperature,Oxygen
from .serializers import MemberSerializer,NewMemberSerializer,TaskSerializer,MemberJourneySerializer,DependantSerializer,OverviewSerializer,ConditionSerializer,BodyMassIndexSerializer,GlycateHaemoglobinSerializer,RespiratorySerializer,FastingBloodSugarSerializer,RandomBloodSugarSerializer,AllergySerializer,PulseSerializer,OxygenSerializer,TemperatureSerializer,BloodPressureSerializer,SurgerySerializer,OthernoteSerializer,AdmissionSerializer,FamilySerializer,SocialSerializer,InteractionSerializer
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from datetime import datetime

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
    
    def perform_create(self, serializer):
        member_id = self.request.data.get('memberId',None)
        if not member_id:
            raise ValidationError('memberId field is required.')

        # You can add additional logic here if needed
        serializer.save(memberId=member_id)
    
class BloodPressurePost(generics.CreateAPIView):
    queryset = BloodPressure.objects.all()
    serializer_class = BloodPressureSerializer

class BloodPressureDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BloodPressure.objects.all()
    serializer_class = BloodPressureSerializer

class TemperatureList(generics.ListCreateAPIView):
    queryset = Temperature.objects.all()
    serializer_class = TemperatureSerializer

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

class BodyMassIndexList(generics.ListCreateAPIView):
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
            return Task.objects.filter(memberId=member_id)
        else:
            return Task.objects.none()  

class TaskListPost(generics.CreateAPIView):
    
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

