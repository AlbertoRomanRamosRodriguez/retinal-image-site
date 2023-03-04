from rest_framework import serializers

from . import models

class OFSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.OFundus
        fields = ('id', 'image', 'class_name')