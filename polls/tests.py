from django.test import TestCase
from polls.models import Question
from django.utils import timezone


# Create your tests here.

class TestPoll(TestCase):
    def setUp(self):
        time = timezone.now()
        self.question1 = Question.objects.create(question_text='On fait une pause ?', pub_date=time)

    def test_resolve_home_url(self):
        response = self.client.get('/polls/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'On fait une pause ?')