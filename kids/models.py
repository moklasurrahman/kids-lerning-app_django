from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


User = get_user_model()


# Create your models here.

class Course(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=250,
                            unique=True)
    image = models.ImageField(upload_to='images/')

    
    
    class Meta:
        verbose_name_plural = 'Course'
        
        
    def __str__(self):
        return self.title
    
    
    def get_absolute_url(self):
        return reverse('kids:kids_course_detail', args=[self.slug])
    
    
    
    
class BanglaLesson(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    
    
    def __str__(self):
        return self.title
        


class Requested_course(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(null=False, blank=False)
    subject_title = models.CharField(max_length=200)
    description = models.TextField()

    
    class Meta:
        verbose_name_plural = 'requested_course'
        
        
    def __str__(self):
        return self.subject_title


class Contact(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    subject = models.TextField()

    def __str__(self):
        return self.name