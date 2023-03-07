"""Database models"""
from django.conf import settings
from django.db import models
import uuid
import os
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

PROJECT_TYPE= [
    ("DATA SCIENCE","DATA SCIENCE"),
    ("DATA ANALYTICS","DATA ANLYTICS"),
    ("AGRICULTURAL ENGINEERNG","AGRICULTURAL ENGINEERING"),
    ("OTHERS","OTHERS")
]
PROJECT_STATUS= [
    ("COMPLETED","COMPLETED"),
    ("ON GOING","ON GOING"),
    ("PENDING","PENDING"),
]
def project_image_file_path(instance, filename):
    """Generate file path for new project image"""
    ext= os.path.splitext(filename)[1]
    filename= f'{uuid.uuid4()}{ext}'

    return os.path.join('uploads','project', filename)

class UserManager(BaseUserManager):
    """Manager for users. """
    def create_user(self, email, password=None, **extra_field):
        """create, save and return a new user"""
        if not email:
            raise ValueError('User must have email address.')
        user= self.model(email= self.normalize_email(email), **extra_field)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """create and return a new superuser."""
        user= self.create_user(email, password)
        user.is_staff= True
        user.is_superuser= True
        user.save(using= self._db)

        return user

class User(AbstractBaseUser, PermissionsMixin):
    """User in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects= UserManager()
    USERNAME_FIELD = 'email'

class Projects(models.Model):
    """Projects Model."""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete= models.CASCADE,
    )
    title= models.CharField(max_length=200)
    caption= models.TextField(null=True, blank=True)
    type=models.CharField(max_length=200, choices=PROJECT_TYPE,null=True, blank=True)
    thumbnail= models.ImageField(null=True,blank=True,default='/uploads/project/default_thumbnail.jpg', upload_to=project_image_file_path)
    tags= models.ManyToManyField('Tag')
    description= models.TextField(null=True, blank=True)
    created= models.DateTimeField(auto_now_add= True)
    id= models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True,editable=False)
    status=models.CharField(max_length=200, choices=PROJECT_STATUS , null=True, blank=True)
    demo_link= models.CharField(max_length=2000, null=True,blank=True)
    github_link= models.CharField(max_length=2000, null=True,blank=True)
    kaggle_link= models.CharField(max_length=2000, null=True,blank=True)
    other_source_link= models.CharField(max_length=2000, null=True,blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering= ['-created']

class Tag(models.Model):
    """Tag for projects"""
    name= models.CharField(max_length=255)
    id= models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True,editable=False)
    user = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete= models.CASCADE,
    )
    def __str__(self):
        return self.name

class Education(models.Model):
    """Education for info"""
    title= models.CharField(max_length=200)
    period= models.CharField(max_length=200)
    college= models.CharField(max_length=200)
    created=  models.DateTimeField(auto_now_add= True)
    id= models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True,editable=False)

    def __str__(self):
        return self.title

class Experience(models.Model):
    """Experience for info"""
    title= models.CharField(max_length=200)
    period= models.CharField(max_length=200)
    company= models.CharField(max_length=200)
    created=  models.DateTimeField(auto_now_add= True)
    id= models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True,editable=False)

    def __str__(self):
        return self.title

class Certificate(models.Model):
    """Certificate for info"""
    title= models.CharField(max_length=200)
    period= models.CharField(max_length=200)
    platform= models.CharField(max_length=200)
    created=  models.DateTimeField(auto_now_add= True)
    link= models.CharField(max_length=2000, null=True,blank=True)
    id= models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True,editable=False)

    def __str__(self):
        return self.title

class Skill(models.Model):
    """Skill for info"""
    skillname = models.CharField(max_length=200)
    body=models.TextField(blank=True, null=True)
    type=models.CharField(max_length=200, choices=PROJECT_TYPE,null=True, blank=True)
    created=  models.DateTimeField(auto_now_add= True)
    id= models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True,editable=False)

    def __str__(self):
        return self.skillname

class SocialLink(models.Model):
    """SocialLink for info"""
    linkedin= models.CharField(max_length=2000, null=True,blank=True)
    github= models.CharField(max_length=2000, null=True,blank=True)
    kaggle= models.CharField(max_length=2000, null=True,blank=True)
    facebook= models.CharField(max_length=2000, null=True,blank=True)
    instagram= models.CharField(max_length=2000, null=True,blank=True)
    created=  models.DateTimeField(auto_now_add= True)
    id= models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True,editable=False)


class Message(models.Model):
    firstname= models.CharField(max_length=200, null=True, blank=True)
    lastname= models.CharField(max_length=200, null=True, blank=True)
    email= models.EmailField(max_length=200)
    Message= models.TextField()
    phone= models.IntegerField(null=True, blank=True)
    interests=models.CharField(max_length=200, choices=PROJECT_TYPE , null=True, blank=True)
    is_read= models.BooleanField(default=False,  null=True, blank=True)
    created=  models.DateTimeField(auto_now_add= True)
    id= models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True,editable=False)

    def __str__(self):
        return self.email
