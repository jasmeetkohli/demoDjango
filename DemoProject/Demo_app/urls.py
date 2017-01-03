
from django.conf.urls import include, url 
from django.conf import settings 
from django.conf.urls.static import static 
from  django.conf.urls import url 
from Demo_app import views 

urlpatterns =[

    url(r'^index/', views.Index),
    url(r'^next/', views.firstPage),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)