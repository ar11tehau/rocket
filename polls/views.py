from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import DetailView, View, ListView, CreateView
from polls.models import Question
from django.urls import reverse_lazy
from polls.forms import QuestionForm
from rest_framework import viewsets
from polls.serializers import QuestionSerializer



import datetime

# Create your views here.
# def index(request):
#     # Récupération des questions
#     questions = Question.objects.all()

#     # Définition d'un contexte à fournir au template
#     context = {'latest_question_list': questions}

#     # Rendu du gabarit
#     return render(request, 'index.html', context)


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


class Indexview(ListView):
    """Classe vue index basée sur ListView"""
    model = Question
    template_name = 'index.html'
    context_object_name = 'latest_question_list'


class CreateQuestion(CreateView):
    class Meta:
        model = Question
        fields = ['question_text']
        succes_url = reverse_lazy(questions_view)
    
    def form_valid(self, form):
        return super().form_valid(form)

class DetailQuestion(DetailView):
    model = Question

def question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)  # instanciation avec données
        if form.is_valid():
            return redirect('/thanks/')
    else:
        form = QuestionForm()  # instanciation sans données
    # Affichage du formulaire via un template
    return render(request, 'form.html', {'form': form})


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all().order_by("question_text")
    serializer_class = QuestionSerializer
    