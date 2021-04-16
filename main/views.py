from django.shortcuts import render
from .models import Question, Developer, Choice

def index(request):
    developers = Developer.objects.all() # Developer에 입력된 모든 값을 가져옴/ get()은 1개만 가져옴

    context = { 
        'developers' : developers,
    }

    return render(request, 'index.html', context=context)

def form(request):
    questions = Question.objects.all() 
    context = { 
        'questions' : questions,
    }

    return render(request, 'form.html', context=context)

def result(request):
    # 문항 수
    N = Question.objects.count()
    # 개발자 유형 수 
    K = Developer.objects.count()
    print(f'문항 수 : {N}, 개발자 유형 수 : {K}')

    counter = [0] * (K + 1)

    # print(f'POST : {request.POST}')

    # 점수 누적
    for n in range(1, N+1):
        developer_id = int(request.POST[f'question-{n}'][0])
        counter[developer_id] += 1

    # 최고점 개발 유형
    best_developer_id = max(range(1, K+1), key=lambda id : counter[id])
    best_developer = Developer.objects.get(pk=best_developer_id)
    best_developer.count += 1
    best_developer.save()

    context = {
        'developer' : best_developer,
        'counter' : counter
    }
    return render(request, 'result.html', context)