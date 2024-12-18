from django.shortcuts import render
# from django.http import HttpResponse

def index(request):
    context = { 
        'title': 'Home - Main',
        'content': 'Main page of shop - Home',
    }
    return render(request, 'home/index.html', context)

def about(request):
    context = { 
        'title': 'Home - About us',
        'content': 'About us',
        'text_on_page': "Text about why this shop is classic and why the items are so good"
    }
    return render(request, 'home/about.html', context)
