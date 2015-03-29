from django.db import models
from django.utils import timezone
import datetime

class Post(models.Model):
	post_text = models.CharField(max_length=500)
	pub_date = models.DateTimeField('date published')
	def was_published_recently(self):
		return self.pub_date >= (timezone.now() - datetime.timedelta(days=1))
	def __str__(self):
		return self.post_text

class Reply(models.Model):
	reply_text = models.CharField(max_length=500)
	post = models.ForeignKey(Post)
	def __str__(self):
		return self.reply_text



