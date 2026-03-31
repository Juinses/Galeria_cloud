from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # 1. El panel de administración
    path('admin/', admin.site.urls),

    # 2. El sistema de autenticación nativo de Django (Login/Logout)
    path('accounts/', include('django.contrib.auth.urls')),

    # 3. Incluimos las URLs de tu aplicación galería
    path('', include('galeria.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)