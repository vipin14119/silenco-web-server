from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.get_data, name='get_data'),
    url(r'^post/$', views.post_record_bundle, name='post_data'),
    url(r'^get_csrf/$', views.get_csrf_token, name='get_csrf'),
    url(r'^login/$', views.login, name='login'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^locations/$', views.get_locations, name='get_locations'),
    url(r'^new_location/$', views.post_location, name='post_location'),
]
