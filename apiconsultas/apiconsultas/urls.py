from django.contrib import admin
from django.urls import path
from clientes import views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/clientes/$', views.clientes_list),
    url(r'^api/clientes/(?P<pk>[0-9]+)$', views.clientes_detail),
]
