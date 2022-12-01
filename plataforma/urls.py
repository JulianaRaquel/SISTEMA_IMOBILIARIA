from django.urls import path
from .views import home, imovel, agendar_visitas, agendamentos, cancelar_agendamento

urlpatterns = [
    path('home/', home, name="home"),
    path('imovel/<int:id>', imovel, name="imovel"),
    path('agendar_visitas/', agendar_visitas, name="agendar_visitas"),
    path('agendamentos/', agendamentos, name="agendamentos"),
    path('cancelar_agendamento/<str:id>', cancelar_agendamento, name="cancelar_agendamento"),
]