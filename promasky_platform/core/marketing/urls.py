from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pricing/', views.pricing, name='pricing'),
    path('trial/', views.trial, name='trial'),
    path('trial/success/', views.trial_success, name='trial_success'),
    path('features/', views.features, name='features'),
    path('features/finance/', views.feature_finance, name='feature_finance'),
]