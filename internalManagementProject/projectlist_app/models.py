from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150)
    img = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    

class Project(models.Model):
    name = models.CharField(max_length=150)
    decription = models.CharField(max_length=800)
    type = models.CharField(max_length=150)
    status = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="projectolist")
    
    def __str__(self):
        return self.name
