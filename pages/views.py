from django.shortcuts import render
from .models import Page


def listfun(request):
    list1 = Page.objects.all()


    context = {
        "list":list1
        }
    return render(request, 'list.html', context)

def detailfun(request,page_id):
    detail1 = Page.objects.get(id=page_id)
    

    context = {
        "detail":detail1
        }
    return render(request, 'detail.html', context)