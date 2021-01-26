from django.urls import include, path
from rest_framework import routers
from myapi.views import EspecialidadeViewSet, ClienteViewSet, MedicoViewSet, ClinicaViewSet,ConsultaViewSet

api_router = routers.DefaultRouter()
api_router.register(r"cliente", ClienteViewSet)
api_router.register(r"medico", MedicoViewSet)
api_router.register(r"clinica", ClinicaViewSet)
api_router.register(r"consulta", ConsultaViewSet)
api_router.register(r"especialidade", EspecialidadeViewSet)


urlpatterns = [
    path("api/", include(api_router.urls)),
]