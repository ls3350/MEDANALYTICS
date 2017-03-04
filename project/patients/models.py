from django.db import models



class Patient(models.Model):

	SEX = (
		('male','male'),
		('female','female'),
		('transgender','transgender'),
	)
	first_name = models.CharField(max_length=25, blank=True)
	last_name = models.CharField(max_length=25, blank=True)
	sex = models.CharField(max_length=12,choices=SEX,default='female')
	age = models.IntegerField(blank=True, null=True)
	weight = models.FloatField(blank=True, null=True)
	height = models.FloatField(blank=True, null=True)
	known_allergies = models.ManyToManyField('Allergy', blank=True)
	address = models.CharField(max_length=25, blank=True)


	def __str__(self):
		return self.last_name


class Allergy(models.Model):
	medication = models.CharField(max_length=25, blank=True)
	food = models.CharField(max_length=25, blank=True)
	enviornmetal = models.CharField(max_length=25, blank=True)


