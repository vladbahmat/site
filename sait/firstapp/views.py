from django.shortcuts import render
from .forms import FeedbackForm
from .models import Feedback

# Create your views here.
def home(request):
    form=FeedbackForm(request.POST or None)
    if request.method=="POST" and form.is_valid():
        form=form.save()
    return render(request,'home.html',locals())

def get(request):
    feedbacks=Feedback.objects.all()
    return render(request, 'get.html', locals())