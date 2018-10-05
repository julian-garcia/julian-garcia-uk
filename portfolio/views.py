from django.shortcuts import render
from .models import PortfolioItem

def portfolio(request):
    portfolio = PortfolioItem.objects.all().order_by('title')
    return render(request, 'portfolio.html', {'portfolio': portfolio})
