from django.shortcuts import render

from .decorators import decorator



@decorator
def question(request):
    latest_question_list = ["데드풀1", "어벤져스", "슈퍼맨vs배트맨", "데드풀2"]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'movies/question.html', context)
