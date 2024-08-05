from django.contrib import admin
from .models import  Profile, Role, Interest, Organization

# Register your models here.
@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Interest)
class InterestAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['name', 'logo']

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'bio', 'profile_picture', 'date_of_birth', 'role', 'organization']