from django.contrib import admin
from django.urls import path
#from core import views
#from core import AdminViews
from django.conf.urls.static import static
from django.urls import include

from Saturno import settings



urlpatterns = [
    
    path('admin/', admin.site.urls),
   
    path('',include('core.adminurls')),
    path('admindashboard/',include('core.adminurls')),

    path('accounts/', include('allauth.urls')),


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)