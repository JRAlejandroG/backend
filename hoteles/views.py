from django.shortcuts import render

def home(request):
    return render(request, 'hoteles/index.html')

def pagina_no_encontrada(request, exception):
    return render(request, 'hoteles/404.html', status=404)