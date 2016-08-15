from django.contrib import admin

from .models import Project, Membership, Comment, Bookmark, Apply, Share


class ProjectAdmin(admin.ModelAdmin):
    pass


class MembershipAdmin(admin.ModelAdmin):
    pass


class CommentAdmin(admin.ModelAdmin):
    pass


class BookmarkAdmin(admin.ModelAdmin):
    pass


class ApplyAdmin(admin.ModelAdmin):
    pass


class ShareAdmin(admin.ModelAdmin):
    pass


admin.site.register(Project, ProjectAdmin)
admin.site.register(Membership, MembershipAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Bookmark, BookmarkAdmin)
admin.site.register(Apply, ApplyAdmin)
admin.site.register(Share, ShareAdmin)
