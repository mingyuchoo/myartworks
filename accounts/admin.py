from django.contrib import admin

# Register your models here.

from .models import Profile, Friend


class ProfileAdmin(admin.ModelAdmin):
    pass


class FriendAdmin(admin.ModelAdmin):
    pass


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Friend, FriendAdmin)
