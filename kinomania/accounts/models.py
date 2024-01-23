from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator

from kinomania.accounts.validators import validate_only_letters
# Create your models here.
class Appuser(AbstractUser):
    first_name = models.CharField(max_length=30,
                                  validators=[MinLengthValidator(2), validate_only_letters],
                                  )
    last_name = models.CharField(max_length=30,
                                 validators=[MinLengthValidator(2), validate_only_letters],
                                 )
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField(null=True, blank=True)