from rest_framework import serializers

from .models import Cat, Owner, Achievement


class AchievementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Achievement
        fields = ('id', 'name')


class CatSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(read_only=True)
    achievement = AchievementSerializer(many=True, read_only=True)

    class Meta:
        model = Cat
        fields = ('name', 'color', 'birth_year', 'owner', 'achievement')


class OwnerSerializer(serializers.ModelSerializer):
    cats = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Owner
        fields = ('first_name', 'last_name', 'cats')
