from django.contrib import admin
from .models import Member,Dependant,Overview,Allergy,Surgery,Othernote,Admission,Family,Social,InteractionLog, BloodPressure, Temperature
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



