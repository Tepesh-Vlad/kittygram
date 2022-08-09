import datetime as dt
import webcolors

from rest_framework import serializers

from .models import Cat, Owner, Achievement


class Hex2NameColor(serializers.Field):
    def to_representation(self, value):
        return value

    def to_internal_value(self, data):
        try:
            data = webcolors.hex_to_name(data)

        except ValueError:
            raise serializers.ValidationError('Для этого цвета нет имени')
        return data


class AchievementSerializer(serializers.ModelSerializer):
    achievement_name = serializers.CharField(source='name')

    class Meta:
        model = Achievement
        fields = ('id', 'achievement_name')


class CatSerializer(serializers.ModelSerializer):
    # owner = serializers.StringRelatedField(read_only=True)
    achievement = AchievementSerializer(many=True, read_only=True)
    age = serializers.SerializerMethodField()
    # color = Hex2NameColor()

    class Meta:
        model = Cat
        fields = ('name', 'color', 'birth_year', 'owner', 'achievement', 'age')

    def get_age(self, obj):
        return dt.datetime.now().year - obj.birth_year


class OwnerSerializer(serializers.ModelSerializer):
    cats = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Owner
        fields = ('first_name', 'last_name', 'cats')
