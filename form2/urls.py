"""form2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from app2 import views

urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('religion',views.religion),
#     path('show_religion',views.show_religion),
#     path('edit/<int:id>',views.edit),
#     path('update/<int:id>',views.modify_religion),
    
    # path('religion/create',views.Create.as_view(),name='create_religion'),
    path('admin/', admin.site.urls),
    
    #religion
    path('religion',views.religion),    #main religion form
    path('show_religion',views.show_religion),  #show religions
    path('delete/<int:id>',views.delete_religion),  #delete religion
    path('<pk>/update', views.ReligionUpdateView.as_view()),    #update religion
    re_path(r'^\d+/religion',views.religion),
    
    #title
    path('title',views.title),  #main title form
    path('show_title',views.show_title),    #show title
    path('delete_title/<int:id>',views.delete_title),   #delete title
    path('<pk>/update_title', views.TitleUpdateView.as_view()), #update title
    re_path(r'^\d+/title',views.title),
    
    #caste
    path('caste',views.CasteCreateView.as_view()),  #main caste
    path('show_caste',views.CasteUpdateView.as_view()), #show caste
    path('<pk>/update_caste', views.CasteUpdateView.as_view()), #delete caste
    # re_path(r'^\d+/caste',views.caste),
    path('delete_caste/<int:id>',views.delete_caste),   #update caste
    
    #category
    path('category',views.category),    #main category
    path('show_category',views.show_category),  #show category
    path('<pk>/update_category', views.CategoryUpdateView.as_view()),   #update category
    re_path(r'^\d+/category',views.category),
    path('delete_category/<int:id>',views.delete_category), #delete category
    
    #suplhead
    path('suplhead',views.suplhead),    #main suplhead
    path('<pk>/suplhead', views.SuplHeadUpdateView.as_view()),
    re_path(r'^\d+/suplhead',views.suplhead),
    path('delete_suplhead/<int:id>',views.delete_suplhead), #delete suplhead

    #main dept
    path('MainDept', views.MainDept_create.as_view()),  #main dept
    path('MainDeptShowView', views.MainDeptShowView.as_view()),     #show dept
    # path('<pk>/MainDeptUpdateView', views.MainDeptUpdateView.as_view()),

    #main designation
    path('MainDesignation', views.MainDesignation_create.as_view()),    #main designature
    path('MainDesignationShowView', views.MainDesignationShowView.as_view()),   #show designature
    # path('<pk>/MainDeptUpdateView', views.MainDeptUpdateView.as_view()),

    #staff
    path('Staff', views.Staff_create.as_view()),    #main staff
    path('StaffShowView', views.StaffShowView.as_view()),   #show staff
    # path('<pk>/MainDeptUpdateView', views.MainDeptUpdateView.as_view()),

    #scale
    path('Scale', views.Scale_create.as_view()),    #main scale
    path('ScaleShowView', views.ScaleShowView.as_view()),   #show scale
    # path('<pk>/MainDeptUpdateView', views.MainDeptUpdateView.as_view()),
     
     #typetran
    path('typetran', views.TypeTranCreateView.as_view()),   #mmain typetran
    path('show_typetran', views.TypeTranListView.as_view()),    #show type tran
    
    #appointment
    path('appointment', views.AppointmentCreateView.as_view()), #main appointment
    path('show_appointment', views.AppointmentListView.as_view()),  #show appointment
    
    #undercollege
    path('undercollege', views.UnderCollegeCreateView.as_view()),   #main under college
    path('show_undercollege', views.UnderCollegeListView.as_view()),    #show college

    #crud operations
    path('crud_create',views.crud_create),
    path('createtemp',views.crud_create),
    path('crud_read',views.crud_read),
    path('readtemp',views.crud_read),
    path('crud_update',views.ask_id_for_update),
    path('updateinfotemp',views.ask_id_for_update),
    path('updatetemp',views.crud_update),




]
