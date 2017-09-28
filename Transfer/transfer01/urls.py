from django.conf.urls import include, url

from . import views

app_name= 'transfer01'
urlpatterns = [ 
    url(r'^home/$', views.home, name='home'),
	url(r'^Transfer/$', views.BulkTransferView.as_view(), name='transfer'),
]