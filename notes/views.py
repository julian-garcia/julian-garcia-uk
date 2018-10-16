from django.shortcuts import render
from .models import Note

def notes(request):
    notes = Note.objects.order_by('-date_saved')
    categories =[]
    [categories.append(item['category']) for item in Note.objects.order_by('category').values('category') if item['category'] not in categories]

    return render(request, 'notes.html', {'notes': notes, 'categories': categories})

def note(request, id):
    note = Note.objects.get(pk=id)
    return render(request, 'note.html', {'note': note})
