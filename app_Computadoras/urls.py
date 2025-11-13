from django.urls import path
from . import views

urlpatterns = [
    # PRODUCTOS
    path('', views.inicio, name='inicio'),
    path('productos/agregar/', views.agregar_producto, name='agregar_producto'),
    path('productos/ver/', views.ver_productos, name='ver_productos'),
    path('', views.inicio_computadoras, name="inicio_computadoras"),
    path('productos/', views.ver_productos, name="ver_productos"),
    path('productos/agregar/', views.agregar_producto, name="agregar_producto"),
    path('productos/actualizar/<int:id>/', views.actualizar_producto, name="actualizar_producto"),
    path('productos/borrar/<int:id>/', views.borrar_producto, name="borrar_producto"),

    # PROVEEDORES
    path('proveedores/', views.ver_proveedores, name="ver_proveedores"),
    path('proveedores/agregar/', views.agregar_proveedor, name="agregar_proveedor"),
    path('proveedores/actualizar/<int:id>/', views.actualizar_proveedor, name="actualizar_proveedor"),
    path('proveedores/borrar/<int:id>/', views.borrar_proveedor, name="borrar_proveedor"),
]
