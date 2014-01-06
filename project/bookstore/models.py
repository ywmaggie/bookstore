from django.db import models
import datetime
from django.contrib import auth
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class profile(models.Model):
    user = models.OneToOneField(User)
    #username = models.CharField(max_length=100,blank=True)
    name = models.CharField(max_length=100,blank=True)
    workID = models.CharField(max_length=20,blank=True)
    age = models.IntegerField(default = 0,blank=True)
    gender_CHOICES = (
        ('F', 'Female'),
        ('M', 'Male'),
    )
    gender = models.CharField(max_length=1, choices=gender_CHOICES,blank=True)


    def __unicode__(self):
    	return u'%s' % (self.name)
    	
def create_user_profile(sender, instance, created, **kwargs):
    """
    Create user profile for new users at save user time, if it doesn't already exist
    """
    if created:
        p = profile(user=instance)
        p.name=instance.username
        p.save()

post_save.connect(create_user_profile, sender=User)

class stock_book(models.Model):
    ISBN = models.CharField(max_length=30)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=60)
    publisher = models.CharField(max_length=30)
    retail_price = models.DecimalField(max_digits=5, decimal_places=2)
    remain = models.IntegerField()
    
    def __unicode__(self):
    	return u'%s %s' % (self.ISBN, self.title)

class import_book(models.Model):
    status_CHOICES = (
        ('0', 'Pending'),
        ('1', 'Paid'),
		('2','Canceled'),
    )
    ISBN = models.CharField(max_length=30)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=60)
    publisher = models.CharField(max_length=30)
    import_price = models.DecimalField(max_digits=5, decimal_places=2)
    import_number = models.IntegerField()
    status = models.CharField(max_length=1,choices=status_CHOICES,default='0')
    
    def __unicode__(self):
    	return u'%s %s' % (self.ISBN, self.title)

    class Meta:
	ordering = ["ISBN"]

class bill(models.Model):
    inout_CHOICES = (
        ('0', 'Out'),
        ('1', 'In'),
    )
    inout = models.CharField(max_length=1, choices=inout_CHOICES)
    date = models.DateTimeField()
    amount = models.DecimalField(max_digits=9, decimal_places=2)

    def __unicode__(self):
    	return u'%s %s %d' % (self.date, self.get_inout_display,self.amount)


    
