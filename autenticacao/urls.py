from django.urls import path
from .views import cadastro, login, sair, pagina_inicial

urlpatterns = [
    path('', pagina_inicial, name="pagina_inicial"),
    path('cadastro/', cadastro, name="cadastro"),
    path('login/', login, name="login"),
    path('sair/', sair, name="sair")
]