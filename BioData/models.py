from django.db import models

class Member(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    memberName = models.CharField(max_length=50)
    memberDOB = models.CharField(max_length = 50, blank=True,null=True )
    memberGender = models.CharField(max_length=10,blank=True)
    memberFacility = models.CharField(max_length=50,blank=True)
    memberPhone = models.IntegerField()
    memerEmail = models.EmailField(max_length=50,null = True, blank = True)
    memberPhoneTwo = models.IntegerField(blank=True,null=True)
    memberOffice = models.CharField(max_length=50,blank=True)
    memberHome = models.CharField(max_length=50,blank=True)
    memberCounty = models.CharField(max_length=15,blank=True)
    memberTown = models.CharField(max_length=15,blank=True)
    memberDelivery = models.TextField(blank = True,null=True)
    memberProgram = models.CharField(max_length=20,blank=True)
    memberStatus = models.CharField(max_length=20,blank=True)
    memberOnboardingStage = models.CharField(max_length=20,blank=True)
    memberCareManager = models.EmailField()
    memberNutritionist = models.CharField(max_length=50,blank=True)
    memberEngagementLead = models.EmailField()
    memberEmployer = models.CharField(max_length=50,blank=True)
    memberInsurer = models.CharField(max_length=50,blank=True)
    memberInsuranceId = models.CharField(max_length=25,blank=True)
    memberNextOfKin = models.CharField(max_length=50,blank=True)
    memberNextOfKinPhone = models.IntegerField(blank=True,null=True)
    memberDepartment = models.CharField(max_length=50,blank=True)
    
        
    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.memberName
    

class Dependant(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    dependantId = models.ForeignKey(Member, related_name='dependants', on_delete=models.CASCADE)
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

class Condition(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    memberId = models.ForeignKey(Member,related_name='condition', on_delete=models.CASCADE)
    condition = models.CharField(max_length=20)
    status = models.CharField(max_length=100) 
    
    

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
    socialNotes = models.TextField()
    atriskDueTo = models.CharField(max_length=50)
    
    
class InteractionLog(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    memberId = models.ForeignKey(Member, related_name='interaction', on_delete=models.CASCADE)
    channel = models.CharField(max_length=20,blank=True,null=True)
    updatedBy = models.EmailField()
    channelDirection = models.CharField(max_length=20,blank=True,null=True)
    interactionDetails = models.TextField()
    taskId = models.ForeignKey('Task', related_name='taskId',null=True,blank=True, on_delete=models.CASCADE)

class BloodPressure(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    memberId = models.ForeignKey(Member, related_name='bloodpressure', on_delete=models.CASCADE)
    updatedBy = models.EmailField()
    readingDate = models.CharField(max_length=50)
    systolic = models.DecimalField(max_digits=5, decimal_places=2,null=True)
    diastolic = models.DecimalField(max_digits=5, decimal_places=2,null=True)
    interpretation = models.CharField(max_length=50,null=True,blank=True)

class Temperature(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    memberId = models.ForeignKey(Member, related_name='temperature', on_delete=models.CASCADE)
    updatedBy = models.EmailField()
    readingDate = models.CharField(max_length=50)
    temperature = models.DecimalField(max_digits=5, decimal_places=2,null=True)
    interpretation = models.CharField(max_length=50,null=True,blank=True)


    
class Oxygen(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    memberId = models.ForeignKey(Member, related_name='oxygen', on_delete=models.CASCADE)
    updatedBy = models.EmailField()
    readingDate = models.CharField(max_length=100)
    oxygen = models.DecimalField(max_digits=5, decimal_places=2,null=True)
    interpretation = models.CharField(max_length=50,null=True,blank=True)
    


class PulseRate(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    memberId = models.ForeignKey(Member, related_name='pulse', on_delete=models.CASCADE)
    updatedBy = models.EmailField()
    readingDate = models.CharField(max_length=100)
    pulse = models.DecimalField(max_digits=5, decimal_places=2,null=True)
    interpretation = models.CharField(max_length=50,null=True,blank=True)

    
class RespiratoryRate(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    memberId = models.ForeignKey(Member, related_name='respiratory', on_delete=models.CASCADE)
    updatedBy = models.EmailField()
    readingDate = models.CharField(max_length=100)
    respiratory = models.DecimalField(max_digits=5, decimal_places=2,null=True)
    interpretation = models.CharField(max_length=50,null=True,blank=True)

    
class RandomBloodSugar(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    memberId = models.ForeignKey(Member, related_name='rbs', on_delete=models.CASCADE)
    updatedBy = models.EmailField()
    readingDate = models.CharField(max_length=100)
    rbs = models.DecimalField(max_digits=5, decimal_places=2,null=True)
    interpretation = models.CharField(max_length=50,null=True,blank=True)


class FastingBloodSugar(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    memberId = models.ForeignKey(Member, related_name='fbs', on_delete=models.CASCADE)
    updatedBy = models.EmailField()
    readingDate = models.CharField(max_length=100)
    fbs = models.DecimalField(max_digits=5, decimal_places=2,null=True)
    interpretation = models.CharField(max_length=50,null=True,blank=True)

    
class GlycatedHaemoglobin(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    memberId = models.ForeignKey(Member, related_name='hba1c', on_delete=models.CASCADE)
    updatedBy = models.EmailField()
    readingDate = models.CharField(max_length=100)
    hba1c = models.DecimalField(max_digits=5, decimal_places=2)
    interpretation = models.CharField(max_length=50,null=True,blank=True)


class BodyMassIndex(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    memberId = models.ForeignKey(Member, related_name='bmi', on_delete=models.CASCADE)
    updatedBy = models.EmailField()
    readingDate = models.CharField(max_length=100)
    height = models.DecimalField(max_digits=5, decimal_places=2,null=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    interpretation = models.CharField(max_length=50,null=True,blank=True)


#Member journey tasks

class memberTaskBase(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    memberId = models.ForeignKey(Member, on_delete=models.CASCADE)
    taskDate = models.DateField()
    status = models.CharField(max_length=20,default='Not started')
    department = models.CharField(max_length=20,null=True,blank=True)
    assignedTo = models.CharField(max_length=50,null=True,blank=True)
    notes = models.TextField(blank=True,null=True)
    task = models.TextField()
    notesDate = models.CharField(max_length=50,null=True,blank=True)
    notesBy = models.EmailField()

    def __str__(self):
        return self.memberId.memberName
    

#Appointments
class Appointments(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    memberId = models.ForeignKey(Member, on_delete=models.CASCADE)
    appointmentDate = models.CharField(max_length=100)
    appointmentTime = models.CharField(max_length=100)
    appointmentReason = models.CharField(max_length=50)
    appointmentDepartment = models.CharField(max_length=50)
    appointmentCreatedBy = models.EmailField()
    appointmentStatus = models.CharField(max_length=50,default='Not started')
    appointmentAssignedTo = models.EmailField(default='machayoephraim@gmail.com')

    appointmentNotes = models.TextField(blank=True,null=True)
    appointmentNotesDate = models.CharField(max_length=50,blank=True,null=True)
    appointmentNotesBy = models.EmailField(blank=True,null=True)

    def __str__(self):
        return self.appointmentReason
    
    
#Tasks
class Task(models.Model):
        
    # STATUS_CHOICES = [
    #     ('Not started', 'Not started'),
    #     ('Inprogress', 'Inprogress'),
    #     ('Cancelled', 'Cancelled'),
    #     ('Complete', 'Complete'),
    # ]
        
    created = models.DateTimeField(auto_now_add=True)
    memberId = models.ForeignKey(Member, on_delete=models.CASCADE)
    taskName = models.CharField(max_length=50)
    task = models.TextField()
    taskDueDate = models.CharField(max_length=50)
    taskStatus = models.CharField(max_length=20)
    taskAssignedTo = models.EmailField(default='machayoephraim@gmail.com')
    taskAppointmentId = models.ForeignKey(Appointments, related_name='taskAppointmentId',null=True,blank=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.taskName

#HR
class HumanResource (models.Model): 
    ROLES = [
        ('Admin', 'Admin'),

        ('Doctor', 'Doctor'),
        ('Psychologist', 'Psychologist'),
        ('Nutritionist', 'Nutritionist'),
        ('Care Manager', 'Care Manager'),
        ('Engagement Lead', 'Engagement Lead'),
    ]

    STATUS = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
        ('On Leave', 'On Leave'),
    ]

    created = models.DateTimeField(auto_now_add=True)
    HRTasks = models.IntegerField(default = 0)
    HREmail = models.EmailField()
    HRRole = models.CharField(max_length=50,choices=ROLES,default='Care Manager')
    HRStatus = models.CharField(max_length=50,choices=STATUS,default='Active')
    # TaskId = models.ManyToManyField(Task, related_name='TaskId',blank=True)


    def __str__(self):
        return self.HREmail

class Whatsapp(models.Model):
    STATUS = [
        ('sent', 'sent'),
        ('delivered', 'delivered'),
        ('read', 'read'),
        ('received','received')
    ]
    
    DIRECTION = [
        ('Inbound', 'Inbound'),
        ('Outbound', 'Outbound'),
    ]

    created = models.DateTimeField(auto_now_add=True)
    memberId = models.ForeignKey(Member, on_delete=models.CASCADE)
    message = models.TextField()
    # messageDate = models.CharField(max_length=50,blank=True,null=True)
    messageStatus = models.CharField(max_length=50,choices=STATUS,default='Sent')
    messageFrom = models.EmailField(null=True,blank=True)
    messageTo = models.CharField(max_length = 20)

    messageDirection = models.CharField(max_length=50,choices=DIRECTION)
    # messageResponse = models.TextField(blank=True,null=True)
    # messageResponseDate = models.CharField(max_length=50,blank=True,null=True)


    
    def __str__(self):
        return self.message
    
