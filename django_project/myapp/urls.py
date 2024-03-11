from django.urls import path
from . import views




urlpatterns = [
    path('', views.home, name='home'),
    path('add_record/', views.add_record , name='add'),
    path('list/',views.animal_listing,name='list'),
    path('viewrecord/<int:pk>',views.viewRecord,name='viewrecord'),
    path('logout/',views.logout_user,name='logout'),
    path('register/',views.register_user,name='register'),
    path('delete/<int:pk>',views.delete_record,name='delete'),
    path('login/',views.login_user,name='login'),
    path('bootstrap/',views.bootstrap_list,name='boot'),
    path('update/<int:pk>',views.update_record,name='update')

   

    ]