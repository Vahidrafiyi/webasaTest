from django.urls import path
from .views import *

urlpatterns = [
    path('slider/', ShowSlider.as_view()),
    # path('add_slider/', AddSlider.as_view()),
]
