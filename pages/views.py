from django.shortcuts import render

def index_pages(request):
    return render(request, "pages/page.html")
