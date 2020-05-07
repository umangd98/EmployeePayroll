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
    path('religion',views.religion),
    path('show_religion',views.show_religion),
    path('delete/<int:id>',views.delete_religion),
    path('<pk>/update', views.ReligionUpdateView.as_view()),
    re_path(r'^\d+/religion',views.religion),
    #title
    path('title',views.title),
    path('show_title',views.show_title),
    path('delete_title/<int:id>',views.delete_title),
    path('<pk>/update_title', views.TitleUpdateView.as_view(),name='title_update'),
    re_path(r'^\d+/title',views.title),
    #caste
    path('caste',views.CasteCreateView.as_view()),
    path('show_caste',views.CasteListView.as_view()),
    path('<pk>/update_caste', views.CasteUpdateView.as_view()),
    re_path(r'^\d+/show_caste',views.CasteListView.as_view()),
    path('delete_caste/<int:id>',views.delete_caste),
    #category
    path('category',views.category),
    path('show_category',views.show_category),
    path('<pk>/update_category', views.CategoryUpdateView.as_view()),
    re_path(r'^\d+/category',views.category),
    path('delete_category/<int:id>',views.delete_category),
    #suplhead
    # path('suplhead',views.suplhead),
    # path('<pk>/suplhead', views.SuplHeadUpdateView.as_view()),
    # re_path(r'^\d+/suplhead',views.suplhead),
    # path('delete_suplhead/<int:id>',views.delete_suplhead),
    path('suplhead', views.SuplHeadCreateView.as_view()),
    path('show_suplhead', views.SuplHeadListView.as_view()),
    path('<pk>/update_suplhead', views.SuplHeadUpdateView.as_view()),
    #re_path(r'^\d+/show_suplhead',views.SuplHeadUpdateView.as_view()),
    #path('delete_suplhead/<int:id>',views.SuplHeadDeleteView),
    path('<pk>/delete_suplhead', views.SuplHeadDeleteView.as_view()),
    #path('delete_suplhead', views.SuplHeadDeleteView.as_view()),
    #Maindept
    path('MainDept', views.MainDept_create.as_view()),
    path('MainDeptShowView', views.MainDeptShowView.as_view()),
    path('<pk>/update_maindept', views.MainDeptUpdateView.as_view()),
    re_path(r'^\d+/MainDeptShowView',views.MainDeptShowView.as_view()),
    path('delete_maindept/<int:id>',views.delete_maindept),
    # path('<pk>/MainDeptUpdateView', views.MainDeptUpdateView.as_view()),
    #MainDesignation
    path('MainDesignation', views.MainDesignation_create.as_view()),
    path('MainDesignationShowView', views.MainDesignationShowView.as_view()),
    path('<pk>/update_maindesig', views.MainDesignationUpdateView.as_view()),
    re_path(r'^\d+/MainDesignationShowView',views.MainDesignationShowView.as_view()),
    path('delete_maindesig/<int:id>',views.delete_maindesig),
    #Staff
    path('Staff', views.Staff_create.as_view()),
    path('StaffShowView', views.StaffShowView.as_view()),
    path('<pk>/update_staff', views.StaffUpdateView.as_view()),
    re_path(r'^\d+/StaffShowView',views.StaffShowView.as_view()),
    path('delete_staff/<int:id>',views.delete_staff),
    #Scale
    path('Scale', views.Scale_create.as_view()),
    path('ScaleShowView', views.ScaleShowView.as_view()),
    path('<pk>/update_scale', views.ScaleUpdateView.as_view()),
    re_path(r'^\d+/ScaleShowView',views.ScaleShowView.as_view()),
    path('delete_scale/<int:id>',views.delete_scale),
    #typetran
    path('typetran', views.TypeTranCreateView.as_view()),
    path('show_typetran', views.TypeTranListView.as_view()),

    path('<pk>/update_typetran', views.TypeTranUpdateView.as_view()),
    path('<pk>/delete_typetran', views.TypeTranDeleteView.as_view()),
    #appointment
    path('appointment', views.AppointmentCreateView.as_view()),
    path('show_appointment', views.AppointmentListView.as_view()),
    path('<pk>/update_appointment', views.AppointmentUpdateView.as_view()),
    re_path(r'^\d+/show_appointment',views.AppointmentListView.as_view()),
    path('delete_appointment/<int:id>',views.delete_appointment),
    #undercollege
    path('undercollege', views.UnderCollegeCreateView.as_view()),
    path('<pk>/update_undercollege', views.UnderCollegeUpdateView.as_view()),
    path('show_undercollege', views.UnderCollegeListView.as_view()),
    re_path(r'^\d+/show_undercollege',views.UnderCollegeListView.as_view()),
    path('delete_undercollege/<int:id>',views.delete_under),
    #bank
    path('bank', views.BankCreateView.as_view()),
    path('show_bank', views.BankListView.as_view()),

    path('<pk>/update_bank', views.BankUpdateView.as_view()),
    path('<pk>/delete_bank', views.BankDeleteView.as_view()),
    #city
    path('city', views.CityCreateView.as_view()),
    path('show_city', views.CityListView.as_view()),

    path('<pk>/update_city', views.CityUpdateView.as_view()),
    path('<pk>/delete_city', views.CityDeleteView.as_view()),
    #Subdept
    path('subdept', views.SubDeptCreateView.as_view()),
    path('show_subdept', views.SubDeptListView.as_view()),
    path('<pk>/update_subdept', views.SubDeptUpdateView.as_view()),
    re_path(r'^\d+/show_subdept',views.SubDeptListView.as_view()),
    path('delete_subdept/<int:id>',views.delete_subdept),
    #InstallmentType
    path('install', views.InstallCreateView.as_view()),
    path('show_install', views.InstallListView.as_view()),

    path('<pk>/update_install', views.InstallUpdateView.as_view()),
    path('<pk>/delete_install', views.InstallDeleteView.as_view()),
    #SubDesignation
    path('subdesig', views.SUBDESIGCreateView.as_view()),
    path('show_subdesig', views.SUBDESIGListView.as_view()),
    path('<pk>/update_subdesig', views.SUBDESIGUpdateView.as_view()),
    re_path(r'^\d+/show_subdesig',views.SUBDESIGListView.as_view()),
    path('delete_subdesig/<int:id>',views.delete_subdesig),
    
    #crud operations
    path('crud_create',views.crud_create),
    path('createtemp',views.crud_create),
    path('crud_read',views.crud_read),
    path('readtemp',views.crud_read),
    path('crud_update',views.ask_id_for_update),
    path('updateinfotemp',views.ask_id_for_update),
    path('updatetemp',views.crud_update),
    
]
