from django.shortcuts import render
from .models import Note

def notes(request):
    notes = Note.objects.all().order_by('-date_saved')
    return render(request, 'notes.html', {'notes': notes})

def note(request, id):
    note = Note.objects.get(pk=id)
    return render(request, 'note.html', {'note': note})
