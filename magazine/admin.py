from django.contrib import admin
from .models import Editor,Article,tags,magazineApiModel,Profile,Comment

class ArticleAdmin(admin.ModelAdmin):
	filter_horizontal = ('tag',)
	list_display = ('title','pub_date')
	list_filter = ('status',)
	search_fields = ['title']
	prepopulated_fields = {'slug':('title',)}

class CommentAdmin(admin.ModelAdmin):
	list_display = ('name','body','post','created_on','active')
	list_filter = ('active','created_on')
	search_fields = ('name','email','body')
	actions = ['approve_comments']

	def approve_comments(self,request,queryset):
		queryset.update(active=False)

admin.site.register(Editor)
admin.site.register(Article,ArticleAdmin)
admin.site.register(tags)
admin.site.register(magazineApiModel)
admin.site.register(Profile)
admin.site.register(Comment)