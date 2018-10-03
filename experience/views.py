from django.shortcuts import render
from .models import Experience

def experience(request):
    experience = Experience.objects.all().order_by('-start_date')

    return render(request, 'experience.html', {'experience': experience})
