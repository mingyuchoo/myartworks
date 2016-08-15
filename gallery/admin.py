from django.contrib import admin

from .models import Portfolio, Comment, Like, Share


class PortfolioAdmin(admin.ModelAdmin):
    pass


class CommentAdmin(admin.ModelAdmin):
    pass


class CreditAdmin(admin.ModelAdmin):
    pass


class LikeAdmin(admin.ModelAdmin):
    pass


class ShareAdmin(admin.ModelAdmin):
    pass


admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Like, LikeAdmin)
admin.site.register(Share, ShareAdmin)
