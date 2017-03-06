from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

from patients.models import Patient 

class PatientListView(ListView):
	model = Patient


class PatientDetailView(DetailView):
	model=Patient 


class PatientCreateView(CreateView):
	model=Patient
	fields = [
		'first_name', 
		'last_name', 
		'sex', 
		'age', 
		'weight',
		'height', 
		'known_allergies', 
		'address',
	] 

class PatientUpdateView(UpdateView):
	model=Patient
	fields = [
		'first_name', 
		'last_name', 
		'sex', 
		'age', 
		'weight',
		'height', 
		'known_allergies', 
		'address',
	] 
	template_name_suffix = '_update_form'

class PatientDeleteView(DeleteView):
	model=Patient
	success_url = reverse_lazy("patients:patient_list")