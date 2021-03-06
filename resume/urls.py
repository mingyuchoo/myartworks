from django.urls import path

from . import views


app_name = 'resume'

urlpatterns = [
    path('', views.index, name='index'),
    path('basic/list/path(', views.BasicList.as_view(), name='basic.list'),
    path('basic/create/', views.BasicCreate.as_view(), name='basic.create'),
    path('basic/<pk>/', views.BasicDetail.as_view(), name='basic.detail'),
    path('basic/<pk>/update/', views.BasicUpdate.as_view(), name='basic.update'),
    path('basic/<pk>/delete/', views.BasicDelete.as_view(), name='basic.delete'),
    path('contact/list/', views.ContactList.as_view(), name='contact.list'),
    path('contact/create/', views.ContactCreate.as_view(), name='contact.create'),
    path('contact/<pk>/', views.ContactDetail.as_view(), name='contact.detail'),
    path('contact/<pk>/update/', views.ContactUpdate.as_view(), name='contact.update'),
    path('contact/<pk>/delete/', views.ContactDelete.as_view(), name='contact.delete'),
    path('letter/list/', views.LetterList.as_view(), name='letter.list'),
    path('letter/create/', views.LetterCreate.as_view(), name='letter.create'),
    path('letter/<pk>/', views.LetterDetail.as_view(), name='letter.detail'),
    path('letter/<pk>/update/', views.LetterUpdate.as_view(), name='letter.update'),
    path('letter/<pk>/delete/', views.LetterDelete.as_view(), name='letter.delete'),
    path('career/list/', views.CareerList.as_view(), name='career.list'),
    path('career/create/', views.CareerCreate.as_view(), name='career.create'),
    path('career/<pk>/', views.CareerDetail.as_view(), name='career.detail'),
    path('career/<pk>/update/', views.CareerUpdate.as_view(), name='career.update'),
    path('career/<pk>/delete/', views.CareerDelete.as_view(), name='career.delete'),
    path('education/list/', views.EducationList.as_view(), name='education.list'),
    path('education/create/', views.EducationCreate.as_view(), name='education.create'),
    path('education/<pk>/', views.EducationDetail.as_view(), name='education.detail'),
    path('education/<pk>/update/', views.EducationUpdate.as_view(), name='education.update'),
    path('education/<pk>/delete/', views.EducationDelete.as_view(), name='education.delete'),
    path('award/list/', views.AwardList.as_view(), name='award.list'),
    path('award/create/', views.AwardCreate.as_view(), name='award.create'),
    path('award/<pk>/', views.AwardDetail.as_view(), name='award.detail'),
    path('award/<pk>/update/', views.AwardUpdate.as_view(), name='award.update'),
    path('award/<pk>/delete/', views.AwardDelete.as_view(), name='award.delete'),
    path('certificate/list/', views.CertificateList.as_view(), name='certificate.list'),
    path('certificate/create/', views.CertificateCreate.as_view(), name='certificate.create'),
    path('certificate/<pk>/', views.CertificateDetail.as_view(), name='certificate.detail'),
    path('certificate/<pk>/update/', views.CertificateUpdate.as_view(), name='certificate.update'),
    path('certificate/<pk>/delete/', views.CertificateDelete.as_view(), name='certificate.delete'),
    path('language/list/', views.LanguageList.as_view(), name='language.list'),
    path('language/create/', views.LanguageCreate.as_view(), name='language.create'),
    path('language/<pk>/', views.LanguageDetail.as_view(), name='language.detail'),
    path('language/<pk>/update/', views.LanguageUpdate.as_view(), name='language.update'),
    path('language/<pk>/delete/', views.LanguageDelete.as_view(), name='language.delete'),
    path('skill/list/', views.SkillList.as_view(), name='skill.list'),
    path('skill/create/', views.SkillCreate.as_view(), name='skill.create'),
    path('skill/<pk>/', views.SkillDetail.as_view(), name='skill.detail'),
    path('skill/<pk>/update/', views.SkillUpdate.as_view(), name='skill.update'),
    path('skill/<pk>/delete/', views.SkillDelete.as_view(), name='skill.delete'),

]
