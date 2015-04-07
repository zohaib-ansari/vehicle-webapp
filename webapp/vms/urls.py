from django.conf.urls import url
from vms import views

urlpatterns = [
        url(r'^$', views.login),
        url('auth/$', views.auth_view),
        url('logout/$', views.logout),
        url('home/$', views.home),
        url('invalid/$', views.login),

        url('report-theft/$', views.report_theft),
        url('submit-theft-report/$', views.report_theft),
        url('your-theft-reports/$', views.user_theft_reports),
        url(r'^(?P<theft_report_id>\d+)/cancel-theft-report/$',views.cancel_theft_report),
]