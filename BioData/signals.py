# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Member, callMembers,CompleteOnboarding,GenerateCarePlan,DoctorsSecondConsultation,GenerateLabRequest,ScheduleAnnualLabTest,ScheduleResultsReview,AddLabResults,ScheduleVitalsCollection,CollectandSubmitVitals,InitialConsultationDoctor,InitialConsultationNutritionist,InitialMentalHealthScreening,InitialConsultationPsychologist
from django.utils.timezone import now, timedelta

@receiver(post_save, sender=Member)
def create_call_member(sender, instance, created, **kwargs):
    if created:
        callMembers.objects.create(
            memberId=instance,
            taskDate=now() + timedelta(days=3),  
            status='Not started',
            department='Care Manager',  
            assignedTo='',  
            notes=''  
        )

@receiver(post_save, sender=Member)
def complete_onboarding(sender, instance, created, **kwargs):
    if created:  # Check if a new instance of Member is created
        CompleteOnboarding.objects.create(
            memberId=instance,
            taskDate=now().date() + timedelta(days=3),
            status='Not started',
            department='Care Manager',  
            assignedTo=''  ,
            notes = ''
        )

@receiver(post_save, sender=Member)
def schedule_vitals_collection(sender, instance, created, **kwargs):
    if created:
        ScheduleVitalsCollection.objects.create(
            memberId=instance,
            taskDate=now().date() + timedelta(days=14),
            status='Not started',
            department='Care Manager',  
            assignedTo=''  ,
            notes = ''
        )

@receiver(post_save, sender=Member)
def collect_and_submit_vitals(sender, instance, created, **kwargs):
    if created:
        CollectandSubmitVitals.objects.create(
            memberId=instance,
            taskDate=now().date() + timedelta(days=17),
            status='Not started',
            department='Care Manager',  
            assignedTo=''  ,
            notes = ''
        )

@receiver(post_save, sender=Member)
def initial_consultation_doctor(sender, instance, created, **kwargs):
    if created:
        InitialConsultationDoctor.objects.create(
            memberId=instance,
            taskDate=now().date() + timedelta(days=35),
            status='Not started',
            department='Care Manager',  
            assignedTo=''  ,
            notes = ''
        )

@receiver(post_save, sender=Member)
def initial_consultation_nutritionist(sender, instance, created, **kwargs):
    if created:
        InitialConsultationNutritionist.objects.create(
            memberId=instance,
            taskDate=now().date() + timedelta(days=35),
            status='Not started',
            department='Care Manager',  
            assignedTo=''  ,
            notes = ''
        )

@receiver(post_save, sender=Member)
def initial_mental_health_screening(sender, instance, created, **kwargs):
    if created:
        InitialMentalHealthScreening.objects.create(
            memberId=instance,
            taskDate=now().date() + timedelta(days=35),
            status='Not started',
            department='Care Manager',  
            assignedTo=''  ,
            notes = ''
        )

@receiver(post_save, sender=Member)

def initial_consultation_psychologist(sender, instance, created, **kwargs):
    if created:
        InitialConsultationPsychologist.objects.create(
            memberId=instance,
            taskDate=now().date() + timedelta(days=35),
            status='Not started',
            department='Care Manager',  
            assignedTo=''  ,
            notes = ''
        )

@receiver(post_save, sender=Member)
def generate_care_plan(sender, instance, created, **kwargs):
    if created:
        GenerateCarePlan.objects.create(
            memberId=instance,
            taskDate=now().date() + timedelta(days=56),
            status='Not started',
            department='Care Manager',  
            assignedTo=''  ,
            notes = ''
        )


@receiver(post_save, sender=Member)
def generate_lab_requests(sender, instance, created, **kwargs):
    if created:
        GenerateLabRequest.objects.create(
            memberId=instance,
            taskDate=now().date() + timedelta(days=42),
            status='Not started',
            department='Care Manager',  
            assignedTo=''  ,
            notes = ''
        )

@receiver(post_save, sender=Member)

def schedule_annual_lab_test(sender, instance, created, **kwargs):
    if created:
        ScheduleAnnualLabTest.objects.create(
            memberId=instance,
            taskDate=now().date() + timedelta(days=42),
            status='Not started',
            department='Care Manager',  
            assignedTo=''  ,
            notes = ''
        )

@receiver(post_save, sender=Member)
def schedule_results_review(sender, instance, created, **kwargs):
    if created:
        ScheduleResultsReview.objects.create(
            memberId=instance,
            taskDate=now().date() + timedelta(days=49),
            status='Not started',
            department='Care Manager',  
            assignedTo=''  ,
            notes = ''
        )

@receiver(post_save, sender=Member)
def add_lab_results(sender, instance, created, **kwargs):
    if created:
        AddLabResults.objects.create(
            memberId=instance,
            taskDate=now().date() + timedelta(days=49),
            status='Not started',
            department='Care Manager',  
            assignedTo=''  ,
            notes = ''
        )

@receiver(post_save, sender=Member)
def doctors_consultation(sender, instance, created, **kwargs):
    if created:
        DoctorsSecondConsultation.objects.create(
            memberId=instance,
            taskDate=now().date() + timedelta(days=56),
            status='Not started',
            department='Care Manager',  
            assignedTo=''  ,
            notes = ''
        )



