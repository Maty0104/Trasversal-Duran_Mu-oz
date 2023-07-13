from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [

    path('', views.listar_productos, name='listar_productos'),
    path('crear/', views.crear_producto, name='crear_producto'),
    path('actualizar/<int:pk>/', views.actualizar_producto, name='actualizar_producto'),
    path('eliminar/<int:pk>/', views.eliminar_producto, name='eliminar_producto'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('admin/', admin.site.urls),
    path('inicio/', views.inicio, name='inicio'),
    path('obras/', views.obras, name='obras'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('formulario/', views.formulario, name='formulario'),
    path('api/', views.api, name='api'),
    path('politicasdeprivacidad/', views.politicasdeprivacidad, name='politicasdeprivacidad'),
    path('politicasdedevolucion/', views.politicasdedevolucion, name='politicasdedevolucion'),
    path('politicasdeenvio/', views.politicasdeenvio, name='politicasdeenvio'),
    path('terminosyservicios/', views.terminosyservicios, name='terminosyservicios'),
    
    path('tienda/',views.tienda,name='tienda'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
