from django.db import models 
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin

class UserManager(BaseUserManager):
    use_in_migrations = True
    
    def create_user(self, username, password, email=''):
        user = self.model(
            username = username,
            email = email,
        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, password, email=''):
        user = self.create_user(
            username = username,
            email = '',
            password=password
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser,PermissionsMixin):
    objects = UserManager()
    username = models.CharField(
        max_length=20,
        null=False,
        unique=True
    )
    email = models.EmailField(
        max_length=255,
        null=True,
        blank=True,
    )
    refresh_count = models.PositiveIntegerField(default=5)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True, null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password']