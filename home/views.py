from django.shortcuts import render
from .models import *

# Create your views here.

def home(req):
    return render(req, 'home.html')

def option1(req):
    if req.method == 'POST':
        ans1 = req.POST.get('ans1', None)
        ans2 = req.POST.get('ans2', None)
        ans3 = req.POST.get('ans3', None)
        ans4 = req.POST.get('ans4', None)

        question1 = quesOne()
        question1.ans1 = ans1
        question1.ans2 = ans2
        question1.ans3 = ans3
        question1.ans4 = ans4

        question1.save()
    return render(req, 'option1.html')

def option2(req):
    return render(req, 'option2.html')

def option3(req):
    return render(req, 'option3.html')

def option4(req):
    return render(req, 'option4.html')

def option5(req):
    return render(req, 'option5.html')

