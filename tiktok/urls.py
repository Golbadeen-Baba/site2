from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_view, name='landing'),
    path('questionnair/', views.tiktok_questionnaire_view, name='questions'),
    path('thank-you/', views.thank_you_view, name='thank_you'),
]