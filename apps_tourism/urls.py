from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('save/', views.save),
    path('show/', views.show),
    path('show_log/', views.show_log),
    path('explore/', views.explore),
    path('places/', views.places),
    path('login/', views.login),

]
