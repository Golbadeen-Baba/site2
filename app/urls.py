from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_view, name='landing'),
    path('form/', views.form_view, name='form'),
    path('questionnaire/', views.model_questionnaire_view, name='questionnaire'),
    path('thank-you/', views.thank_you_view, name='thank-you'),
]