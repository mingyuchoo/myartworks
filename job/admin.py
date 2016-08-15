from django.contrib import admin

from .models import Work, Comment, Bookmark, Apply, Share


class WorkAdmin(admin.ModelAdmin):
    pass


class CommentAdmin(admin.ModelAdmin):
    pass


class BookmarkAdmin(admin.ModelAdmin):
    pass


class ApplyAdmin(admin.ModelAdmin):
    pass


class ShareAdmin(admin.ModelAdmin):
    pass


admin.site.register(Work, WorkAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Bookmark, BookmarkAdmin)
admin.site.register(Apply, ApplyAdmin)
admin.site.register(Share, ShareAdmin)
