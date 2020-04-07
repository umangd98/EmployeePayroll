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
    path('<pk>/update_title', views.TitleUpdateView.as_view()),
    re_path(r'^\d+/title',views.title),
    #caste
    path('caste',views.CasteCreateView.as_view()),
    path('show_caste',views.CasteUpdateView.as_view()),
    path('<pk>/update_caste', views.CasteUpdateView.as_view()),
    # re_path(r'^\d+/caste',views.caste),
    path('delete_caste/<int:id>',views.delete_caste),
    #category
    path('category',views.category),
    path('show_category',views.show_category),
    path('<pk>/update_category', views.CategoryUpdateView.as_view()),
    re_path(r'^\d+/category',views.category),
    path('delete_category/<int:id>',views.delete_category),
    #suplhead
    path('suplhead',views.suplhead),
    path('<pk>/suplhead', views.SuplHeadUpdateView.as_view()),
    re_path(r'^\d+/suplhead',views.suplhead),
    path('delete_suplhead/<int:id>',views.delete_suplhead),

    path('MainDept', views.MainDept_create.as_view()),
    path('MainDeptShowView', views.MainDeptShowView.as_view()),
    # path('<pk>/MainDeptUpdateView', views.MainDeptUpdateView.as_view()),

    path('MainDesignation', views.MainDesignation_create.as_view()),
    path('MainDesignationShowView', views.MainDesignationShowView.as_view()),
    # path('<pk>/MainDeptUpdateView', views.MainDeptUpdateView.as_view()),

    path('Staff', views.Staff_create.as_view()),
    path('StaffShowView', views.StaffShowView.as_view()),
    # path('<pk>/MainDeptUpdateView', views.MainDeptUpdateView.as_view()),

    path('Scale', views.Scale_create.as_view()),
    path('ScaleShowView', views.ScaleShowView.as_view()),
    # path('<pk>/MainDeptUpdateView', views.MainDeptUpdateView.as_view()),
     #typetran
    path('typetran', views.TypeTranCreateView.as_view()),
    path('show_typetran', views.TypeTranListView.as_view()),
    #appointment
    path('appointment', views.AppointmentCreateView.as_view()),
    path('show_appointment', views.AppointmentListView.as_view()),
    #undercollege
    path('undercollege', views.UnderCollegeCreateView.as_view()),
    path('show_undercollege', views.UnderCollegeListView.as_view()),
        #bank
    path('bank', views.BankCreateView.as_view()),
    path('show_bank', views.BankListView.as_view()),
    #city
    path('city', views.CityCreateView.as_view()),
    path('show_city', views.CityListView.as_view()),
    #Subdept
    path('subdept', views.SubDeptCreateView.as_view()),
    path('show_subdept', views.SubDeptListView.as_view()),
    #InstallmentType
    path('install', views.InstallCreateView.as_view()),
    path('show_install', views.InstallListView.as_view()),
    #SubDesignation
    path('subdesig', views.SUBDESIGCreateView.as_view()),
    path('show_subdesig', views.SUBDESIGListView.as_view()),
    #Designature
    path('designature', views.DesignatureCreateView.as_view()),
    path('show_designature', views.DesignatureListView.as_view()),
    
]
