from django.shortcuts import render, redirect
from .forms import ModelApplicantForm
from .models import ModelQuestionnaire, ModelApplicant
from django.contrib import messages

# Create your views here.

def landing_view(request):
    return render(request, 'app/landing.html')


def form_view(request):
    if request.method == 'POST':
        form = ModelApplicantForm(request.POST)
        if form.is_valid():
            # Manually create and save the model instance
            ModelApplicant.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                phone_number=form.cleaned_data['phone_number'],
                date_of_birth=form.cleaned_data['date_of_birth'],
                instagram_handle=form.cleaned_data['instagram_handle'],
            )
            return redirect('questionnaire')  # Or wherever you want to go next
        else:
            for error in form.errors:
                messages.error(request, form.errors[error])
    else:
        form = ModelApplicantForm()
    return render(request, 'app/form.html', {'form': form})



def model_questionnaire_view(request):
    if request.method == "POST":
        ModelQuestionnaire.objects.create(
            q1=request.POST.get('q1'),
            q2=request.POST.get('q2'),
            q3=request.POST.get('q3'),
            q4=request.POST.get('q4'),
            q5=request.POST.get('q5'),
            q6=request.POST.get('q6'),
            q7=request.POST.get('q7'),
        )
        return redirect('thank-you')  # Redirect after submission

    return render(request, 'app/questions.html')

def thank_you_view(request):
    return render(request, 'app/thank_you.html')