"""apiconsultas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path
from rest_framework import routers
from myapi.views import ClienteViewSet, MedicoViewSet, ClinicaViewSet,ConsultaViewSet

api_router = routers.DefaultRouter()
api_router.register(r"cliente", ClienteViewSet)
api_router.register(r"medico", MedicoViewSet)
api_router.register(r"clinica", ClinicaViewSet)
api_router.register(r"consulta", ConsultaViewSet)


urlpatterns = [
    path("api/", include(api_router.urls)),
]