from django.shortcuts import render

def index_pages(request):
    return render(request, "page/page.html")
