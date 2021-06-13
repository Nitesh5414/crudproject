"""modelform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from modelapp import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_page_view),
    path('add/', views.add_student_view),
    path('show/', views.show_student_view),
    path('update/<int:id>/', views.update_student_view),
    path('delete/<int:id>/', views.delete_student_view),
    path('register/', views.user_register_view),
    path('login/', auth_view.LoginView.as_view(template_name= 'modelapp/login.html')),
    path('logout/', auth_view.LogoutView.as_view()),
]
