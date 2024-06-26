from .models import Member,Dependant,Overview,Allergy,Surgery,Othernote,Admission,Family,Social,InteractionLog,BloodPressure
from .serializers import MemberSerializer,DependantSerializer,OverviewSerializer,AllergySerializer,BloodPressureSerializer,SurgerySerializer,OthernoteSerializer,AdmissionSerializer,FamilySerializer,SocialSerializer,InteractionSerializer
from rest_framework import generics

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

class InteractionList(generics.ListCreateAPIView):
    queryset = InteractionLog.objects.all()
    serializer_class = InteractionSerializer
    
class InteractionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = InteractionLog.objects.all()
    serializer_class = InteractionSerializer

class BloodPressureList(generics.ListCreateAPIView):
    queryset = BloodPressure.objects.all()
    serializer_class = BloodPressureSerializer

class BloodPressureDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BloodPressure.objects.all()
    serializer_class = BloodPressureSerializer