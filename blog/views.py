from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "index.html", context={})


def about(request):
    return render(request, "about.html", context={})


def contact(request):
    return render(request, "contact.html", context={})


def post(request):
    return render(request, "post.html", context={})
