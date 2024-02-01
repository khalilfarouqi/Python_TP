from django.http import HttpResponse

def index_projet(request):
    return HttpResponse("<h1 style='text-align:center;'>Bienvenue au site de LP GLAASRI</h1>")