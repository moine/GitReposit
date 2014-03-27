from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangoTest.views.home', name='home'),
    url(r'^grappelli/',include('grappelli.urls')),
    url(r'^blog/', include('blog.urls')),# pour blog
    #url(r'^accueil/$', 'blog.views.home'),
    url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += staticfiles_urlpatterns()
