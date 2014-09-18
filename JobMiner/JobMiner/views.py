from django.shortcuts import render
from fetch.models import Creator

def home(request):
    context = {
        'creators' : Creator.objects.all()
    }
    return render(request, 'home_page.html', context)