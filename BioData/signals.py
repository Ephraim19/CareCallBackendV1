# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Member, callMembers,CompleteOnboarding,ScheduleVitalsCollection,CollectandSubmitVitals,InitialConsultationDoctor,InitialConsultationNutritionist,InitialMentalHealthScreening,InitialConsultationPsychologist
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
            taskDate=now().date() + timedelta(days=21),
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
            taskDate=now().date() + timedelta(days=21),
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
            taskDate=now().date() + timedelta(days=21),
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
            taskDate=now().date() + timedelta(days=21),
            status='Not started',
            department='Care Manager',  
            assignedTo=''  ,
            notes = ''
        )
        


