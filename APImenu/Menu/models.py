from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from django.contrib.auth.models import BaseUserManager

class EmployeeManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

    def get_by_natural_key(self, username):
        return self.get(email=username)

class Employee(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(db_index=True, max_length=255, unique=True)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField(db_index=True, unique=True)
    telephone = models.CharField(max_length=15)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = EmployeeManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return self.email

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        return self.username


class Restaurant(models.Model):
    name = models.CharField(max_length=200, blank=False, db_index=True)
    address = models.TextField(max_length=300, blank=False, null=True)
    contact_info = models.TextField(max_length=600, blank=False, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(Employee, on_delete=models.CASCADE, primary_key=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Restaurant'
        verbose_name_plural = "Restaurants"

    def __str__(self):
        return self.name


class Menu(models.Model):
    name = models.CharField(max_length=200, blank=False, null=True, db_index=True)
    restaurant = models.OneToOneField(Restaurant, on_delete=models.CASCADE, primary_key=True,)
    items = models.ManyToManyField('MenuItem', blank=True, related_name='menus')
    is_published = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Menu'
        verbose_name_plural = "Menus"

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(max_length=200, blank=False, db_index=True)
    description = models.TextField(max_length=1000, blank=False, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'MenuItem'
        verbose_name_plural = "MenuItems"

    def __str__(self):
        return self.name


class Vote(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='votes')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='votes')
    date = models.DateField(auto_now_add=True)
    rating = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.employee.username} voted for {self.menu.name} on {self.date}'
