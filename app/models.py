from django.db import models
from django.contrib import messages
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def registration_validator(self,dataPost):
        errors = {}
        print(dataPost)
        if len(dataPost['first_name']) < 2:
            errors['first_name'] = "First name must have 2 and more characters."
        if len(dataPost['last_name']) < 2:
            errors['last_name'] = "Last name must have 2 and more characters."
        # if dataPost['bday']=="":
        #     errors['bday']="Birthday cannot be empty"
        # else:
        #     if datetime.today()<datetime.strptime(dataPost['bday'], '%Y-%M-%d'):
        #         errors['bday']="No dates in the future"
        if not EMAIL_REGEX.match(dataPost['email']):
            errors['email'] = "Email is invalid."
        # if len(dataPost['bio'])>100:
        #     errors['bio']="Bio too long"
        if dataPost['password'] == "":
            errors['password'] = "Password must have 8 or more characters."
        if dataPost['password'] != dataPost['confirm_password']:
            errors['confirm_pass'] = "Passwords do not match."
        return errors


    def login_validator(self,dataPost):
        errors = {}
        print(dataPost)
        if not EMAIL_REGEX.match(dataPost['email']):
            errors['email'] = "Invalid credentials."
        if dataPost['password'] == "":
            errors['password'] = "Invalid credentials."
        return errors


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    pw_hash = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
    userManager = UserManager()