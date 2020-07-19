from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Editor,Article,magazineApiModel,Profile,Comment
from django_summernote.admin import SummernoteModelAdmin

class ArticleAdmin(SummernoteModelAdmin):
	# filter_horizontal = ('tag',)
	list_display = ('title','slug')
	# list_filter = ('status',)
	search_fields = ['title']
	prepopulated_fields = {'slug': ('title',)}
	summernote_fields = '__all__'
	exclude = ('Articles')
 
class CommentAdmin(admin.ModelAdmin):
	list_display = ('name','body','post','created_on','active')
	list_filter =     ('active','created_on')
	search_fields = ('name','email','body')
	actions = ['approve_comments']

	def approve_comments(self,request,queryset):
		queryset.update(active=False)
  

admin.site.site_header = "Baseline Magazine Admin"
admin.site.unregister(Group)
admin.site.register(Editor)
admin.site.register(Article,SummernoteModelAdmin)
# admin.site.register(tags)
admin.site.register(magazineApiModel)
admin.site.register(Profile)
admin.site.register(Comment)
