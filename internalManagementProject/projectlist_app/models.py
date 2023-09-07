from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.contrib.auth.models import User

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
    avg_rating = models.FloatField(default=0)
    number_rating = models.IntegerField(default = 0)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="projectolist")
    
    def __str__(self):
        return self.name

class Comment(models.Model):
    comentario_user = models.ForeignKey(User,on_delete =models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    text = models.CharField(max_length=200, null=True)
    project = models.ForeignKey(Project, on_delete = models.CASCADE, related_name="comentarios")
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True) 
    
    def __str__(self):
        return str(self.rating) + self.project.name