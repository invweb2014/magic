from django.db import models

class Base(models.Model):
    class Meta:
        abstract = True 
    added = models.DateField(auto_now=True, blank=True, null=True)
    modified = models.DateField(auto_now=True, blank=True, null=True)
    status =  models.CharField(max_length = 50, blank=True, null=True)

    def __str__(self):
        return str(self.id) 
    
class BaseStat(models.Model):
    class Meta:
        abstract = True
    num_view = models.IntegerField(default=0, blank=True, null=True) 
    num_comment = models.IntegerField(default=0, blank=True, null=True)
    num_rating = models.IntegerField(default=0, blank=True, null=True) 
    num_subscribed = models.IntegerField(default=0, blank=True, null=True)
    rating = models.DecimalField(max_digits=1, decimal_places=1, blank=True, null=True)

class BaseUser(models.Model):
    class Meta:
        abstract = True
    user_id = models.CharField(max_length=0, blank=True, null=True)
    user_name = models.CharField(max_length=0, blank=True, null=True) 
    email = models.CharField(max_length=0, blank=True, null=True)

       
class Comment(Base):
    name =  models.CharField(max_length = 50)
    comment =  models.CharField(max_length = 50)
    ip =  models.CharField(max_length = 50, blank=True, null=True)
    owner =  models.IntegerField(blank=True, null=True)
    ref_id = models.IntegerField(blank=True, null=True)
    ref_obj = models.CharField(max_length = 50, blank=True, null=True)

class Token(Base, BaseUser):
    code = models.CharField(max_length=100, unique=True)
    type = models.CharField(max_length=50) 
    expired = models.DateField(auto_now=True, blank=True, null=True)
    
    