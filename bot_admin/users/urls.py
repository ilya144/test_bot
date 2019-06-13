from django.urls import path, include
from .views import setUser

urlpatterns = [
    path('', setUser)
]