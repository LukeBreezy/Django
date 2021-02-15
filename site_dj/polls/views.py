from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, Http404

from .models import Question
# Create your views here.


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def index_teste(request):
    teste = Question.objects.raw('Select * from polls_question order by pub_date desc')
    saida = ', '.join(list(q.question_text for q in teste[:5]))
    return HttpResponse(saida)


def detail(request, question_id):
    # question = get_list_or_404(Question, question_text__startswith='Teste') - Verificar como funciona
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

# Alternativamente
# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404(f"Question {question_id} does not exist")
#     return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
