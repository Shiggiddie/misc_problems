from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^json-endpoint', views.json_endpoint, name='json-endpoint'),
    url(r'^xml-endpoint', views.xml_endpoint, name='xml-endpoint'),
]
