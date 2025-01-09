from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name="home"),
    path('dbdata',views.index,name="teluskohomepage"),
    path('createaccount',views.createaccount,name="createaccount"),
    path('login',views.login_func,name="login"),
    path('logout',views.logout_func,name="logout")
]
