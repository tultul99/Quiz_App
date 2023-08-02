from django.shortcuts import render
from .models import *

# Create your views here.

marks = 0

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

        result = quesOne.objects.all()
        global marks
        for i in result:
            if i.ans3 == '114':
                marks = marks + 1
                break
        print(marks)

        result.delete()
    return render(req, 'option1.html')

def option2(req):
    if req.method == 'POST':
        ans1 = req.POST.get('ans1', None)
        ans2 = req.POST.get('ans2', None)
        ans3 = req.POST.get('ans3', None)
        ans4 = req.POST.get('ans4', None)

        question1 = quesTwo()
        question1.ans1 = ans1
        question1.ans2 = ans2
        question1.ans3 = ans3
        question1.ans4 = ans4

        question1.save()

        result = quesTwo.objects.all()
        global marks
        for i in result:
            if i.ans2 == '89':
                marks = marks + 1
                break
        print(marks)

        result.delete()
    return render(req, 'option2.html')

def option3(req):
    if req.method == 'POST':
        ans1 = req.POST.get('ans1', None)
        ans2 = req.POST.get('ans2', None)
        ans3 = req.POST.get('ans3', None)
        ans4 = req.POST.get('ans4', None)

        question1 = quesThree()
        question1.ans1 = ans1
        question1.ans2 = ans2
        question1.ans3 = ans3
        question1.ans4 = ans4

        question1.save()

        result = quesThree.objects.all()
        global marks
        for i in result:
            if i.ans4 == '25':
                marks = marks + 1
                break
        print(marks)

        result.delete()
    return render(req, 'option3.html')

def option4(req):
    if req.method == 'POST':
        ans1 = req.POST.get('ans1', None)
        ans2 = req.POST.get('ans2', None)
        ans3 = req.POST.get('ans3', None)
        ans4 = req.POST.get('ans4', None)

        question1 = quesFour()
        question1.ans1 = ans1
        question1.ans2 = ans2
        question1.ans3 = ans3
        question1.ans4 = ans4

        question1.save()

        result = quesFour.objects.all()
        global marks
        for i in result:
            if i.ans1 == 'Dawud':
                marks = marks + 1
                break
        print(marks)

        result.delete()
    return render(req, 'option4.html')

def option5(req):
    if req.method == 'POST':
        ans1 = req.POST.get('ans1', None)
        ans2 = req.POST.get('ans2', None)
        ans3 = req.POST.get('ans3', None)
        ans4 = req.POST.get('ans4', None)

        question1 = quesFive()
        question1.ans1 = ans1
        question1.ans2 = ans2
        question1.ans3 = ans3
        question1.ans4 = ans4

        question1.save()

        result = quesFive.objects.all()
        global marks
        for i in result:
            if i.ans4 == 'Ali':
                marks = marks + 1
                break
        print(marks)

        result.delete()
    return render(req, 'option5.html')


def result(req):
    return render(req, 'result.html', {'mark':marks})

