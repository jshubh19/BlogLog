
from django.contrib import admin

from django.conf.urls import url,include
from post import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# django-jet urls
from jet_django.urls import jet_urls

app_name=['post','users']


urlpatterns = [
    url(r'^admin/',admin.site.urls),
    #url(r'^posts/',admin.site.urls),

    #post app urls
    url(r'^posts/',include('post.urls',namespace='posts')),
    #users app urls
    url(r'^users/',include('users.urls')),
    #google api urls
    url(r'^accounts/',include('allauth.urls')),

    # django-jet urls
    url(r'^jet_api/', include(jet_urls)),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT )

urlpatterns += staticfiles_urlpatterns()

urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)