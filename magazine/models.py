from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField

class Editor(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	email = models.EmailField()
	phone_number = models.CharField(max_length = 14,blank=True)

	def __str__(self):
		return self.last_name

	def save_editor(self):
		self.save()

class tags(models.Model):
	name = models.CharField(max_length = 30)
	def __str__(self):
		return self.name

# class comment(models.Model):
#     comment=models.TextField()
#     id = models.
#     def __str__(self):
#         self.comment

class Article(models.Model):
    title = models.CharField(max_length=60)
    post = HTMLField()
    editor = models.ForeignKey(User,on_delete=models.CASCADE)
    tag = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add=True)
    article_image = models.ImageField(upload_to='articles/', blank=True)
    photo_credits = models.CharField(max_length=60,default='unsplash.com')
    # comments = models.ManyToManyField(comment)
    def __str__(self):
        return self.title

    @classmethod
    def all_articles(cls):
        articles = cls.objects.all()
        return articles
        
    @classmethod
    def search(cls,search_term):
        articles = cls.objects.filter(title__icontains = search_term)
        return articles

# class comments(models.Model):
#     comment=models.TextField()
#     def __str__(self):
#         self.comment

class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    def __str__(self):
        return self.name