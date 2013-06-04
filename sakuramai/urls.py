from django.conf.urls import patterns, include, url
from skm.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', Index, name="skm_index"),
    url(r'^introduce/$', Introduce, name='skm_introduce'),
    url(r'^signup/$', WhiteDaySignup, name='skm_white_day_signup'),
    url(r'^participants/$', Participants, name='skm_participants'),
    url(r'^mads/$', Mads, name="skm_mads"),
    url(r'^staff/$', SkmStaff, name="skm_staff"),
    url(r'^2013/$', Schedule, name="skm_white_day_schedule"),
    url(r'^2013/(?P<day>(\d{1,2})|sp1|sp2)/$', Display, name="skm_white_day_display"),
    url(r'^result/$', Result, name="skm_white_day_result"),
    # Examples:
    # url(r'^$', 'sakuramai.views.home', name='home'),
    # url(r'^sakuramai/', include('sakuramai.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^cron/countday/$', CountDay),
    url(r'^cron/syncvotes/$', SyncVotes),
    url(r'^category/$', Category),
)
