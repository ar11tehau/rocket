from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from polls.models import Question

import datetime

# Create your views here.
def index(request):
    # Récupération des questions
    questions = Question.objects.all()

    # Définition d'un contexte à fournir au template
    context = {'latest_question_list': questions}

    # Rendu du gabarit
    return render(request, 'index.html', context)


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

class CurrentDatetimeView(View):
    def get(self, request, *args, **kwargs):
        now = datetime.datetime.now()
        html = "<html><body>It is now %s.</body></html>" % now
        return HttpResponse(html)
    
class ArchiveView(View):
    def get(self, request, year, month):
        print(year)  # 2014
        print(month)  # 12
        html = "<html><body>It {} is now {}.</body></html>".format(year, month)
        return HttpResponse(html)


def questions_view(request):
    # Récupération des questions
    questions = Question.objects.all()

    # Définition d'un contexte à fournir au template
    context = {'latest_question_list': questions}

    # Rendu du gabarit
    return render(request, 'index.html', context)


def detail(request, question_id):
    # Récupération des questions
    question = Question.objects.get(pk=question_id)

    # Définition d'un contexte à fournir au template
    context = {'question': question, }

    # Rendu du gabarit
    return render(request, 'question_detail.html', context)


def add_question(request):
    # Récupération des questions
    questions = Question.objects.all()

    # Définition d'un contexte à fournir au template
    context = {'latest_question_list': questions}

    # Rendu du gabarit
    return render(request, 'index.html', context)