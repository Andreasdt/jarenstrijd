from django.urls import path

from . import views

urlpatterns = [
    path('', views.counter, name='counter'),
    path('increase_counter/<int:jaar>/<int:sprong>/', views.increase_counter, name='increase_counter'),
    path('decrease_counter/<int:jaar>/<int:sprong>/', views.decrease_counter, name='decrease_counter')
]