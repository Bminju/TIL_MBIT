from django.shortcuts import render
from .models import Question, Developer, Choice

def index(request):
    developers = Developer.objects.all() # Developer에 입력된 모든 값을 가져옴/ get()은 1개만 가져옴

    context = { 
        'developers' : developers,
    }

    return render(request, 'index.html', context=context)