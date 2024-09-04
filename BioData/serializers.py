from rest_framework import serializers
from .models import Member,Whatsapp,Task,Dependant,Prescription,Psychologist,Nutritionist,Appointments,memberTaskBase,HumanResource,Overview,Allergy,Condition,Surgery,BodyMassIndex,Othernote,FastingBloodSugar,GlycatedHaemoglobin,Admission,RandomBloodSugar,RespiratoryRate,Family,Social,InteractionLog,BloodPressure,PulseRate,Temperature,Oxygen

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
        
class InteractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = InteractionLog
        fields = ['id','created','memberId','channel','updatedBy','channelDirection','interactionDetails','taskId']

    def create(self,validated_data):
        return InteractionLog.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.channel = validated_data.get("channel",instance.channel)
        instance.updatedBy = validated_data.get("updatedBy",instance.updatedBy)
        instance.channelDirection = validated_data.get("channelDirection",instance.channelDirection)
        instance.interactionDetails = validated_data.get("interactionDetails",instance.interactionDetails)
        instance.taskId = validated_data.get("taskId",instance.taskId)
        instance.save()
        return instance
    
class BloodPressureSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodPressure
        fields = '__all__'
        
        def create(self,validated_data):
            return BloodPressure.objects.all(**validated_data)
        
        def update(self,instance,validated_data):
            instance.updatedBy = validated_data.get("updatedBy",instance.updatedBy)
            instance.readingDate = validated_data.get("readingDate",instance.readingDate)
            instance.systolic = validated_data.get("systolic",instance.systolic)
            instance.diastolic = validated_data.get("diastolic",instance.diastolic)
            instance.save()
            return instance
        
class TemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temperature
        fields = '__all__'
        
        def create(self,validated_data):
            return Temperature.objects.all(**validated_data)
        
        def update(self,instance,validated_data):
            instance.updatedBy = validated_data.get("updatedBy",instance.updatedBy)
            instance.readingDate = validated_data.get("readingDate",instance.readingDate)
            instance.temperature = validated_data.get("temperature",instance.temperature)
            instance.save()
            return instance

class OxygenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oxygen
        fields = '__all__'
        
        def create(self,validated_data):
            return Oxygen.objects.all(**validated_data)
        
        def update(self,instance,validated_data):
            instance.updatedBy = validated_data.get("updatedBy",instance.updatedBy)
            instance.readingDate = validated_data.get("readingDate",instance.readingDate)
            instance.oxygen = validated_data.get("oxygen",instance.oxygen)
            instance.save()
            return instance
        
class PulseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PulseRate
        fields = '__all__'
        
        def create(self,validated_data):
            return PulseRate.objects.all(**validated_data)
        
        def update(self,instance,validated_data):
            instance.updatedBy = validated_data.get("updatedBy",instance.updatedBy)
            instance.readingDate = validated_data.get("readingDate",instance.readingDate)
            instance.pulse = validated_data.get("pulse",instance.pulse)
            instance.save()
            return instance
        
class RespiratorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RespiratoryRate
        fields = '__all__'
        
        def create(self,validated_data):
            return RespiratoryRate.objects.all(**validated_data)
        
        def update(self,instance,validated_data):
            instance.updatedBy = validated_data.get("updatedBy",instance.updatedBy)
            instance.readingDate = validated_data.get("readingDate",instance.readingDate)
            instance.respiratory = validated_data.get("respiratory",instance.respiratory)
            instance.save()
            return instance
            
class RandomBloodSugarSerializer(serializers.ModelSerializer):
    class Meta:
        model = RandomBloodSugar
        fields = ['id','memberId','rbs','readingDate','interpretation']
        
        def create(self,validated_data):
            return RandomBloodSugar.objects.all(**validated_data)
        
        def update(self,instance,validated_data):
            instance.updatedBy = validated_data.get("updatedBy",instance.updatedBy)
            instance.readingDate = validated_data.get("readingDate",instance.readingDate)
            instance.rbs = validated_data.get("rbs",instance.rbs)
            instance.interpretation = validated_data.get("interpretation",instance.interpretation)
            instance.save()
            return instance
        
class FastingBloodSugarSerializer(serializers.ModelSerializer):
    class Meta:
        model = FastingBloodSugar
        fields = ['id','memberId','fbs','readingDate','interpretation']
        
        def create(self,validated_data):
            return FastingBloodSugar.objects.all(**validated_data)
        
        def update(self,instance,validated_data):
            instance.updatedBy = validated_data.get("updatedBy",instance.updatedBy)
            instance.readingDate = validated_data.get("readingDate",instance.readingDate)
            instance.fbs = validated_data.get("fbs",instance.fbs)
            instance.interpretation = validated_data.get("interpretation",instance.interpretation)
            instance.save()
            return instance
        
class GlycateHaemoglobinSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlycatedHaemoglobin
        fields = ['id','memberId','hba1c','readingDate','interpretation']
        
        def create(self,validated_data):
            return GlycatedHaemoglobin.objects.all(**validated_data)
        
        def update(self,instance,validated_data):
            instance.updatedBy = validated_data.get("updatedBy",instance.updatedBy)
            instance.readingDate = validated_data.get("readingDate",instance.readingDate)
            instance.hba1c = validated_data.get("hba1c",instance.hba1c)
            instance.interpretation = validated_data.get("interpretation",instance.interpretation)
            instance.save()
            return instance
        
class BodyMassIndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = BodyMassIndex
        fields = ['id','memberId','readingDate','updatedBy','height','weight','interpretation']
        
        def create(self,validated_data):
            return BodyMassIndex.objects.all(**validated_data)
        
        def update(self,instance,validated_data):
            instance.updatedBy = validated_data.get("updatedBy",instance.updatedBy)
            instance.readingDate = validated_data.get("readingDate",instance.readingDate)
            instance.height = validated_data.get("height",instance.height)
            instance.weight = validated_data.get("weight",instance.weight)
            instance.interpretation = validated_data.get("interpretation",instance.interpretation)
            instance.save()
            return instance
        

class ConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Condition
        fields = ['id', 'memberId', 'condition', 'status']
                
        def create(self, validated_data):
            return Condition.objects.create(**validated_data)
                
        def update(self, instance, validated_data):
            instance.condition = validated_data.get('condition', instance.condition)
            instance.status = validated_data.get('status', instance.status)
            instance.save()
            return instance
        
class MemberJourneySerializer(serializers.ModelSerializer):
    class Meta:
        model = memberTaskBase
        fields = ['id', 'memberId', 'taskDate', 'status', 'department', 'assignedTo', 'notes','task','notesDate','notesBy']
        
        def create(self, validated_data):
            return memberTaskBase.objects.create(**validated_data)
        
        def update(self, instance, validated_data):
            instance.taskDate = validated_data.get('taskDate', instance.taskDate)
            instance.status = validated_data.get('status', instance.status)
            instance.department = validated_data.get('department', instance.department)
            instance.assignedTo = validated_data.get('assignedTo', instance.assignedTo)
            instance.notes = validated_data.get('notes', instance.notes)
            instance.task = validated_data.get('task', instance.task)
            instance.notesDate = validated_data.get('notesDate', instance.notesDate)
            instance.notesBy = validated_data.get('notesBy', instance.notesBy)
            instance.save()
            return 
        
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id','memberId', 'taskName', 'taskDueDate', 'taskStatus', 'taskAssignedTo','task','taskAppointmentId']
        
        def create(self, validated_data):
            return Task.objects.create(**validated_data)
        
        def update(self, instance, validated_data):
            instance.taskDueDate = validated_data.get('taskDueDate', instance.taskDueDate)
            instance.taskStatus = validated_data.get('taskStatus', instance.taskStatus)
            instance.taskAssignedTo = validated_data.get('taskAssignedTo', instance.taskAssignedTo)
            instance.taskName = validated_data.get('taskName',instance.taskName)
            instance.task = validated_data.get('task', instance.task)
            instance.taskAppointmentId = validated_data.get('taskAppointmentId', instance.taskAppointmentId)
            instance.save()
            return instance
        
class HrSerializer(serializers.ModelSerializer):
    class Meta:
        model = HumanResource
        fields = ['id','HRTasks','HRRole','HRStatus','HREmail']

    def create(self, validated_data):
        return HumanResource.objects.create(**validated_data)


class AppointmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointments
        fields = ['id','memberId','appointmentDate','appointmentTime','appointmentReason','appointmentStatus',
                  'appointmentDepartment',
                  'appointmentAssignedTo','appointmentNotes','appointmentNotesDate','appointmentNotesBy','appointmentCreatedBy']
        
        def create(self, validated_data):
            return Appointments.objects.create(**validated_data)
        
        def update(self, instance, validated_data):
            instance.appointmentDate = validated_data.get('appointmentDate', instance.appointmentDate)
            instance.appointmentTime = validated_data.get('appointmentTime', instance.appointmentTime)
            instance.appointmentReason = validated_data.get('appointmentReason', instance.appointmentReason)
            instance.appointmentStatus = validated_data.get('appointmentStatus', instance.appointmentStatus)
            instance.appointmentDepartment = validated_data.get('appointmentDepartment', instance.appointmentDepartment)
            instance.appointmentAssignedTo = validated_data.get('appointmentAssignedTo', instance.appointmentAssignedTo)
            instance.appointmentNotes = validated_data.get('appointmentNotes', instance.appointmentNotes)
            instance.appointmentNotesDate = validated_data.get('appointmentNotesDate', instance.appointmentNotesDate)
            instance.appointmentNotesBy = validated_data.get('appointmentNotesBy', instance.appointmentNotesBy)
            instance.appointmentCreatedBy = validated_data.get('appointmentCreatedBy', instance.appointmentCreatedBy)
            
            instance.save()
            return instance

        
class NewMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['id', 'memberName', 'memberDOB', 'memberGender', 'memberFacility', 
                  'memberPhone', 'memerEmail']
        
        def create(self, validated_data):
            """
            Create and return a new `Member` instance, given the validated data.
            """
            return Member.objects.create(**validated_data)
        
        def update(self, instance, validated_data):
            instance.memberName = validated_data.get('memberName', instance.memberName)
            instance.memberDOB = validated_data.get('memberDOB', instance.memberDOB)
            instance.memberGender = validated_data.get('memberGender', instance.memberGender)
            instance.memberFacility = validated_data.get('memberFacility', instance.memberFacility)
            instance.memberPhone = validated_data.get('memberPhone', instance.memberPhone)
            instance.memerEmail = validated_data.get('memerEmail', instance.memerEmail)
            instance.save()
            return instance
        
class WhatsappSerializer(serializers.ModelSerializer):
    class Meta:
        model = Whatsapp
        fields = '__all__'

        def create(self, validated_data):
            return Whatsapp.objects.create(**validated_data)
        

class MemberSerializer (serializers.ModelSerializer):
    dependants = DependantSerializer(many=True, read_only=False)
    overview = OverviewSerializer(many=True, read_only=True)
    allergy = AllergySerializer(many=True, read_only=True)
    surgery = SurgerySerializer(many=True, read_only=True)
    othernote = OthernoteSerializer(many=True, read_only=True)
    admission = AdmissionSerializer(many=True, read_only=True)
    family = FamilySerializer(many=True, read_only=True)
    social = SocialSerializer(many=True, read_only=True) 
    condition = ConditionSerializer(many=True, read_only=True)

    
    class Meta:
        model = Member
        fields = ['id', 'memberName', 'memberDOB', 'memberGender', 'memberFacility', 
                  'memberPhone', 'memerEmail', 'memberPhoneTwo', 'memberOffice', 'memberHome', 
                  'memberCounty', 'memberTown', 'memberDelivery', 'memberProgram', 'memberStatus',
                 'memberOnboardingStage', 'memberCareManager', 'memberNutritionist', 'memberEngagementLead',
                 'memberEmployer', 'memberInsurer', 'memberInsuranceId', 'memberNextOfKin', 'memberNextOfKinPhone','memberDepartment',
                  'dependants','overview','allergy','surgery','othernote','admission','family','social',
                 'condition'
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

            
   
class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = ['id', 'memberId', 'prescriptionDate', 'prescriptionDrug', 'prescriptionDosage', 'prescriptionFrequency', 'prescriptionDuration']
        
        def create(self, validated_data):
            """
            Create and return a new `Prescription` instance, given the validated data.
            """
            return Prescription.objects.create(**validated_data)
        
        def update(self, instance, validated_data):
            instance.prescriptionDate = validated_data.get('prescriptionDate', instance.prescriptionDate)
            instance.prescriptionDrug = validated_data.get('prescriptionDrug', instance.prescriptionDrug)
            instance.prescriptionDosage = validated_data.get('prescriptionDosage', instance.prescriptionDosage)
            instance.prescriptionFrequency = validated_data.get('prescriptionFrequency', instance.prescriptionFrequency)
            instance.prescriptionDuration = validated_data.get('prescriptionDuration', instance.prescriptionDuration)
            instance.save()
            return instance
        
class NutritionistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nutritionist
        fields = ['id', 'memberId', 'nutritionistDate', 'nutritionistAssesment', 'nutritionistDiagnosis','nutritionistRecommendations','updatedBy']

        def create(self, validated_data):
            return Nutritionist.objects.create(**validated_data)
        

class PsychologistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Psychologist
        fields = ['id', 'memberId', 'psychologistDate', 'psychologistAssesment', 'psychologistDiagnosis','psychologistRecommendations','updatedBy']

        def create(self, validated_data):
            return Psychologist.objects.create(**validated_data)
        
        