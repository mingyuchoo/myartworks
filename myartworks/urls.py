"""django_study URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.urls import path
from django.conf import settings
from django.urls import include
from django.contrib import admin


urlpatterns = [
    path('', include(('common.urls', 'common'), namespace='common')),
    path('admin/', admin.site.urls),
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('blog/', include(('blog.urls', 'blog'), namespace='blog')),
    path('classification/', include(('classification.urls', 'classification'), namespace='classification')),
    path('gallery/', include(('gallery.urls', 'gallery'), namespace='gallery')),
    path('job/', include(('job.urls', 'job'), namespace='job')),
    path('messagebox/', include(('messagebox.urls', 'messagebox'), namespace='messagebox')),
    path('resume/', include(('resume.urls', 'resume'), namespace='resume')),
    path('group/', include(('group.urls', 'group'), namespace='group')),
    path('organization/', include(('organization.urls', 'organization'), namespace='organization')),
]

urlpatterns += [
    path('search/', include(('haystack.urls', 'haystack'), namespace='search')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Error page
handler400 = 'common.views.handler400'
handler403 = 'common.views.handler403'
handler404 = 'common.views.handler404'
handler405 = 'common.views.handler405'
handler500 = 'common.views.handler500'
