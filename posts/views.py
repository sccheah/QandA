from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from .models import Question

# Create your views here. Start off with function-based views then switch to CBV
def index(request):
	question_list = Question.objects.order_by('-pub_date')
	context = {'question_list': question_list}
	return render(request, 'posts/index.html', context)

def detail(request, post_id):
	question = get_object_or_404(Question, pk=post_id)
	return render(request, 'posts/detail.html', {'question': question, 'answers': question.answer_set.all()})

def add_question(request):
	return render(request, 'posts/add_question.html', {})