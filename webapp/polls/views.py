from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Question


def index(request):
    questions = Question.objects.order_by('-pub_date')[:5]
    return render(request, 'polls/index.html', {
        'questions': questions
    })


def last5(request):
    questions = [
        oQuestion.question_text
        for oQuestion
        in Question.objects.order_by('-pub_date')[:5]
    ]

    response = ', '.join(questions)
    return HttpResponse(response)


def detail(request, question_id):
    oQuestion = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {
        'question': oQuestion
    })


def results(request, question_id):
    response = "You're looking at the results of question %s." % question_id
    return HttpResponse(response)


def vote(request, question_id):
    response = "You're voting on question %s." % question_id
    return HttpResponse(response)
