from django.urls import path
from . import views
urlpatterns = [
    path( '',views.home,name="home" ),
    #path('createaccount/',views.createaccount,name="creatingaccount"),
    #path('logintomyaccount/',views.login,name="login"),
    #path('logintomyaccount/verify/',views.verify,name="verification"),
]


