from django.contrib import admin
from .models import Editor,Article,tags,NewsLetterRecipients,magazineApiModel,Profile

class ArticleAdmin(admin.ModelAdmin):
	filter_horizontal = ('tag',)

admin.site.register(Editor)
admin.site.register(Article,ArticleAdmin)
admin.site.register(tags)
admin.site.register(NewsLetterRecipients)
admin.site.register(magazineApiModel)
admin.site.register(Profile)