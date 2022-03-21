from django.urls import path
from . import views

urlpatterns=[
    path('client_home/',views.fnClientHome,name='client_home'),
]