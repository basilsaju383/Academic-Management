from django.urls import path,include
from .import views


urlpatterns = [
    path('admin_master_desig_mng/', views.admin_master_desig_mng,name="admin_master_desig_mng"),
    path('admin_master_dpt_mng/', views.admin_master_dpt_mng,name="admin_master_dpt_mng"),
    path('admin_master_qual_mng/', views.admin_master_qual_mng,name="admin_master_qual_mng"),
    path('cls_mng/', views.cls_mng,name="cls_mng"),
    path('division_mng/', views.division_mng,name="division_mng"),
    path('employee_category/', views.employee_category,name="employee_category"),
    path('division_mng_edt/', views.division_mng_edt,name="division_mng_edt"),
    path('division_mng_updt/', views.division_mng_updt,name="division_mng_updt"),
    
]