from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
	path('', views.index, name='index'),
	path('<int:post_id>/', views.detail, name='detail'),
	path('add_question/', views.add_question, name='add_question'),
	path('save_question/', views.save_question, name='save_question'),
	path('delete_question/', views.delete_question, name='delete_question'),
]