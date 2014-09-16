from django.shortcuts import render
from fetch.models import Creator

# Create your views here.
def home_page(request):
    context = {
        'creators' : Creator.objects.all()
    }
    return render(request, 'home_page.html', context)