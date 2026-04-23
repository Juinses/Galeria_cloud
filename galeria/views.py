from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import GaleriaFotos
from .forms import ImagenForm
from django.http import HttpResponse

@login_required
def home(request):
    if request.method == 'POST' and request.user.is_staff:
        form = ImagenForm(request.POST, request.FILES)
        if form.is_valid():
            # Creamos la instancia sin guardar todavía
            nueva_imagen = form.save(commit=False)
            
            # Si se subió un archivo, lo procesamos
            if 'archivo' in request.FILES:
                archivo = request.FILES['archivo']
                # Guardamos el nombre del archivo en el campo 'foto' de la BD
                nueva_imagen.foto = archivo.name 
                # NOTA: Aquí también deberías tener lógica para subir el archivo a S3 usando boto3
            
            nueva_imagen.save() # Ahora sí guardamos en RDS
            return redirect('home')
    else:
        form = ImagenForm()

    # IMPORTANTE: Cambiamos 'Imagen' por 'GaleriaFotos'
    imagenes = GaleriaFotos.objects.all()
    
    return render(request, 'galeria/home.html', {
        'imagenes': imagenes,
        'form': form
    })

def health(request):
    return HttpResponse("ok", status=200)
