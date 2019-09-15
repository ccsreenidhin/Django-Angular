from django.contrib.auth.models import User
from django.db import models

# Create your models here.
STATUS = (
	(0,'Approved'),
	(1,'Rejected'),
    	(2,'Processing'),
	)


class Application(models.Model):
	employee = models.ForeignKey(User, on_delete='cascade')
	date_from = models.DateField(null=True)
	date_to	= models.DateField(null=True)
	status = models.IntegerField(choices=STATUS,default=1)
	reason = models.TextField(max_length=200)
	time_received = models.DateTimeField(null=True)
	time_approved = models.DateTimeField(null=True,blank=True)
