from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('ajouter', views.ajouter, name='ajouter'),
    path('editer/<list_id>', views.editer, name='editer'),
    path('effacer/<list_id>', views.effacer, name='effacer'), 
    path('search_nom', views.search_nom, name='search-nom')   
]
