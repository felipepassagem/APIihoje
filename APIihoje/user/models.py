from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The email field is required')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    document = models.CharField(max_length=14)  # Renamed "cpf" to "document"
    phone = models.CharField(max_length=20)
    birth_date = models.DateField(null=True)
    address = models.TextField()
    postal_code = models.CharField(max_length=10)  # Renamed "cep" to "postal_code"
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    name = models.CharField(max_length=255, blank=True)  # Campo name
    last_name = models.CharField(max_length=255, blank=True)  # Campo last_name
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    have_venues = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'  # Define o campo de autenticação como 'email'
    REQUIRED_FIELDS = []  # Campos adicionais obrigatórios ao criar superusuários

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='customuser_set'  # Renomeie o related_name para evitar conflitos
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='customuser_set'  # Renomeie o related_name para evitar conflitos
    )

    def save(self, *args, **kwargs):
        self.email = self.email.lower()  # Armazene o email em minúsculas
        super(CustomUser, self).save(*args, **kwargs)

    def __str__(self):
        return self.email


