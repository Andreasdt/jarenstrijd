from django.shortcuts import render
from django.db.models import F
from .models import Jaar
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


def counter(request):
    jaren = Jaar.objects.order_by('jaar')
    context = {'jaren': jaren}
    return render(request, 'main/counter.html', context)


@csrf_exempt
def increase_counter(request, jaar, sprong):
    _response = Jaar.objects.filter(jaar=jaar).update(aantal_punten=F('aantal_punten') + sprong)
    response_text = Jaar.objects.filter(jaar=jaar).values('aantal_punten')
    return HttpResponse(response_text)


@csrf_exempt
def decrease_counter(request, jaar, sprong):
    _response = Jaar.objects.filter(jaar=jaar).update(aantal_punten=F('aantal_punten') - sprong)
    response_text = Jaar.objects.filter(jaar=jaar).values('aantal_punten')
    return HttpResponse(response_text)


def barchart(request):
    jaren = Jaar.objects.order_by('jaar')
    context = {'jaren': jaren}
    return render(request, 'main/display.html', context)
