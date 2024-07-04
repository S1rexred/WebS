from django.contrib import admin
from django.urls import path, include
from product.views import menu, index, phone, than
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('menu/', menu, name='menu'),
    path('phone/', phone, name='phone'),
    path('phone/than/',than, name='than'),
   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)