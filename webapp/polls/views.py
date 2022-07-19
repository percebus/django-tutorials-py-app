from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.shortcuts import render, get_object_or_404

from .models import Question, Choice


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'questions'

    """
    Return the last five published questions
    (not including those set to be published in the future).
    """
    def get_queryset(self):
        now = timezone.now()
        return Question \
            .objects \
            .filter(pub_date__lte=now) \
            .order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        # Excludes any questions that aren't published yet.
        return Question \
            .objects \
            .filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    oQuestion = get_object_or_404(Question, pk=question_id)
    try:
        oChoice = oQuestion.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': oQuestion,
            'error_message': "You didn't select a choice.",
        })
    else:
        oChoice.votes += 1
        oChoice.save()

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        response = reverse('polls:results', args=(oQuestion.id,))
        return HttpResponseRedirect(response)
