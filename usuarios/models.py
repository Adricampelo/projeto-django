from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.contrib.auth.hashers import make_password

class UsuarioManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        """Cria e salva um usuário com e-mail e password."""
        if not email:
            raise ValueError('O e-mail precisa ser informado')
        email = self.normalize_email(email)
        usuario = self.model(email=email, **extra_fields)
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, email, password, **extra_fields):
        """Cria e salva um superusuário."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    nome = models.CharField(max_length=60)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=256)  
    contato = models.CharField(max_length=20)
    endereco = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)  

    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'  
    REQUIRED_FIELDS = ['nome']  

    def __str__(self):
        return self.nome

def set_password(self, password):
    """Usa o método nativo do Django para criptografar a senha."""
    super().set_password(password)
