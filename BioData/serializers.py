from rest_framework import serializers
from .models import Member,Dependant,Overview,Allergy,Surgery,Othernote,Admission,Family,Social

class DependantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dependant
        fields = ['id', 'dependantId', 'dependantNames' , 'dependantAge', 'dependantRelationship', 'dependantStatus']
        def create(self, validated_data):
            """
            Create and return a new `Dependant` instance, given the validated data.
            """
            return Dependant.objects.create(**validated_data)
        
        def update(self,instance,validated_data ):
                """
                Update and return an existing `Dependant` instance, given the validated data.
                """
                instance.dependantNames = validated_data.get('dependantNames', instance.dependantNames)
                instance.dependantAge = validated_data.get('dependantAge', instance.dependantAge)
                instance.dependantRelationship = validated_data.get('dependantRelationship', instance.dependantRelationship)
                instance.dependantStatus = validated_data.get('dependantStatus', instance.dependantStatus)
                
                instance.save()
                return instance

class OverviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Overview
        fields = ['id', 'memberId', 'overviewHealthStatus', 'overviewRiskScore', 'overviewHealthGoals', 'overViewBloodGroup']
        
        def create(self, validated_data):
            """
            Create and return a new `Overview` instance, given the validated data.
            """
            return Overview.objects.create(**validated_data)
        
        def update(self,instance,validated_data ):
                """
                Update and return an existing `Overview` instance, given the validated data.
                """
                instance.overviewHealthStatus = validated_data.get('overviewHealthStatus', instance.overviewHealthStatus)
                instance.overviewRiskScore = validated_data.get('overviewRiskScore', instance.overviewRiskScore)
                instance.overviewHealthGoals = validated_data.get('overviewHealthGoals', instance.overviewHealthGoals)
                instance.overViewBloodGroup = validated_data.get('overViewBloodGroup', instance.overViewBloodGroup)
                
                instance.save()
                return instance

class AllergySerializer(serializers.ModelSerializer):
    class Meta:
        model = Allergy
        fields = ['id', 'memberId','allergyAllargen', 'allergyReaction']
        
        def create(self, validated_data):
            return Allergy.objects.create(**validated_data)
        
        def update(self,instance,validated_data ):
            instance.allergyAllargen = validated_data.get('allergyAllargen', instance.allergyAllargen)
            instance.allergyReaction = validated_data.get('allergyReaction', instance.allergyReaction)
            instance.save()
            return instance
        

class SurgerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Surgery
        fields = ['id', 'memberId','surgeryType', 'surgeryDate']
        def create(self, validated_data):
            return Surgery.objects.create(**validated_data)
        def update(self,instance,validated_data ):
            instance.surgeryType = validated_data.get('surgeryType', instance.surgeryType)
            instance.surgeryDate = validated_data.get('surgeryDate', instance.surgeryDate)
            
            instance.save()
            return instance
    


class OthernoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Othernote
        fields = ['id','memberId','othernoteNote']
        
        def create(self,validated_data):
            return Othernote.objects.all(**validated_data)
        
        def update(self,instance,validated_data):
            instance.othernoteNote = validated_data.get("othernoteNote",instance.othernoteNote)
            instance.save()
            return instance
    
class AdmissionSerializer (serializers.ModelSerializer):
    class Meta:
        model = Admission
        fields = ['id','memberId','admissionDate','admissionReason']
        
        def create(self,validated_data):
            return Admission.objects.all(**validated_data)
        
        def update(self,instance,validated_data):
            instance.admissionReason = validated_data.get("admissionReason",instance.othernoteNote)
            instance.admissionDate = validated_data.get("admissionDate",instance.admissionDate)
            instance.save()
            return instance
     

class FamilySerializer (serializers.ModelSerializer):
    class Meta:
        model = Family
        fields = ['id','memberId','familyRelationship','familyCondition']
        
        def create(self,validated_data):
            return Family.objects.all(**validated_data)
        
        def update(self,instance,validated_data):
            instance.FamilyRelationship = validated_data.get("familyRelationship",instance.FamilyRelationship)
            instance.familyCondition = validated_data.get("familyCondition",instance.familyCondition)
            instance.save()
            return instance
        

