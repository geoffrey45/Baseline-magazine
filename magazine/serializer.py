from rest_framework import serializers
from .models import magazineApiModel

class apiSerializer(serializers.ModelSerializer):
	class Meta:
		model = magazineApiModel
		fields = ('id', 'title','post','editor','tags','article_image','photo_credits')

