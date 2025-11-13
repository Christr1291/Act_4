from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Proveedor
from django.utils import timezone

# ------------------ INICIO ------------------

def inicio(request):
    return render(request, 'inicio.html')

def inicio_computadoras(request):
    contexto = {'hoy': timezone.now()}
    return render(request, 'inicio.html', contexto)

# ------------------ PROVEEDORES ------------------

def ver_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, "proveedor/ver_proveedores.html", {"proveedores": proveedores})

def agregar_proveedor(request):
    if request.method == "POST":
        Proveedor.objects.create(
            nombre=request.POST["nombre"],
            contacto=request.POST.get("contacto", ""),
            telefono=request.POST.get("telefono", ""),
            correo=request.POST.get("correo", ""),
            direccion=request.POST.get("direccion", ""),
            pais=request.POST.get("pais", "")
        )
        return redirect("ver_proveedores")
    return render(request, "proveedor/agregar_proveedor.html")

def actualizar_proveedor(request, id):
    proveedor = get_object_or_404(Proveedor, id=id)
    if request.method == "POST":
        proveedor.nombre = request.POST["nombre"]
        proveedor.contacto = request.POST.get("contacto", "")
        proveedor.telefono = request.POST.get("telefono", "")
        proveedor.correo = request.POST.get("correo", "")
        proveedor.direccion = request.POST.get("direccion", "")
        proveedor.pais = request.POST.get("pais", "")
        proveedor.save()
        return redirect("ver_proveedores")
    return render(request, "proveedor/actualizar_proveedor.html", {"proveedor": proveedor})

def borrar_proveedor(request, id):
    proveedor = get_object_or_404(Proveedor, id=id)
    if request.method == "POST":
        proveedor.delete()
        return redirect("ver_proveedores")
    return render(request, "proveedor/borrar_proveedor.html", {"proveedor": proveedor})

# ------------------ PRODUCTOS ------------------

def ver_productos(request):
    productos = Producto.objects.all()
    return render(request, 'producto/ver_productos.html', {'productos': productos})

def agregar_producto(request):
    if request.method == 'POST':
        prod_id = request.POST.get('id')
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio') or 0
        stock = request.POST.get('stock') or 0
        categoria = request.POST.get('categoria') or 0
        proveedor_id = request.POST.get('proveedor')

        proveedor = None
        if proveedor_id:
            try:
                proveedor = Proveedor.objects.get(id=int(proveedor_id))
            except Proveedor.DoesNotExist:
                proveedor = None

        prod_data = {
            'nombre': nombre,
            'descripcion': descripcion,
            'precio': precio,
            'stock': stock,
            'categoria': categoria,
            'proveedor': proveedor
        }

        if prod_id:
            Producto.objects.update_or_create(id=int(prod_id), defaults=prod_data)
        else:
            Producto.objects.create(**{k: v for k, v in prod_data.items() if v is not None})

        return redirect('ver_productos')
    else:
        proveedores = Proveedor.objects.all()
        return render(request, 'producto/agregar_producto.html', {'proveedores': proveedores})

def actualizar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    proveedores = Proveedor.objects.all()

    if request.method == 'POST':
        producto.nombre = request.POST.get('nombre')
        producto.descripcion = request.POST.get('descripcion')
        producto.precio = request.POST.get('precio') or 0
        producto.stock = request.POST.get('stock') or 0
        producto.categoria = request.POST.get('categoria') or 0

        proveedor_id = request.POST.get('proveedor')
        if proveedor_id:
            try:
                producto.proveedor = Proveedor.objects.get(id=int(proveedor_id))
            except Proveedor.DoesNotExist:
                producto.proveedor = None

        producto.save()
        return redirect('ver_productos')

    return render(request, 'producto/actualizar_producto.html', {'producto': producto, 'proveedores': proveedores})

def borrar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('ver_productos')
    return render(request, 'producto/borrar_producto.html', {'producto': producto})
