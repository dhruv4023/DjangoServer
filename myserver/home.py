from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
    # return HttpResponse("Server is running")