"""CapStrongFinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from sampolApp import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'sampolApp'

urlpatterns = [
    #VIEWS
    path('index',views.MyIndexView2.as_view(), name="my_index_view2"),
    path('admin/', admin.site.urls),
    path('', views.MyIndexView.as_view(), name="my_index_view"),
    #path('register', views.RegisterView.as_view(), name="my_index_view"),
    
    #DASHBOARDS
    path('dashboard/', views.dashboard, name="Dashboard_View"),
    path('dash', views.UserDashboardView1.as_view(), name="my_dash_view"),
    path('UserDashboard/',views.UserDashboard, name="UserDashboard_View"),
    path('RegistrationDashboard/',views.RegistrationDashboard, name="RegistrationDashboard_View"),

    #EDIT
    path('EditUser/<int:id>',views.editUser),
    path('EditRegistrations/<int:id>',views.editRegistration),
    #UPDATE
    path('UpdateUser/<int:id>',views.updateUser),
    path('UpdateRegistrations/<int:id>',views.updateRegistration),
    #DELETE
    path('DeleteUser/<int:id>',views.deleteUser),
    path('DeleteRegistrations/<int:id>',views.deleteRegistrations),

    path('login', views.login, name="my_login_view"),
    path('signup/',views.SignupView.as_view(), name="SignupView"),

    path('qr/',views.qr),

    path('getQr/<int:id>',views.GetRegistrationQr),


]

urlpatterns += staticfiles_urlpatterns()