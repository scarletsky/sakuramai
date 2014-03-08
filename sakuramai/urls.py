from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    'white.views',
    # Examples:
    # url(r'^$', 'sakuramai.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'index'),
    url(r'^(?P<year>\d{4})/$', 'year'),
    url(r'^(?P<year>\d{4})/info/$', 'info'),
    url(r'^(?P<year>\d{4})/signup/$', 'signup'),
    url(r'^(?P<year>\d{4})/participants/$', 'participants'),
    url(r'^(?P<year>\d{4})/schedule/$', 'schedule'),
    url(r'^(?P<year>\d{4})/(?P<day>\d{2}|sp1|sp2|fin)/$', 'display'),
    url(r'^(?P<year>\d{4})/result/$', 'result'),

    url(r'^vote-ajax/$', 'vote_ajax'),
    url(r'^signup-ajax/$', 'signup_ajax'),
    url(r'^check-author-ajax/$', 'check_author'),

    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^wd/admin/', include(admin.site.urls)),
)

handler404 = 'white.views.custom_404'
# handler500 = 'white.views.custom_500'
