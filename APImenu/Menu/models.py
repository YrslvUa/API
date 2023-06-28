from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=200, blank=False, db_index=True)
    address = models.TextField(max_length=300, blank=False, null=True)
    contact_info = models.TextField(max_length=600, blank=False, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Restaurant'
        verbose_name_plural = "Restaurants"

    def __str__(self):
        return self.name


class Menu(models.Model):
    name = models.CharField(max_length=200, blank=False, null=True, db_index=True)
    restaurant = models.ForeignKey(
        Restaurant,
        default=1,
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
    )
    items = models.ManyToManyField('MenuItem', blank=True)
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
    price = models.DecimalField(max_digits=10, decimal_places=2, default=00.00)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'MenuItem'
        verbose_name_plural = "MenuItems"

    def __str__(self):
        return self.name
class Employee(models.Model):
    pass
# user: OneToOneField (User, if you're using Django's built-in User model)
# restaurant: ForeignKey (Restaurant)

class Vote(models.Model):
    pass
# employee: ForeignKey (Employee)
# menu: ForeignKey (Menu)
# date: DateField
