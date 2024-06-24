from .import views
from django.urls import path,include

urlpatterns = [
  
    path("",views.home,name="home"),
    path('register',views.register,name="register"),
    path('login',views.login,name="login"),
    path('new',views.new,name="new"),
    path('logout',views.logout,name="logout"),
    path('getdata',views.getdata,name="getdata"),
]
