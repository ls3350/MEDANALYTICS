from django.contrib import admin

from patients.models import Patient, Allergy

admin.site.register(Patient)
admin.site.register(Allergy)