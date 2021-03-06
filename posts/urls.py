from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
	path('', views.index, name='index'),
	path('<int:post_id>/', views.detail, name='detail'),
	path('add_question/', views.add_question, name='add_question'),
	path('save_question/', views.save_question, name='save_question'),
	path('delete_question/', views.delete_question, name='delete_question'),
	path('<int:post_id>/save_answer/', views.save_answer, name='save_answer'),
	path('<int:post_id>/delete_answer/', views.delete_answer, name='delete_answer'),
]