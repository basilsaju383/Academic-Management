from django.urls import path,include
from .import views


urlpatterns = [
   path('empl_mng/', views.empl_mng,name="empl_mng"),
]