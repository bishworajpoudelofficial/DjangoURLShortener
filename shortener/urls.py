from django.urls import path 
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('<str:shorturl>/',views.redirect_site, name="redirect-url")
]
