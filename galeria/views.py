from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Imagen
from .forms import ImagenForm
from django.http import HttpResponse

@login_required
def home(request):
    if request.method == 'POST' and request.user.is_staff: # Solo admins suben fotos
        form = ImagenForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ImagenForm()

    imagenes = Imagen.objects.all()
    return render(request, 'galeria/home.html', {
        'imagenes': imagenes,
        'form': form
    })


def health(request):
    return HttpResponse("ok", status=200)
