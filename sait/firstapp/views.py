from django.shortcuts import render
from .forms import FeedbackForm
from .models import Feedback
from django.http import HttpResponse

def home(request):
    form = FeedbackForm(request.POST or None)
    if request.method =="POST" and form.is_valid():
        form=form.save()
        return HttpResponse("""<h1>Ваш комментарий сохранен!</h1>
        <h1><a href="http://127.0.0.1:8000/firstapp/test">Просмотр всех комменатриев</h1>""")
    else:
        return render(request,'home.html',locals())

def get(request):
    feedbacks = Feedback.objects.all()
    return render(request, 'get.html', locals())