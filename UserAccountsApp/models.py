

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, first_name, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        
        email = email.lower()
        first_name = first_name.lower()

        email = self.normalize_email(email)
        user = self.model(email=email, date_of_birth=date_of_birth, first_name=first_name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, first_name, password):
        user = self.create_user(email=email, first_name=first_name, password=password, date_of_birth=date_of_birth)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    email = models.EmailField(max_length=150, unique=True, verbose_name='email')
    first_name = models.CharField(max_length=150, verbose_name='first name')
    last_name = models.CharField(max_length=150, verbose_name='last name')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_of_birth = models.DateField(verbose_name='date of birth')
    created_at=models.DateTimeField(auto_now_add=True)
    update_time=models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'date_of_birth']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'


class UserProfile(models.Model):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'))
    PROFESSION = (
        ('Doctor', 'Doctor'),
        ('Engineer', 'Engineer'),
        ('Student', 'Student')
    )
    user = models.OneToOneField(CustomUser, on_delete= models.CASCADE, related_name = 'profile')
    f_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=50, choices=GENDER, default='Select Here')
    date_of_birth = models.DateField(verbose_name='date of birth')
    profession = models.CharField(max_length=100, choices=PROFESSION, default='Select Here')
    academy = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='profile_image', blank=True)
    def __str__(self):
        return self.f_name

