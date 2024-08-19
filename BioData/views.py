from .models import Member,Task,Dependant,memberTaskBase,Condition,Overview,Allergy,HumanResource,Surgery,Othernote,BodyMassIndex,RespiratoryRate,GlycatedHaemoglobin,FastingBloodSugar,RandomBloodSugar,Admission,Family,Social,PulseRate,InteractionLog,BloodPressure,Temperature,Oxygen
from .serializers import MemberSerializer,NewMemberSerializer,TaskSerializer,HrSerializer,MemberJourneySerializer,DependantSerializer,OverviewSerializer,ConditionSerializer,BodyMassIndexSerializer,GlycateHaemoglobinSerializer,RespiratorySerializer,FastingBloodSugarSerializer,RandomBloodSugarSerializer,AllergySerializer,PulseSerializer,OxygenSerializer,TemperatureSerializer,BloodPressureSerializer,SurgerySerializer,OthernoteSerializer,AdmissionSerializer,FamilySerializer,SocialSerializer,InteractionSerializer
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from datetime import datetime, timedelta
from rest_framework.decorators import api_view
from rest_framework.response import Response

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
            return InteractionLog.objects.all()  
    
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
        if float(temperature) >= 38.0 and float(temperature) < 41.5:

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
        elif float(temperature) >= 41.5:

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
        
        
        if float(oxygen) < 90.0:

            Task.objects.create(
                memberId= member,
                taskDueDate=date_string,
                taskStatus='Not started',
                taskDepartment='Clinical',  
                taskAssignedTo=updatedBy  ,
                task = 'Follow up for Hypoxemia for member oxygen saturation reading on' + ' ' + readingDate ,
                taskName = "Hypoxemia Follow up"
            )
            interpretation = 'Hypoxemia'
        elif float(oxygen) > 100:

            Task.objects.create(
                memberId= member,
                taskDueDate=date_string,
                taskStatus='Not started',
                taskDepartment='Clinical',  
                taskAssignedTo=updatedBy  ,
                task = 'Follow up for Hyperoxemia for member oxygen saturation reading on' + ' ' + readingDate ,
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
        #         taskDepartment='Clinical',  
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
        
        
        if int(respiratory) < 12:

            Task.objects.create(
                memberId= member,
                taskDueDate=date_string,
                taskStatus='Not started',
                taskDepartment='Clinical',  
                taskAssignedTo=updatedBy  ,
                task = 'Follow up for Bradypnea for member respiratory rate reading on' + ' ' + readingDate ,
                taskName = "Bradypnea Follow up"
            )
            interpretation = 'Bradypnea'
        elif int(respiratory) > 20:

            Task.objects.create(
                memberId= member,
                taskDueDate=date_string,
                taskStatus='Not started',
                taskDepartment='Clinical',  
                taskAssignedTo=updatedBy  ,
                task = 'Follow up for Tachypnea for member respiratory rate reading on' + ' ' + readingDate ,
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
        
        
        if int(rbs) > 140 and int(rbs) < 200:

            Task.objects.create(
                memberId= member,
                taskDueDate=date_string,
                taskStatus='Not started',
                taskDepartment='Clinical',  
                taskAssignedTo=updatedBy  ,
                task = 'Follow up for Prediabetes for member random blood sugar reading on' + ' ' + readingDate ,
                taskName = "Prediabetes Follow up"
            )
            interpretation = 'Prediabetes'
        elif int(rbs) >= 200:

            Task.objects.create(
                memberId= member,
                taskDueDate=date_string,
                taskStatus='Not started',
                taskDepartment='Clinical',  
                taskAssignedTo=updatedBy  ,
                task = 'Follow up for Diabetes for member random blood sugar reading on' + ' ' + readingDate ,
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
        
        
        if int(fbs) < 70:

            Task.objects.create(
                memberId= member,
                taskDueDate=date_string,
                taskStatus='Not started',
                taskDepartment='Clinical',  
                taskAssignedTo=updatedBy  ,
                task = 'Follow up for Hypoglycemia for member fasting blood sugar reading on' + ' ' + readingDate ,
                taskName = "Hypoglycemia Follow up"
            )
            interpretation = 'Hypoglycemia'
        elif int(fbs) >= 126:

            Task.objects.create(
                memberId= member,
                taskDueDate=date_string,
                taskStatus='Not started',
                taskDepartment='Clinical',  
                taskAssignedTo=updatedBy  ,
                task = 'Follow up for Diabetes for member fasting blood sugar reading on' + ' ' + readingDate ,
                taskName = "Diabetes Follow up"
            )
            interpretation = 'Diabetes'

        elif int(fbs) > 100 and int(fbs) < 126:

            Task.objects.create(
                memberId= member,
                taskDueDate=date_string,
                taskStatus='Not started',
                taskDepartment='Clinical',  
                taskAssignedTo=updatedBy  ,
                task = 'Follow up for Prediabetes for member fasting blood sugar reading on' + ' ' + readingDate ,
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
        
        if float(hba1c) >= 5.7 and float(hba1c) <= 6.4:

            Task.objects.create(
                memberId= member,
                taskDueDate=date_string,
                taskStatus='Not started',
                taskDepartment='Clinical',  
                taskAssignedTo=updatedBy  ,
                task = 'Follow up for Prediabetes for member glycated haemoglobin reading on' + ' ' + readingDate ,
                taskName = "Prediabetes Follow up"
            )
            interpretation = 'Prediabetes'
        elif float(hba1c) >= 6.5:

            Task.objects.create(
                memberId= member,
                taskDueDate=date_string,
                taskStatus='Not started',
                taskDepartment='Clinical',  
                taskAssignedTo=updatedBy  ,
                task = 'Follow up for Diabetes for member glycated haemoglobin reading on' + ' ' + readingDate ,
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
                taskDepartment='Clinical',  
                taskAssignedTo=updatedBy  ,
                task = 'Follow up for underweight for member BMI reading on' + ' ' + readingDate ,
                taskName = "Underweight Follow up"
            )
            interpretation = 'Underweight'
        elif bmi2 >= 25 and bmi2 <= 29.9:

            Task.objects.create(
                memberId= member,
                taskDueDate=date_string,
                taskStatus='Not started',
                taskDepartment='Clinical',  
                taskAssignedTo=updatedBy  ,
                task = 'Follow up for overweight for member BMI reading on' + ' ' + readingDate ,
                taskName = "Overweight Follow up"
            )
            interpretation = 'Overweight'

        elif bmi2>= 30 and bmi2 <= 34.9:

            Task.objects.create(
                memberId= member,
                taskDueDate=date_string,
                taskStatus='Not started',
                taskDepartment='Clinical',  
                taskAssignedTo=updatedBy  ,
                task = 'Follow up for obesity class 1 for member BMI reading on' + ' ' + readingDate ,
                taskName = "Obesity class 1 Follow up"
            )
            interpretation = 'Obesity class 1'

        elif bmi2 >= 35 and bmi2 <= 39.9:
                
                Task.objects.create(
                    memberId= member,
                    taskDueDate=date_string,
                    taskStatus='Not started',
                    taskDepartment='Clinical',  
                    taskAssignedTo=updatedBy  ,
                    task = 'Follow up for obesity class 2 for member BMI reading on' + ' ' + readingDate ,
                    taskName = "Obesity class 2 Follow up"
                )
                interpretation = 'Obesity class 2'

        elif bmi2>= 40:
                
                Task.objects.create(
                    memberId= member,
                    taskDueDate=date_string,
                    taskStatus='Not started',
                    taskDepartment='Clinical',  
                    taskAssignedTo=updatedBy  ,
                    task = 'Follow up for obesity class 3/severe/morbid for member BMI reading on' + ' ' + readingDate ,
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
            # members= Member.objects.all()
            tasks = Task.objects.all()

            # tasks_with_name = []
            # for task1 in tasks:
            #     for member1 in members:
            #         if task1.memberId == member1:
            #             tasks_with_name.append(task1)

            return tasks
 

class TaskListPost(generics.CreateAPIView):
    
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


#HR
class HR(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

#Tasks analytics
@api_view(['GET'])
def TasksAnalytics(request):
   
        TasksAnalytics = []
        TaskObject = {}

        allTasks = Task.objects.all()
        #All tasks len
        TaskObject['total'] = len(allTasks)

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
        
        # pre_diabetis_tasks = allTasks.filter(taskName = "Prediabetes Follow up" )
        # TaskObject['Prediabetes'] = len(pre_diabetis_tasks)

        # diabetis_tasks = allTasks.filter(taskName = "Diabetes Follow up")
        # TaskObject['Diabetes'] = len(diabetis_tasks)

        # hypoglycemia_tasks = allTasks.filter(taskName = "Hypoglycemia Follow up")
        # TaskObject['Hypoglycemia']= len(hypoglycemia_tasks)

        # all_bs = len(pre_diabetis_tasks) + len(diabetis_tasks) + len(hypoglycemia_tasks)
        # TaskObject['all_bs'] = all_bs

        TasksAnalytics.append(TaskObject)
        return Response(TasksAnalytics)

