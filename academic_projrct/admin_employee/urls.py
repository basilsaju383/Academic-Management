from django.urls import path,include
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
   path('empl_mng/', views.empl_mng,name="empl_mng"),
   path('empl_sub_list/', views.empl_sub_list,name="empl_sub_list"),
   path('sub_listss/', views.sub_listss,name="sub_listss"),
   path('get_employee_details/', views.get_employee_details,name="get_employee_details"),
   path('fetch_employee/<int:item_id>/', views.fetch_employee,name="fetch_employee"),
   path('delete_empl/', views.delete_empl,name="delete_empl"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)