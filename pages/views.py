from django.http import HttpResponse

def index_pages(request):
    return HttpResponse("<h1 style='text-align:center;'>Site de GLAASRI : Application pages</h1>")
