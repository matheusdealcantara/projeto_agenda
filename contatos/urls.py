from django.urls import path

from accounts import views as v

from . import views

urlpatterns = [
    path('logout/', v.logout, name='logout'),
    path('login/', v.login, name='login'),
    path('dashboard/', v.dashboard, name='dashboard'),
    path('', views.index, name='index'),
    path('busca/', views.busca, name='busca'),
    path('<int:contato_id>', views.ver_contato, name='ver_contato'),
]
