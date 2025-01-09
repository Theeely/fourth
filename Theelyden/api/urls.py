from django.urls import path
from . import views

urlpatterns = [
    path('',views.getRoute,name="gettingroute"),
    path('rooms/',views.getRooms,name="gettingrooms"),
    path('rooms/<int:pk>',views.getRoom,name="gettingroom"),
    path('teluskohmepage',views.getItems,name="getItems"),
]
 