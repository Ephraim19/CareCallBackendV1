from django.db import models

class Member(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    memberName = models.CharField(max_length=50)
    memberDOB = models.DateField(blank=True,null=True )
    memberGender = models.CharField(max_length=5,blank=True)
    memberFacility = models.CharField(max_length=50,blank=True)
    memberPhone = models.IntegerField()
    memerEmail = models.EmailField(max_length=50)
    memberPhoneTwo = models.IntegerField(blank=True,null=True)
    memberOffice = models.CharField(max_length=50,blank=True)
    memberHome = models.CharField(max_length=50,blank=True)
    memberCounty = models.CharField(max_length=15,blank=True)
    memberTown = models.CharField(max_length=15,blank=True)
    memberDelivery = models.TextField()
    memberProgram = models.CharField(max_length=20,blank=True)
    memberStatus = models.CharField(max_length=20,blank=True)
    memberOnboardingStage = models.CharField(max_length=20,blank=True)
    memberCareManager = models.CharField(max_length=50,blank=True)
    memberNutritionist = models.CharField(max_length=50,blank=True)
    memberEngagementLead = models.CharField(max_length=50,blank=True)
    memberEmployer = models.CharField(max_length=50,blank=True)
    memberInsurer = models.CharField(max_length=50,blank=True)
    memberInsuranceId = models.CharField(max_length=25,blank=True)
    memberNextOfKin = models.CharField(max_length=50,blank=True)
    memberNextOfKinPhone = models.IntegerField(blank=True,null=True)
    
        
    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.memberName
    

class Dependant(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    dependantId = models.ForeignKey(Member, related_name='dependants', on_delete=models.CASCADE)
    # depandantName = models.TextField()
    dependantAge = models.IntegerField()
    dependantRelationship = models.CharField(max_length=10)
    dependantStatus = models.CharField(max_length=10)
    dependantNames = models.CharField(max_length=50)



class Overview(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    memberId = models.ForeignKey(Member, related_name='overview', on_delete=models.CASCADE)
    overviewHealthStatus = models.CharField(max_length=10)
    overviewRiskScore = models.IntegerField()
    overviewHealthGoals = models.TextField()
    overViewBloodGroup = models.CharField(max_length=3)
    
    

class Allergy(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    memberId = models.ForeignKey(Member,related_name='allergy', on_delete=models.CASCADE)
    allergyAllargen = models.CharField(max_length=20)
    allergyReaction = models.CharField(max_length=100)


class Surgery(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    memberId = models.ForeignKey(Member, related_name='surgery' , on_delete=models.CASCADE)
    surgeryType = models.CharField(max_length=50)
    surgeryDate = models.DateField()
    
class Othernote(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    memberId = models.ForeignKey(Member,related_name='othernote' , on_delete=models.CASCADE)
    othernoteNote = models.TextField()
    
class Admission(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    memberId = models.ForeignKey(Member, related_name='admission', on_delete=models.CASCADE)
    admissionDate = models.DateField()
    admissionReason = models.CharField(max_length=100)
    
class Family(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    memberId = models.ForeignKey(Member,related_name='family', on_delete=models.CASCADE)
    familyRelationship = models.CharField(max_length=20)
    familyCondition = models.CharField(max_length=50)
    
class Social(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    memberId = models.ForeignKey(Member, related_name='social', on_delete=models.CASCADE)
    socialNotes = models.CharField(max_length=20)
    atriskDueTo = models.CharField(max_length=50)
    
    
class InteractionLog(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    memberId = models.ForeignKey(Member, related_name='interaction', on_delete=models.CASCADE)
    channel = models.CharField(max_length=20,blank=True,null=True)
    updatedBy = models.EmailField()
    channelDirection = models.CharField(max_length=20,blank=True,null=True)
    interactionDetails = models.TextField()

class BloodPressure(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    memberId = models.ForeignKey(Member, related_name='bloodpressure', on_delete=models.CASCADE)
    updatedBy = models.EmailField()
    notes = models.TextField()
    readingDate = models.DateField()
    systolic = models.IntegerField()
    diastolic = models.IntegerField()
    pulse = models.IntegerField()

class Temperature(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    memberId = models.ForeignKey(Member, related_name='temperature', on_delete=models.CASCADE)
    updatedBy = models.EmailField()
    notes = models.TextField()
    readingDate = models.DateField()
    temperature = models.IntegerField()

    
class Oxygen(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    memberId = models.ForeignKey(Member, related_name='oxygen', on_delete=models.CASCADE)
    updatedBy = models.EmailField()
    notes = models.TextField()
    readingDate = models.DateField()
    oxygen = models.IntegerField()

class PulseRate(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    memberId = models.ForeignKey(Member, related_name='pulse', on_delete=models.CASCADE)
    updatedBy = models.EmailField()
    notes = models.TextField()
    readingDate = models.DateField()
    pulse = models.IntegerField()
    
class RespiratoryRate(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    memberId = models.ForeignKey(Member, related_name='respiratory', on_delete=models.CASCADE)
    updatedBy = models.EmailField()
    notes = models.TextField()
    readingDate = models.DateField()
    respiratory = models.IntegerField()
    
class RandomBloodSugar(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    memberId = models.ForeignKey(Member, related_name='rbs', on_delete=models.CASCADE)
    updatedBy = models.EmailField()
    readingDate = models.DateField()
    rbs = models.IntegerField()

class FastingBloodSugar(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    memberId = models.ForeignKey(Member, related_name='fbs', on_delete=models.CASCADE)
    updatedBy = models.EmailField()
    readingDate = models.DateField()
    fbs = models.IntegerField()
    
class GlycatedHaemoglobin(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    memberId = models.ForeignKey(Member, related_name='hba1c', on_delete=models.CASCADE)
    updatedBy = models.EmailField()
    readingDate = models.DateField()
    hba1c = models.IntegerField()
    
    
    
    
    
    
    
    
    
    
    
    
