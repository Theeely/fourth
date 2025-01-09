from django.urls import path
from . import views

urlpatterns = [
    path( '',views.home,name="home" ), 
    path( '<int:pk>',views.room,name="room" ), 
    path( 'createroom',views.createroom,name="createroom" ), 
    path( 'updateroom/<int:pk>',views.updateroom,name="updateroom" ), 
    path( 'deleteroom/<int:pk>',views.deleteroom,name="deleteroom" ),
    path('deletemessage/<int:pk>',views.deletemessage,name="deletemessage" )

]


