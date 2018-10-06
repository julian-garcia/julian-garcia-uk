from django.urls import path
from .views import notes, note

urlpatterns = [
    path('', notes, name='notes'),
    path('note/<id>', note, name='note'),
]
