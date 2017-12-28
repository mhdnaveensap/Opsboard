#############################################################################
# IMPORT STATEMENTS                                                         #
#############################################################################

from django.conf.urls import url,include
from commonpage.views import *
from django.contrib.auth import views as auth_views
from django.conf.urls import handler404, handler500
from django.contrib.staticfiles.urls import static
from web import settings
from django.contrib.auth.views import (
    password_reset,
    password_reset_done,
    password_reset_confirm,
    password_reset_complete
)

#############################################################################
#URL Patterns                                                               #
#############################################################################
app_name = 'userpg'

urlpatterns = [
                url(r'^login/$', login,name="login"),
                url(r'^logout/$', auth_views.logout,{'next_page': '/user/login/'},name="logout"),
                url(r'^register/', register, name='register'),
                # url(r'^$', home,name="home"),
                url(r'^testing/$', test_view),
                url(r'^teamdetails/$',update_team, name='update_team'),
                url(r'^profile/$', view_profile, name='view_profile'),
                url(r'^reset-password/$', password_reset, {'template_name': 'registration/reset-password.html'}),
                url(r'^reset-password/done/$', password_reset_done,{'template_name': 'registration/reset-password-done.html'}, name='password_reset_done'),
                url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, name='password_reset_confirm'),
                url(r'^reset-password/complete/$', password_reset_complete, name='password_reset_complete'),

              ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = handler404_view
handler500 = handler500_view
