from django.urls import path
from . import views


urlpatterns = [

    path('',views.Home,name='index'),
    path('delete/<int:id>',views.Delete_record,name='delete'),
    path('<int:id>',views.Update_Record,name='update'),
    path('sign_up/', views.sign_up,name='sign_up'),
    path('sign_in/', views.sign_in,name='login'),
    path('log_out/', views.log_out,name='log_out'),
    
]