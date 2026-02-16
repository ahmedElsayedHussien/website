# marketing/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'marketing/index.html')

def pricing(request):
    return render(request, 'marketing/pricing.html')

def trial(request):
    return render(request, 'marketing/trial.html')

def trial_success(request):
    return render(request, 'marketing/trial_success.html')