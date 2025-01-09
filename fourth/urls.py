
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.mainpage,name="main"),
    path('kirai/',include('kirai.urls'), name="kirai"),
    path('telusko/',include('teluskolearn.urls'),name="telusko"),
    path('theelyden/',include('Theelyden.urls'),name="theelyden"),
    path('dennis/',include('Dennis.urls'),name="dennis"),
    path('api/',include('Theelyden.api.urls'),name="api-requester")
]

urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)