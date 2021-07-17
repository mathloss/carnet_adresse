from django.db import models

class Adresse(models.Model):
	nom = models.CharField(max_length=200) 
	email = models.EmailField(max_length=200)
	adresse = models.CharField(max_length=200)
	ville = models.CharField(max_length=200)
	code_postal = models.CharField(max_length=20)
	telephone = models.CharField(max_length=20)

	def __str__(self):
		return self.nom
