from django.conf.urls import patterns, url
urlpatterns = patterns('blog.views',
    url(r'^$', 'accueil'),
    url(r'^article/(?P<id>\d+)/$', 'lire'),
    url(r'^main/$', 'tplbase'),
    url(r'^page/$', 'mapage'),
    url(r'^date/$', 'tpl'),
    url(r'^sexe/$', 'tpls'),
    url(r'^addition/(?P<nombre1>\d+)/(?P<nombre2>\d+)/$', 'addition'),
    url(r'^accueil/$', 'home'),

    #url(r'^article/(\d+)/$', 'view_article'), # Vue d'un article
    url(r'^articles/(?P<year>\d{4})/(?P<month>\d{2})/$', 'list_articles'),
)
