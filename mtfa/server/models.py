from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

# in your 3rd project app, e.g., sso/models.py

class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'        # field to login with
    REQUIRED_FIELDS = []
    
    class Meta:
        db_table = 'users_user'  # exact DB table name
        managed = False          # IMPORTANT: no migrations
    @property
    def is_authenticated(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_username(self):
        return self.email


