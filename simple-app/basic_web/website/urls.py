from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('home/', views.home_page, name='home'),
    path('search_results_page/<str:search_term>/', views.search_results_page, name='search_results_page')
]