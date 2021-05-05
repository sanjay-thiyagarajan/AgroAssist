from django.urls import path
from predictor.views import *
urlpatterns = [
    path('', home, name='home'),
    path('select/', select, name='select'),
    path('results/', results, name='results')
]
