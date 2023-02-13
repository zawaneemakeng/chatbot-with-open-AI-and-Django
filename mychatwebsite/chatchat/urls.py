from django.urls import path
from .views import *

urlpatterns = [
    path('', Qa, name='qa'),

]
