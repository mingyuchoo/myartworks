from django.contrib import admin


from .models import Profile, Friend, Credit


class ProfileAdmin(admin.ModelAdmin):
    pass


class FriendAdmin(admin.ModelAdmin):
    pass


class CreditAdmin(admin.ModelAdmin):
    pass

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Friend, FriendAdmin)
admin.site.register(Credit, CreditAdmin)

