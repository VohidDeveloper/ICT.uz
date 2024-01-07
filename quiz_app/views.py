from django.shortcuts import render
import random

from .models import Quiz

def quiz(request):
    quizes = list(Quiz.objects.all())
    if len(quizes) >= 20:
        random_quizes = random.sample(quizes, 20)
    else:
        random_quizes = random.sample(quizes, len(quizes))

    if request.method == 'POST':
        print(request.POST)
        result = 0
        for i in range(len(random_quizes)):
            if request.POST.get(f'answer_{random_quizes[i].id}'):
                if request.POST.get(f'answer_{random_quizes[i].id}') == random_quizes[i].correct_answer:
                    result += 1
        return render(request, 'quiz/quiz-success.html', {
            'result': result,
            'len_quizes': len(random_quizes),
            'problem_results': len(random_quizes) - result,
        })

    ctx = {
        'quizes': random_quizes,
    }

    return render(request, 'quiz/quiz.html', ctx)
