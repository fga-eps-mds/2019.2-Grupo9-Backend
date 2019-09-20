from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.tela_de_cadastro, name = 'tela_de_cadastro'),
    url(r'^register_multiples/$', views.MultipleRegistrationsViewSet.as_view(), name='set_registration_list'),
]
