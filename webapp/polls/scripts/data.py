# SRC: https://docs.djangoproject.com/en/4.0/intro/tutorial02/

from django.utils import timezone
from polls.models import Question, Choice

# SELECT *
Question.objects.all()  # <QuerySet []>

# INSERT
oQuestion = Question(question_text="What's new?", pub_date=timezone.now())
oQuestion.save()

# SELECT
oQuestion.id  # 1
oQuestion.question_text  # "What's new?"
oQuestion.pub_date  # today's date
oQuestion.was_published_recently()  # true

# UPDATE
oQuestion.question_text = "What's up?"
oQuestion.save()


# FK INSERT
oQuestion.choice_set.all()  # <QuerySet []>
oQuestion.choice_set.create(choice_text="Not much", votes=0)
oQuestion.choice_set.create(choice_text="The sky", votes=0)
oQuestion.choice_set.create(choice_text="Just hacking again", votes=0)
# NOTE: No .save()
oQuestion.choice_set.count()  # 3
oQuestion.choice_set.all()

# SELECT WHERE choice_text LIKE "Just hacking*"
oChoice = oQuestion.choice_set.filter(choice_text__startswith="Just hacking")
oChoice.delete()
oQuestion.choice_set.count()  # 2
oQuestion.choice_set.all()


# SELECT *
Question.objects.all()  # <QuerySet []>


# SELECT * WHERE id=1
Question.objects.filter(id=1)
Question.objects.get(pk=1)

# SELECT * WHERE question_text LIKE "What*"
Question.objects.filter(question_text__startswith="What")

# SELECT * WHERE id=2
Question.objects.get(id=2)  # "DoesNotExist: Question matching query does not exist."

current_year = timezone.now().year
Choice.objects.filter(question__pub_date__year=current_year)
