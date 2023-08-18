from rest_framework import serializers
from .models import Game

class GameSerializer(serializers.Serializer):

    name=serializers.CharField(max_length=100)
    url=serializers.URLField()
    author=serializers.CharField(max_length=100)
    published_date=serializers.DateField()

    def create(self, validated_data):
        return Game.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        print(instance)
        instance.name=validated_data.get('name',instance.name)
        instance.url=validated_data.get('url',instance.url)
        instance.author=validated_data.get('author',instance.author)
        instance.published_date=validated_data.get('published_date',instance.published_date)
        instance.save()
        return instance
