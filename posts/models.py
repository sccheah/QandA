from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Question(models.Model):
	author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
	question_text = models.CharField(max_length=250)
	detail_text = models.CharField(max_length=1000)
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return "Question: " + self.question_text + "\nDetail: " + self.detail_text

class Answer(models.Model):
	author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	answer_text = models.CharField(max_length=10000)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return self.answer_text