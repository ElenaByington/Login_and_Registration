from django.urls import path
from . import views

# NO LEADING SLASHES
urlpatterns = [
    path('', views.index),
    path('register',views.register),
    path('login',views.login),
    path('success',views.success),
    path('logout',views.logout),
]
