from django.shortcuts import render
from . models import Page

def index_pages(request, pagename):
    pagename = '/' + pagename
    pg = Page.objects.get(permalink=pagename)
    context = {
        'title': pg.title,
        'content': pg.bodytext,
        'last_updated': pg.update_date,
    }
    return render(request, "pages/page.html", context)