class SocialSerializer (serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = ['id','memberId','socialNotes','atriskDueTo']
        
        def create(self,validated_data):
            return Social.objects.all(**validated_data)
        
        def update(self,instance,validated_data):
            instance.socialNotes = validated_data.get("socialNotes",instance.socialNotes)
            instance.atriskDueTo = validated_data.get("atriskDueTo",instance.atriskDueTo)
            instance.save()
            return instance

            
class MemberSerializer (serializers.ModelSerializer):
    dependants = DependantSerializer(many=True, read_only=False)
    overview = OverviewSerializer(many=True, read_only=True)
    allergy = AllergySerializer(many=True, read_only=True)
    surgery = SurgerySerializer(many=True, read_only=True)
    othernote = OthernoteSerializer(many=True, read_only=True)
    admission = AdmissionSerializer(many=True, read_only=True)
    family = FamilySerializer(many=True, read_only=True)
    social = SocialSerializer(many=True, read_only=True)
    
    class Meta:
        model = Member
        fields = ['id', 'memberName', 'memberDOB', 'memberGender', 'memberFacility', 
                  'memberPhone', 'memerEmail', 'memberPhoneTwo', 'memberOffice', 'memberHome', 
                  'memberCounty', 'memberTown', 'memberDelivery', 'memberProgram', 'memberStatus',
                 'memberOnboardingStage', 'memberCareManager', 'memberNutritionist', 'memberEngagementLead',
                 'memberEmployer', 'memberInsurer', 'memberInsuranceId', 'memberNextOfKin', 'memberNextOfKinPhone',
                  'dependants','overview','allergy','surgery','othernote','admission','family','social'
                  ]
        
        
        def create(self, validated_data):
            """
            Create and return a new `Member` instance, given the validated data.
            """
            return Member.objects.create(**validated_data)
        
        
        def update(self,instance,validated_data ):
                """
                Update and return an existing `Member` instance, given the validated data.
                """
                instance.memberName = validated_data.get('memberName', instance.memberName)
                instance.memberDOB = validated_data.get('memberDOB', instance.memberDOB)
                instance.memberGender = validated_data.get('memberGender', instance.memberGender)
                instance.memberFacility = validated_data.get('memberFacility', instance.memberFacility)
                instance.memberPhone = validated_data.get('memberPhone', instance.memberPhone)
                instance.memberEmail = validated_data.get('memberEmail', instance.memberEmail)
                instance.memberPhoneTwo = validated_data.get('memberPhoneTwo', instance.memberPhoneTwo)
                instance.memberOffice = validated_data.get('memberOffice', instance.memberOffice)
                instance.memberHome = validated_data.get('memberHome', instance.memberHome)
                instance.memberCounty = validated_data.get('memberCounty', instance.memberCounty)
                instance.memberTown = validated_data.get('memberTown', instance.memberTown)
                instance.memberDelivery = validated_data.get('memberDelivery', instance.memberDelivery)
                instance.memberProgram = validated_data.get('memberProgram', instance.memberProgram)
                instance.memberStatus = validated_data.get('memberStatus', instance.memberStatus)
                instance.memberOnboardingStage = validated_data.get('memberOnboardingStage', instance.memberOnboardingStage)
                instance.memberCareManager = validated_data.get('memberCareManager', instance.memberCareManager)
                instance.memberNutritionist = validated_data.get('memberNutritionist', instance.memberNutritionist)
                instance.memberEngagementLead = validated_data.get('memberEngagementLead', instance.memberEngagementLead)
                instance.memberEmployer = validated_data.get('memberEmployer', instance.memberEmployer)
                instance.memberInsurer = validated_data.get('memberInsurer', instance.memberInsurer)
                instance.memberInsuranceId = validated_data.get('memberInsuranceId', instance.memberInsuranceId)
                instance.memberNextOfKin = validated_data.get('memberNextOfKin', instance.memberNextOfKin)
                instance.memberNextOfKinPhone = validated_data.get('memberNextOfKinPhone', instance.memberNextOfKinPhone)
                
                instance.save()
        
                return instance

            
   
