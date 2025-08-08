from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


# Create your models here.
class Manager(UserManager):
    """User manager"""

    def create_user(self, username, email=None, password=None, **extra_fields):
        if not email:
            raise ValueError("Пользователь должен иметь email")
        user = self.model(
            email=email,
        )
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        user = self.model(
            email=email,
        )
        user.username = ""
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractUser):
    """User model"""

    objects = Manager()
    username = None
    email = models.EmailField(verbose_name="Email", unique=True)
    fio = models.CharField(max_length=250, verbose_name="Fio", null=True)
    confirm = models.CharField(max_length=250, verbose_name="ConfirmCode", null=True)
    comment = models.TextField(verbose_name="Comment", null=True)
    is_active = models.BooleanField(
        ("active"),
        default=False,
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.fio} - {self.email}"
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
