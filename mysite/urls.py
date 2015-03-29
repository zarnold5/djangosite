from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',

	url(r'^polls/', include('polls.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', 'authenticate.views.login_page'),
    url(r'^profile/', 'brother.views.profile'),
    url(r'^logout/', 'authenticate.views.logout_request'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

