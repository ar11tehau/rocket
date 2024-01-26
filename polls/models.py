from django.db import models

class Question(models.Model):
    """Model for Question"""
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    question_number = models.IntegerField(default=0)
    def __str__(self):
        return self.question_text
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class Task(models.Model):
    task_name = models.CharField(max_length=200)
    def __str__(self):
        return self.task_name
  
class TaskList(models.Model):
    list_name = models.CharField(max_length=200)
    task_choice = models.ForeignKey(Task, on_delete=models.CASCADE, default = 1)
    def __str__(self):
        return self.list_name

class Personne(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    def __str__(self):
        return self.name

class Voiture(models.Model):
    name = models.CharField(max_length=200)
    drivers = models.ManyToManyField(Personne)
    def __str__(self):
        return self.name + ": " + ', '.join(str(driver) for driver in self.drivers.all())
    

