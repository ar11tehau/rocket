### polls/admin.py
from django.contrib import admin
from polls.models import Choice, Personne, Question, Task, TaskList, Voiture

admin.site.register([Choice, Personne, Question, Task, TaskList, Voiture])
# admin.site.register(Choice)

