from rest_framework import serializers

from . import models

class OFSerializer(serializers.HyperlinkedModelSerializer):

    image = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = models.OFundus
        fields = ('image', 'class_name', 'refer_to_hospital', 'check_for_macular_edema')