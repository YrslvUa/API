from django.contrib import admin
from .models import *


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('username', 'full_name', 'email', 'telephone', 'is_active', 'is_staff', 'created', 'updated')
    list_filter = ('is_staff', 'created', 'updated')
    list_editable = ('is_active',)
    search_fields = ('name',)


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'contact_info', 'owner', 'created', 'updated')
    list_filter = ('created', 'updated')
    search_fields = ('name',)


class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'restaurant', 'is_published', 'date', 'created', 'updated')
    list_filter = ('date', 'created', 'updated')
    search_fields = ('name',)


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'created', 'updated')
    list_filter = ('price', 'created', 'updated')
    search_fields = ('name',)


class VoteAdmin(admin.ModelAdmin):
    list_display = ('menu', 'employee', 'date', 'rating')
    list_filter = ('date', 'rating')
    search_fields = ('menu',)


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Vote, VoteAdmin)
