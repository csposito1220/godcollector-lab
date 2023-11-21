from django.urls import path
from . import views
	
urlpatterns = [
	path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('mythologies/', views.mythologies_index, name='index'),
    path('mythologies/detail/<int:mythology_id>/', views.mythologies_detail, name='detail'),
    path('mythologies/create/', views.MythologyCreate.as_view(), name='mythology_create'),
    path('mythologies/<int:pk>/update/', views.MythologyUpdate.as_view(), name='mythology_update'),
  	path('mythologies/<int:pk>/delete/', views.MythologyDelete.as_view(), name='mythology_delete'),
  	path('gods/', views.GodList.as_view(), name='gods_index'),
  	path('gods/<int:pk>/', views.GodDetail.as_view(), name='gods_detail'),
  	path('gods/create/', views.GodCreate.as_view(), name='gods_create'),
  	path('gods/<int:pk>/update/', views.GodUpdate.as_view(), name='gods_update'),
  	path('gods/<int:pk>/delete/', views.GodDelete.as_view(), name='gods_delete'),
  	path('mythologies/<int:mythology_id>/assoc_god/<int:god_id>/', views.assoc_god, name='assoc_god'),
  	path('mythologies/<int:mythology_id>/remove_god/<int:god_id>/', views.remove_god, name='remove_god')

 ]