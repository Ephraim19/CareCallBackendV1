# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Member,memberTaskBase 
from django.utils.timezone import now, timedelta

@receiver(post_save, sender=Member)
def create_call_member(sender, instance, created, **kwargs):
    if created:
        memberTaskBase.objects.create(
            memberId=instance,
            taskDate=now() + timedelta(days=3),  
            status='Not started',
            department='Care Manager',  
            assignedTo='',  
            notes=''  ,
            task = 'Call member for welcoming into CareCall'
        )

@receiver(post_save, sender=Member)
def complete_onboarding(sender, instance, created, **kwargs):
    if created:  # Check if a new instance of Member is created
        memberTaskBase.objects.create(
            memberId=instance,
            taskDate=now().date() + timedelta(days=3),
            status='Not started',
            department='Care Manager',  
            assignedTo=''  ,
            notes = '',
            task = 'Complete member onboarding process'
        )

@receiver(post_save, sender=Member)
def schedule_vitals_collection(sender, instance, created, **kwargs):
    if created:
        memberTaskBase.objects.create(
            memberId=instance,
            taskDate=now().date() + timedelta(days=14),
            status='Not started',
            department='Care Manager',  
            assignedTo=''  ,
            notes = '',
            task = 'Schedule vitals collection for memberr'
        )

@receiver(post_save, sender=Member)
def collect_and_submit_vitals(sender, instance, created, **kwargs):
    if created:
        memberTaskBase.objects.create(
            memberId=instance,
            taskDate=now().date() + timedelta(days=17),
            status='Not started',
            department='Care Manager',  
            assignedTo=''  ,
            notes = '',
            task = 'Collect and submit vitals for member'
        )

@receiver(post_save, sender=Member)
def initial_consultation_doctor(sender, instance, created, **kwargs):
    if created:
        memberTaskBase.objects.create(
            memberId=instance,
            taskDate=now().date() + timedelta(days=35),
            status='Not started',
            department='Care Manager',  
            assignedTo=''  ,
            notes = '',
            task = 'Schedule initial consultation with doctor'
        )

@receiver(post_save, sender=Member)
def initial_consultation_nutritionist(sender, instance, created, **kwargs):
    if created:
        memberTaskBase.objects.create(
            memberId=instance,
            taskDate=now().date() + timedelta(days=35),
            status='Not started',
            department='Care Manager',  
            assignedTo=''  ,
            notes = '',
            task = 'Schedule initial consultation with nutritionist'
        )

@receiver(post_save, sender=Member)
def initial_mental_health_screening(sender, instance, created, **kwargs):
    if created:
        memberTaskBase.objects.create(
            memberId=instance,
            taskDate=now().date() + timedelta(days=35),
            status='Not started',
            department='Care Manager',  
            assignedTo=''  ,
            notes = '',
            task = 'Schedule initial mental health screening'
        )

@receiver(post_save, sender=Member)

def initial_consultation_psychologist(sender, instance, created, **kwargs):
    if created:
        memberTaskBase.objects.create(
            memberId=instance,
            taskDate=now().date() + timedelta(days=35),
            status='Not started',
            department='Care Manager',  
            assignedTo=''  ,
            notes = '',
            task = 'Schedule initial consultation with psychologist'
        )

@receiver(post_save, sender=Member)
def generate_care_plan(sender, instance, created, **kwargs):
    if created:
        memberTaskBase.objects.create(
            memberId=instance,
            taskDate=now().date() + timedelta(days=56),
            status='Not started',
            department='Care Manager',  
            assignedTo=''  ,
            notes = '',
            task = 'Generate care plan for member'
        )


@receiver(post_save, sender=Member)
def generate_lab_requests(sender, instance, created, **kwargs):
    if created:
        memberTaskBase.objects.create(
            memberId=instance,
            taskDate=now().date() + timedelta(days=42),
            status='Not started',
            department='Care Manager',  
            assignedTo=''  ,
            notes = '',
            task = 'Generate lab requests for member'
        )

@receiver(post_save, sender=Member)

def schedule_annual_lab_test(sender, instance, created, **kwargs):
    if created:
        memberTaskBase.objects.create(
            memberId=instance,
            taskDate=now().date() + timedelta(days=42),
            status='Not started',
            department='Care Manager',  
            assignedTo=''  ,
            notes = '',
            task = 'Schedule annual lab test for member'
        )

@receiver(post_save, sender=Member)
def schedule_results_review(sender, instance, created, **kwargs):
    if created:
        memberTaskBase.objects.create(
            memberId=instance,
            taskDate=now().date() + timedelta(days=49),
            status='Not started',
            department='Care Manager',  
            assignedTo=''  ,
            notes = '',
            task = 'Schedule results review for member'
        )

@receiver(post_save, sender=Member)
def add_lab_results(sender, instance, created, **kwargs):
    if created:
        memberTaskBase.objects.create(
            memberId=instance,
            taskDate=now().date() + timedelta(days=49),
            status='Not started',
            department='Care Manager',  
            assignedTo=''  ,
            notes = '',
            task = 'Add lab results to member profile'
        )

@receiver(post_save, sender=Member)
def doctors_consultation(sender, instance, created, **kwargs):
    if created:
        memberTaskBase.objects.create(
            memberId=instance,
            taskDate=now().date() + timedelta(days=56),
            status='Not started',
            department='Care Manager',  
            assignedTo=''  ,
            notes = '',
            task = 'Schedule doctor’s consultation for member'
        )



