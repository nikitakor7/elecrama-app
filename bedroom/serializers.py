from rest_framework import serializers
from bedroom.models import bedroom, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    bedroom = serializers.PrimaryKeyRelatedField(many=True, queryset=bedroom.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'bedroom')


class bedroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = bedroom
        fields = ('id', 'created', 'switch', 'current_value', 'status')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return bedroom.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `bedroom` instance, given the validated data.
        """
        instance.switch = validated_data.get('switch', instance.switch)
        instance.current_value = validated_data.get('room', current_value)
        instance.status = validated_data.get('status', instance.status)
        instance.switch = validated_data.get('switch', instance.switch)
        instance.save()
        return instance
