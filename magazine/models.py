from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    bio = models.TextField(max_length=500,blank=True)
    location = models.CharField(max_length = 30,blank=True)
    birth_date = models.DateField(null=True,blank=True)
    image = models.ImageField(upload_to='articles',default='articles/yhb5DBT91u4_Regular.jpg',blank=True)
    def __str__(self):
        return (self.user.first_name)

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        image = Image.open(self.image.path)
        if image.height > 400 or image.width > 400:
            output_size = (400,400)
            image.thumbnail(output_size)
            image.save(self.image.path)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

class Editor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 14,blank=True)
    bio = models.TextField(default='')
    profile_pic = models.ImageField(upload_to='avatars/',blank=True)

    def __str__(self):
        return self.last_name

    def save_editor(self):
        self.save()

class tags(models.Model):
	name = models.CharField(max_length = 30)
	def __str__(self):
		return self.name


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Article(models.Model):
    title = models.CharField(max_length=60)
    slug = models.SlugField(max_length=200, unique=True)
    status = models.IntegerField(choices=STATUS, default=0)
    post = HTMLField()
    editor = models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
    tag = models.ManyToManyField(tags,blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    article_image = models.ImageField(upload_to='articles/', blank=True)
    photo_credits = models.CharField(max_length=60,default='unsplash.com')
    
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

class Comment(models.Model):
    post = models.ForeignKey(Article,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
class magazineApiModel(models.Model):
    title = models.CharField(max_length=100)
    post = HTMLField()
    editor = models.CharField(max_length=100)
    tags = models.CharField(max_length=200,blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    article_image = models.ImageField(upload_to='articles/')
    photo_credits = models.CharField(max_length=100)

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

mode = Article