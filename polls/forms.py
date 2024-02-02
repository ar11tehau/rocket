from django import forms

class QuestionForm(forms.Form):
    questions_text = forms.CharField(max_length=100)
    question_nombre = forms.CharField()
    pub_date = forms.DateField()
