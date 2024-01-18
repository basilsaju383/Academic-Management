from django.urls import path,include
from .import views


urlpatterns = [
   path('empl_mng/', views.empl_mng,name="empl_mng"),
   path('empl_sub_list/', views.empl_sub_list,name="empl_sub_list"),
   path('sub_listss/', views.sub_listss,name="sub_listss"),
]