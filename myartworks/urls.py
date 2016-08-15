"""myartworks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^', include('common.urls', namespace='common')),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^classification/', include('classification.urls', namespace='classification')),
    url(r'^gallery/', include('gallery.urls', namespace='gallery')),
    url(r'^job/', include('job.urls', namespace='job')),
    url(r'^resume/', include('resume.urls', namespace='resume')),
    url(r'^group/', include('group.urls', namespace='group')),
    url(r'^organization/', include('organization.urls', namespace='organization')),
    url(r'^messagebox/', include('messagebox.urls', namespace='messagebox')),
    url(r'^blog/', include('blog.urls', namespace='blog')),
]

urlpatterns += [
    url(r'^search/', include('haystack.urls', namespace='search')),
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
