from django.contrib import admin
from userauths.models import Profile, User
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','full_name', 'date']

admin.site.register(Profile, ProfileAdmin)
admin.site.register(User)