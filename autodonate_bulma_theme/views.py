from django.shortcuts import render


def index(request):
    return render(request, "bulma/pages/index.html")
