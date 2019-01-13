from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse

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

def save_question(request):
	q = Question(question_text=request.POST['question'], detail_text=request.POST['detail'], 
			pub_date=timezone.now())
	q.save()

	if request.user.id:
		request.user.question_set.add(q)
		request.user.save()
		
	return HttpResponseRedirect(reverse('posts:detail', args=(q.id,)))

def delete_question(request):
	q = get_object_or_404(Question, pk=request.POST['question'])

	if request.user.id == q.author.id and request.user.id != None:
		q.delete()

	return HttpResponseRedirect(reverse('posts:index'))