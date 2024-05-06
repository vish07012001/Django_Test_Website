from django.urls import path
from . import views

urlpatterns = [
    path('authentication/',views.user_login,name='login'),
    path('forgot/',views.forgot),
    path('register/',views.register),
    path('logout/',views.user_logout,name='logout')
]
