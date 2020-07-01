from django.test import TestCase
from .models import Editor,Article,tag

class EditorTestClass(TestCase):
	def setUp(self):
		self.cwilv=Editor(first_name = 'Cwilv',last_name = 'Iam',email = 'a@b.com')

	def test_instance(self):
		self.assertTrue(isinstance(self.cwilv,Editor))

	def test_save_method(self):
		self.cwilv.save_editor()
		editors = Editor.objects.all()
		self.assertTrue(len(editors)>0)

class ArticleTestCase(TestCase):
	def setUp(self):
		self.cwilv = Article(title = 'Nature of Beauty',post = 'I will talk about the legendary beauty',editor='cwilv',created_on='23-07-2020')
	def test_instance(self):
		self.assertTrue(isinstance(self.cwilv,Article))
	def test_save_method(self):
		self.cwilv.save_article()
		articles = Article.objects.all()
		self.assertTrue(len(articles)>0)