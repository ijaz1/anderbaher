from django.urls import path
from . import views

urlpatterns=[
    path('employer_home/',views.fnEmployerHome,name='employer_home'),
    path('employer_log_out/',views.fnEmployerLogOut,name='employer_log_out'),
    path('your_profile/',views.fnYour_profile,name='your_profile'),
    path('edit_employer_profile/',views.fnEdit_employer_profile,name='edit_employer_profile'),
    path('work_start/',views.work_start,name='work_start'),
    path('onLoad/',views.onLoad,name='onLoad'),
]