from django.shortcuts import render
from .models import SliderObject

def main_page(request):
    context = {
        'slider_objects': SliderObject.objects.all(),
    }
    return render(request, 'nasa/main_page.html', context = context)
