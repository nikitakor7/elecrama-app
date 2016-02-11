from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'created', 'switch', 'room', 'status','current_value')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        print(validated_data)
        import pdb
        pdb.set_trace()
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.switch = validated_data.get('switch', instance.switch)
        instance.Room = validated_data.get('room', instance.Room)
        instance.status = validated_data.get('status', instance.status)
        #instance.longitude = validated_data.get('longitude', instance.language)
        #instance.time = validated_data.get('time', instance.time)
        instance.switch = validated_data.get('switch', instance.switch)
        instance.current_value = validated_data.get('switch', instance.current_value)
        instance.save()
        return instance
