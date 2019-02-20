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
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings


urlpatterns = [
    url('', include(('common.urls', 'common'), namespace='common')),
    url('admin/', admin.site.urls),
    url('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    url('blog/', include(('blog.urls', 'blog'), namespace='blog')),
    url('classification/', include(('classification.urls', 'classification'), namespace='classification')),
    url('gallery/', include(('gallery.urls', 'gallery'), namespace='gallery')),
    url('job/', include(('job.urls', 'job'), namespace='job')),
    url('messagebox/', include(('messagebox.urls', 'messagebox'), namespace='messagebox')),
    url('resume/', include(('resume.urls', 'resume'), namespace='resume')),
    url('group/', include(('group.urls', 'group'), namespace='group')),
    # url('organization/', include(('organization.urls', 'organization'), namespace='organization')),
]

urlpatterns += [
    url(r'^search/', include(('haystack.urls', 'haystack'), namespace='search')),
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
