from django.db import models
import datetime as dt

class Editor(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	email = models.EmailField()
	phone_number = models.CharField(max_length = 14,blank=True)

	def __str__(self):
		return self.last_name

	def save_editor(self):
		self.save()

class tag(models.Model):
	name = models.CharField(max_length = 30)
	def __str__(self):
		return self.name

class Article(models.Model):
    title = models.CharField(max_length =60)
    post = models.TextField()
    editor = models.ForeignKey(Editor,on_delete = models.CASCADE)
    tags = models.ManyToManyField(tag)
    pub_date = models.DateTimeField(auto_now_add=True)
    article_image = models.ImageField(upload_to='articles/',blank=True)
    photo_credits = models.CharField(max_length=30,blank=True)

    def __str__(self):
        return self.title

    @classmethod
    def all_articles(cls):
        news = cls.objects.all()
        return news