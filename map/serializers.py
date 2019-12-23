from rest_framework import serializers

from .models import Condition

class ConditionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Condition
        fields = ('name', 'state')
