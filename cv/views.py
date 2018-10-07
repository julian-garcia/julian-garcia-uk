from django.shortcuts import render
from .models import CVSection

def cv(request):
    headline = CVSection.objects.all().order_by('section_sequence','-date_saved')[:1].get()
    sections = CVSection.objects.all().order_by('section_sequence','-date_saved')[1:]
    return render(request, 'cv.html', {'headline': headline, 'sections': sections})
