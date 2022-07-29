import datetime
from django.urls import reverse
from django.test import TestCase
from django.utils import timezone

from .models import Question


def ignore(x):
    pass


def createQuestion(question_text, days):
    """
    Create a question with the given `question_text` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        fixedQuestion = createQuestion(question_text="in 30 days", days=+30)
        self.assertIs(fixedQuestion.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is older than 1 day.
        """
        oldQuestion = createQuestion(question_text="2 days ago", days=-2)
        self.assertIs(oldQuestion.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() returns True for questions whose pub_date
        is within the last day.
        """
        almost_yesterday = timezone.now() - datetime.timedelta(
            hours=23, minutes=59, seconds=59
        )
        recentQuestion = Question(pub_date=almost_yesterday)
        self.assertIs(recentQuestion.was_published_recently(), True)


class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        """
        If no questions exist,
        an appropriate message is displayed.
        """
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context["questions"], [])

    def test_past_question(self):
        """
        Questions with a pub_date in the past
        are displayed on the index page.
        """
        pastQuestion = createQuestion(question_text="Past question.", days=-30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(
            response.context["questions"],
            [pastQuestion],
        )

    def test_future_question(self):
        """
        Questions with a pub_date in the future
        aren't displayed on the index page.
        """
        futureQuestion = createQuestion(question_text="Future question.", days=30)
        ignore(futureQuestion)

        response = self.client.get(reverse("polls:index"))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context["questions"], [])

    def test_future_question_and_past_question(self):
        """
        Even if both past and future questions exist,
        only past questions are displayed.
        """
        futureQuestion = createQuestion(question_text="Future question.", days=30)
        ignore(futureQuestion)

        pastQuestion = createQuestion(question_text="Past question.", days=-30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(
            response.context["questions"],
            [pastQuestion],
        )

    def test_two_past_questions(self):
        """
        The questions index page may display multiple questions.
        """
        olderQuestion = createQuestion(question_text="Past question 1.", days=-30)
        oldQuestion = createQuestion(question_text="Past question 2.", days=-5)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(
            response.context["questions"],
            [oldQuestion, olderQuestion],
        )


class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        """
        The detail view of a question with a pub_date in the future
        returns a 404 not found.
        """
        futureQuestion = createQuestion(question_text="Future question.", days=5)
        url = reverse("polls:detail", args=(futureQuestion.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        """
        The detail view of a question with a pub_date in the past
        displays the question's text.
        """
        pastQuestion = createQuestion(question_text="Past Question.", days=-5)
        url = reverse("polls:detail", args=(pastQuestion.id,))
        response = self.client.get(url)
        self.assertContains(response, pastQuestion.question_text)
