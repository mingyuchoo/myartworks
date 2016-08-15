from django.contrib import admin

from .models import (Basic,
                     Contact,
                     Letter,
                     Career,
                     Education,
                     Award,
                     Certificate,
                     Language,
                     Skill
                     )


class BasicAdmin(admin.ModelAdmin):
    pass


class ContactAdmin(admin.ModelAdmin):
    pass


class LetterAdmin(admin.ModelAdmin):
    pass


class CareerAdmin(admin.ModelAdmin):
    pass


class EducationAdmin(admin.ModelAdmin):
    pass


class AwardAdmin(admin.ModelAdmin):
    pass


class CertificateAdmin(admin.ModelAdmin):
    pass


class LanguageAdmin(admin.ModelAdmin):
    pass


class SkillAdmin(admin.ModelAdmin):
    pass


admin.site.register(Basic, BasicAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Letter, LetterAdmin)
admin.site.register(Career, CareerAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Award, AwardAdmin)
admin.site.register(Certificate, CertificateAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Skill, SkillAdmin)
