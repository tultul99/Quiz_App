from django.urls import path
from home import views

urlpatterns = [
    path("", views.home, name='home'),
    path("op1/", views.option1, name='option1'),
    path("op2/", views.option2, name='option2'),
    path("op3/", views.option3, name='option3'),
    path("op4/", views.option4, name='option4'),
    path("op5/", views.option5, name='option5'),    
    path("r/", views.result, name='result'),    
]
