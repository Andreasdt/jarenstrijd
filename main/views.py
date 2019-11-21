from django.shortcuts import render
from django.db.models import F
from .models import Jaar
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


def counter(request):
    jaren = Jaar.objects.order_by('jaar')
    context = {'jaren': jaren}
    return render(request, 'main/counter.html', context)


@csrf_exempt
def increase_counter(request, jaar, sprong):
    _response = Jaar.objects.filter(jaar=jaar).update(aantal_punten=F('aantal_punten') + sprong)
    return JsonResponse
