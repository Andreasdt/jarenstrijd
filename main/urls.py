from django.urls import path

from . import views

urlpatterns = [
    path('', views.counter, name='counter'),
    path('increase_counter/<int:jaar>/<int:sprong>/', views.increase_counter, name='increase_counter')
]