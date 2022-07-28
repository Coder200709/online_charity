
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.STATIC_URL, ducument_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, ducument_root=settings.MEDIA_ROOT)

