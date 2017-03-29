from django.db import models

class Physical(models.Model):
	APPEARANCES = (
		('normal','normal'),
		('poor','poor'),
		('good','good'),
	)
	patient = models.OneToOneField('patients.Patient')
	appearance = models.CharField(max_length=12,choices=APPEARANCES,default='normal')
	temperature = models.DecimalField(max_digits=5, decimal_places=1)
	blood_pressure = models.CharField(max_length=12)
	palpation = models.CharField(max_length=25)
	palpation_first = models.DecimalField(max_digits=2, decimal_places=1)
	palpation_second = models.DecimalField(max_digits=2, decimal_places=1)



class Pathological(models.Model):
	patient = models.OneToOneField('patients.Patient')
	blood_test = models.CharField(max_length=100)



class Inspection(models.Model):
	body = models.CharField(max_length=12,choices=BODY,default='Normal')
	body_temperature = models.DecimalField(max_digits=5, decimal_places=1)
	blood_pressure = models.CharField(max_length=12)
	skin = models.CharField(max_length=12,choices=SKIN,default='Normal')
	body_weight = models.CharField(max_length=12,choices=WEIGHT,default='Normal')
	breath_frequency = models.CharField(max_length=12,choices=BREATH,default='Normal')



# class Exainations(models.Model):
# 	palpation = models.DecimalField(max_digits=25, decimal_places=2, Null=True, default=0.00)
# 	percussion = models.DecimalField(max_digits=25, decimal_places=2, Null=True, default=0.00)
# 	pathology = models.DecimalField(max_digits=25, decimal_places=2, Null=True, default=0.00)
# 	radiology = models.DecimalField(max_digits=25, decimal_places=2, Null=True, default=0.00)
# 	ct_scan = models.DecimalField(max_digits=25, decimal_places=2, Null=True, default=0.00)


	
