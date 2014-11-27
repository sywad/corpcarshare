from django.db import models
from django.utils.encoding import smart_unicode

class eachpost(models.Model):
	email = models.EmailField(max_length=70)
	date = models.DateTimeField(auto_now_add = True, auto_now = False)
	homezip = models.CharField(max_length = 5)
	workzip = models.CharField(max_length = 5)
	workaddr = models.CharField(max_length = 50)
	workname = models.CharField(max_length = 30)

	found = models.BooleanField()
	withdraw = models.BooleanField()

	def __unicode__(self):
		return smart_unicode(self.email)

class eachcompany(models.Model):
	compname = models.CharField(max_length = 30)
	compzip = models.CharField(max_length = 5)
	compaddr = models.CharField(max_length = 50)

	def __unicode__(self):
		return smart_unicode(self.compname)
	

# Create your models here.
