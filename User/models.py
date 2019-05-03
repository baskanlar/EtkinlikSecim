from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, name=None, is_active=True, is_staff=False, is_admin=False):
        if not email:
            raise ValueError('Geçerli  bir email giriniz!')
        if not password:
            raise ValueError('Geçerli bir parola giriniz!')

        user_obj = self.model(email=email)
        user_obj.set_password(password)
        user_obj.name = name
        user_obj.active = is_active
        user_obj.admin = is_admin
        user_obj.staff = is_staff
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, password, name):
        user = self.create_user(
            email=email,
            name=name,
            password=password,
            is_staff=True,
        )
        return user

    def create_superuser(self, email, password, name):
        user = self.create_user(
            email=email,
            password=password,
            name=name,
            is_admin=True,
            is_staff=True
        )
        return user


class User(AbstractBaseUser):
    Id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=128)
    active = models.BooleanField(default=True)  # can login
    staff = models.BooleanField(default=False)  # staff user non superuser
    admin = models.BooleanField(default=False)  # superuser
    timestamp = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'

    object = UserManager()

    def __str__(self):
        return self.email

    def get_name(self):
        return self.name

    @staticmethod
    def has_perm(perm, obj=None):
        return True

    @staticmethod
    def has_module_perms(app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active
