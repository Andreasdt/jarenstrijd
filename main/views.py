from django.shortcuts import render

from .models import Jaar


def counter(request):
    jaren = Jaar.objects.order_by('jaar')
    context = {'jaren': jaren}
    return render(request, 'main/counter.html', context)
