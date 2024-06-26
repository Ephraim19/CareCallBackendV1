from django.contrib import admin
from .models import Member,Dependant,Overview,Allergy,Surgery,FastingBloodSugar,Othernote,RespiratoryRate,RandomBloodSugar,Admission,Social,Family,PulseRate,InteractionLog, BloodPressure, Temperature,Oxygen
# Register your models here.

admin.site.register(Member)
admin.site.register(Dependant)
admin.site.register(Overview)
admin.site.register(Allergy)
admin.site.register(Surgery)
admin.site.register(Othernote)
admin.site.register(Admission)
admin.site.register(Family)
admin.site.register(Social)
admin.site.register(InteractionLog)
admin.site.register(BloodPressure)
admin.site.register(Temperature)
admin.site.register(Oxygen)
admin.site.register(PulseRate)
admin.site.register(RespiratoryRate)
admin.site.register(RandomBloodSugar)
admin.site.register(FastingBloodSugar)



