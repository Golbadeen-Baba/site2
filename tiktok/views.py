from django.shortcuts import render, redirect
from .forms import TikTokProfileForm  # Make sure this imports the form you created

# Create your views here.

def landing_view(request):
    return render(request, 'tiktok/landing.html')



def tiktok_questionnaire_view(request):
    if request.method == "POST":
        form = TikTokProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')  # Redirect after successful submission
    else:
        form = TikTokProfileForm()

    return render(request, 'tiktok/questions.html', {'form': form})




def thank_you_view(request):
    return render(request, 'tiktok/thank_you.html')