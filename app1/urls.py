from django.urls import path
from . import views

urlpatterns=[
    path('',views.fnIndex,name='index'),
    path('image_gallery/',views.fnImage_Gallery,name='image_gallery'),
    path('client/',views.fnClient,name='client'),
    path('logIn/',views.fnLogIn,name='logIn'),
    path('garden/',views.fnGarden,name='garden'),
    path('terrace/',views.fnTerrace,name='terrace'),
    path('plants/',views.fnPlants,name='plants'),
    path('test/',views.test,name='test'),
    path('book_online_consultation/',views.fnBook_online_consultation,name='book_online_consultation'),
    path('sign_up/',views.fnSignUp,name='sign_up'),
]