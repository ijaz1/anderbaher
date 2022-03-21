from unicodedata import name
from django.urls import path
from . import views

urlpatterns=[
    path('',views.fnAdmin_Panel,name='admin_panel'),
    path('admin_log_out',views.fnLogout,name='admin_log_out'),
    path('admin_manage_website/',views.fnManage_Website,name='admin_manage_website'),
    path('edit_contact/',views.fnEdit_contact,name='edit_contact'),
    path('editContact/',views.fnEditContact,name='editContact'),
    path('upload_category_photo/',views.fnUpload_category_photo,name='upload_category_photo'),
    path('edit_photo/',views.fnEdit_photo,name='edit_photo'),
    path('update_edit_photo/',views.fnUpdate_Edit_photo,name='update_edit_photo'),
    path('delete_photo/<id>',views.fnDelete_photo,name='delete_photo'),
    path('view_deleted_photo/',views.view_deleted_photo,name='view_deleted_photo'),
    path('recover_deleted_photo/',views.fnRecover_deleted_photo,name='recover_deleted_photo'),
    path('estimated_client/',views.fnEstimated_client,name='estimated_client'),
    path('checkout/<id>',views.fnCheckOut,name='checkout'),
    path('checked_clients/',views.fnChecked_clients,name='checked_clients'),
    path('view_employer/',views.fnView_employer,name='view_employer'),
    path('add_employer/',views.fnAdd_employer,name='add_employer'),
    path('adding_employer_details/',views.fnAdding_employer_details,name='adding_employer_details'),
    path('edit_employer_admin/',views.fnEdit_employer_admin,name='edit_employer_admin'),
    path('view_edit_employer_admin/<id>',views.fnView_edit_employer_admin,name='view_edit_employer_admin'),
    path('update_employer_admin/',views.fnUpdate_employer_admin,name='update_employer_admin'),
    path('terminate_employer/<id>',views.fnTerminate_employer,name='terminate_employer'),
    path('view_terminated_employees/',views.fnView_terminated_employees,name='view_terminated_employees'),
    path('edit_terminated_employer_admin/<id>',views.fnEdit_terminated_employer_admin,name='edit_terminated_employer_admin'),
    path('view_terminated_employer_bank/',views.fnView_terminated_employer_bank,name='view_terminated_employer_bank'),    
    path('view_employer_bank/',views.fnView_employer_bank,name='view_employer_bank'),    
    path('assign_work/',views.assign_work,name='assign_work'),    
    path('work_assigning/',views.work_assigning,name='work_assigning'),    
]