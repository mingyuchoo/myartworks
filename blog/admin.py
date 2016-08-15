from django.contrib import admin

from .models import Section, Post, Comment


class SectionAdmin(admin.ModelAdmin):
    pass


class PostAdmin(admin.ModelAdmin):
    pass


class CommentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Section, SectionAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
