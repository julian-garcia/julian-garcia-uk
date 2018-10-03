from django.urls import path
from .views import experience

urlpatterns = [
    path('', experience, name='experience'),
]
