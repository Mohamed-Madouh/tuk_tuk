from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator 
# Create your models here.
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field is required")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    username = None  # Remove the default username field
    email = models.EmailField(unique=True)  # Use email as the unique identifier
    phone_number = models.CharField(max_length=11, null=True, blank=True)
    first_name = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=20, null=True, blank=True)

    USERNAME_FIELD = "email"  # Set email as the primary identifier
    REQUIRED_FIELDS = []  # No additional required fields

    objects = CustomUserManager()  # Use the custom manager
    def __str__(self):
        return self.first_name + " " + self.last_name
class PasswordReset(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    token = models.CharField(max_length=100)
    code = models.CharField(max_length=4)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"password reset for {self.user.email}"
class Profile(models.Model):
    user = models.OneToOneField(CustomUser, related_name='profile', on_delete=models.CASCADE)
    reset_code = models.CharField(max_length=4,null=True, blank=True)
    def __str__(self):
        return f"profile of {self.user.email}" 
