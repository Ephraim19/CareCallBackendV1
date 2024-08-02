from .models import Member,Task,Dependant,Overview,Allergy,Surgery,Othernote,GenerateCarePlan,GenerateLabRequest,ScheduleAnnualLabTest,ScheduleResultsReview,DoctorsSecondConsultation,Condition,InitialConsultationNutritionist,InitialConsultationDoctor,InitialConsultationPsychologist,InitialMentalHealthScreening,callMembers,CollectandSubmitVitals,ScheduleVitalsCollection,CompleteOnboarding,BodyMassIndex,RespiratoryRate,GlycatedHaemoglobin,FastingBloodSugar,RandomBloodSugar,Admission,Family,Social,PulseRate,InteractionLog,BloodPressure,Temperature,Oxygen
from .serializers import MemberSerializer,TaskSerializer,DependantSerializer,GenerateCarePlanSerializer,GenerateLabRequestSerializer,ScheduleAnnualLabTestSerializer,ScheduleResultsReviewSerializer,DoctorsSecondConsultationSerializer,callMembersSerializer,CollectandSubmitVitalsSerializer,InitialConsultationDoctorSerializer,InitialConsultationNutritionistSerializer,InitialConsultationPsychologistSerializer,InitialMentalHealthScreeningSerializer,ScheduleVitalsCollectionSerializer,CompleteOnboardingSerializer,OverviewSerializer,ConditionSerializer,BodyMassIndexSerializer,GlycateHaemoglobinSerializer,RespiratorySerializer,FastingBloodSugarSerializer,RandomBloodSugarSerializer,AllergySerializer,PulseSerializer,OxygenSerializer,TemperatureSerializer,BloodPressureSerializer,SurgerySerializer,OthernoteSerializer,AdmissionSerializer,FamilySerializer,SocialSerializer,InteractionSerializer
from rest_framework import generics
from rest_framework.exceptions import ValidationError

class MemberList(generics.ListCreateAPIView):
    
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    
    
    
class MemberDetail(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    
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
class BloodPressureList(generics.ListCreateAPIView):
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

class callMembersList(generics.ListCreateAPIView):
    queryset = callMembers.objects.all()
    serializer_class = callMembersSerializer

class callMembersDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = callMembers.objects.all()
    serializer_class = callMembersSerializer

class CompleteOnboardingList(generics.ListCreateAPIView):
    queryset = CompleteOnboarding.objects.all()
    serializer_class = CompleteOnboardingSerializer

class CompleteOnboardingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CompleteOnboarding.objects.all()
    serializer_class = CompleteOnboardingSerializer

class ScheduleVitalsCollectionList(generics.ListCreateAPIView):
    queryset = ScheduleVitalsCollection.objects.all()
    serializer_class = ScheduleVitalsCollectionSerializer

class ScheduleVitalsCollectionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ScheduleVitalsCollection.objects.all()
    serializer_class = ScheduleVitalsCollectionSerializer

class CollectandSubmitVitalsList(generics.ListCreateAPIView):
    queryset = CollectandSubmitVitals.objects.all()
    serializer_class = CollectandSubmitVitalsSerializer

class CollectandSubmitVitalsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CollectandSubmitVitals.objects.all()
    serializer_class = CollectandSubmitVitalsSerializer

class InitialConsultationDoctorList(generics.ListCreateAPIView):
    queryset = InitialConsultationDoctor.objects.all()
    serializer_class = InitialConsultationDoctorSerializer

class InitialConsultationDoctorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = InitialConsultationDoctor.objects.all()
    serializer_class = InitialConsultationDoctorSerializer

class InitialConsultationNutritionistList(generics.ListCreateAPIView):
    queryset = InitialConsultationNutritionist.objects.all()
    serializer_class = InitialConsultationNutritionistSerializer

class InitialConsultationNutritionistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = InitialConsultationNutritionist.objects.all()
    serializer_class = InitialConsultationNutritionistSerializer

class InitialConsultationPsychologistList(generics.ListCreateAPIView):
    queryset = InitialConsultationPsychologist.objects.all()
    serializer_class = InitialConsultationPsychologistSerializer

class InitialConsultationPsychologistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = InitialConsultationPsychologist.objects.all()
    serializer_class = InitialConsultationPsychologistSerializer

class InitialMentalHealthScreeningList(generics.ListCreateAPIView):
    queryset = InitialMentalHealthScreening.objects.all()
    serializer_class = InitialMentalHealthScreeningSerializer

class InitialMentalHealthScreeningDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = InitialMentalHealthScreening.objects.all()
    serializer_class = InitialMentalHealthScreeningSerializer

class GenerateCarePlanList(generics.ListCreateAPIView):
    queryset = GenerateCarePlan.objects.all()
    serializer_class = GenerateCarePlanSerializer

class GenerateCarePlanDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = GenerateCarePlan.objects.all()
    serializer_class = GenerateCarePlanSerializer

class GenerateLabRequestList(generics.ListCreateAPIView):
    queryset = GenerateLabRequest.objects.all()
    serializer_class = GenerateLabRequestSerializer

class GenerateLabRequestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = GenerateLabRequest.objects.all()
    serializer_class = GenerateLabRequestSerializer

class ScheduleAnnualLabTestList(generics.ListCreateAPIView):
    queryset = ScheduleAnnualLabTest.objects.all()
    serializer_class = ScheduleAnnualLabTestSerializer

class ScheduleAnnualLabTestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ScheduleAnnualLabTest.objects.all()
    serializer_class = ScheduleAnnualLabTestSerializer

class ScheduleResultsReviewList(generics.ListCreateAPIView):
    queryset = ScheduleResultsReview.objects.all()
    serializer_class = ScheduleResultsReviewSerializer

class ScheduleResultsReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ScheduleResultsReview.objects.all()
    serializer_class = ScheduleResultsReviewSerializer

class DoctorsSecondConsultationList(generics.ListCreateAPIView):

    queryset = DoctorsSecondConsultation.objects.all()
    serializer_class = DoctorsSecondConsultationSerializer

class DoctorsSecondConsultationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DoctorsSecondConsultation.objects.all()
    serializer_class = DoctorsSecondConsultationSerializer


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

