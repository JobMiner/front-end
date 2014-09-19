from django.shortcuts import render
from fetch.models import Creator, Listing

# Create your views here.
def home_page(request):
    context = {
        'creators' : Creator.objects.all(),
        'count': Listing.objects.all().count(),
        'listings': Listing.objects.all()
    }
    return render(request, 'fetch.html', context)