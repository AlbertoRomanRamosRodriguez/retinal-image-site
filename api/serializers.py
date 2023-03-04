from rest_framework import serializers

from . import models

class OFSerializer(serializers.HyperlinkedModelSerializer):

    image = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = models.OFundus
        fields = ('id', 'image', 'class_name')