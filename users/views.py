from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.urls import reverse

from .forms import CustomUserCreationForm
from .models import CustomUser

# Create your views here.
class SignUp(generic.CreateView):
	form_class = CustomUserCreationForm
	success_url = reverse_lazy('login')
	template_name = 'signup.html'

def profile(request, user_id):
	user = get_object_or_404(CustomUser, pk=user_id)
	return render(request, 'users/profile.html', {
		'user': user, 
		'questions': user.question_set.all(), 
		'answers': user.answer_set.all()
	})