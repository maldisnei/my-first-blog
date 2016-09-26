from django.db import models

from django.utils import timezone
class Post(models.Model):
	auth = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	texto = models.TextField()
	created_data = models.DateTimeField(default=timezone.now())
	published_data = models.DateTimeField(blank=True, null=True)

	def __str__(self):
		return self.title
	def published(self):
		self.published_data=timezone.now()
		self.save()
	def approved_comments(self):
		return self.comments.filter(approved_comment=True)
class Comment(models.Model):
	post = models.ForeignKey('blog.Post',related_name='comments')
	author = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	approved_comment = models.BooleanField(default=False)
	def approve(self):
		self.approved_comment = True
		self.save()
	def __str__(self):
		return self.text		
