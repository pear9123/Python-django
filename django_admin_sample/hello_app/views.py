from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from hello_app.models import Question, Choice
from django.views.generic import ListView, DetailView

# Create your views here.

#IndexView
class IndexView(ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

#DetailView
class DetailsView(DetailView):
    model = Question
    template_name = 'polls/detail.html'

#vote
def vote(request, pk):
    question = get_object_or_404(Question, pk=pk)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': 'You didn`t select a choice',
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('hello_app:results', args=(question.id,)))

#Reuslt views
class ResultView(DetailView):
    model = Question
    template_name = 'polls/results.html'
