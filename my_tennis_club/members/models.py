from django.db import models
from django.utils.module_loading import module_has_submodule


# Create your models here.
class Member(models.Model):
    firstname = models.CharField(max_length = 255)
    lastname = models.CharField(max_length = 255)
