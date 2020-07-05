from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image
from django.urls import reverse
from django.template.defaultfilters import slugify

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    bio = models.TextField(max_length=500,blank=True)
    location = models.CharField(max_length = 30,blank=True)
    birth_date = models.DateField(null=True,blank=True)
    image = models.TextField(default='https://i.ibb.co/y5HMpDk/0-T9m-KFye-N5-M-Regular.jpg')
    def __str__(self):
        return (self.user.username)
    
    # to resize image size on file upload

    # def save(self, *args, **kwargs):
    #     super(Profile, self).save(*args, **kwargs)
    #     image = Image.open(self.image.path)
    #     if image.height > 400 or image.width > 400:
    #         output_size = (400,400)
    #         image.thumbnail(output_size)
    #         image.save(self.image.path)
            
    @classmethod
    def all_editors(cls):
        editors = cls.objects.all()
        return editors

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

    def __str__(self):
        return self.last_name

    def save_editor(self):
        self.save()
    

# class tags(models.Model):
# 	name = models.CharField(max_length = 30)
# 	def __str__(self):
# 		return self.name


# STATUS = (
#     (0,"Draft"),
#     (1,"Publish")
# )

class Article(models.Model):
    title = models.CharField(max_length=1000)
    # status = models.IntegerField(choices=STATUS, default=0)
    post = models.TextField(default='')
    editor = models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
    # tag = models.ManyToManyField(tags,blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    article_image = models.CharField(max_length=6000,default='https://i.ibb.co/d7rtpgC/5c3vd-Zz-jdc-Regular.jpg')
    photo_credits = models.CharField(max_length=6000,default='unsplash.com')
    slug = models.SlugField(null=False,unique=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("article", kwargs={"slug": self.slug})
    
    def save(self, **kwargs):
        if not self.slug:
            slug = slugify(self.title)
            while True:
                try:
                    article = Article.objects.get(slug=slug)
                    if article == self:
                        self.slug = slug
                        break
                    else:
                        slug = slug + '-'
                except:
                    self.slug = slug
                    break

        super(Article, self).save()
    
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
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.email)
    
class magazineApiModel(models.Model):
    title = models.CharField(max_length=100)
    post = models.TextField()
    editor = models.CharField(max_length=100)
    tags = models.CharField(max_length=200,blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
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