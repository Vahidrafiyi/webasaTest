from django.urls import path, re_path
from .views import *

urlpatterns = [
    re_path(r'sliders/(?P<pk>[0-9]*)', ShowSlider.as_view()),
    # path('add_slider/', AddSlider.as_view()),
]
