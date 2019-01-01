from core.models import huerfano
from rest_framework import serializers


class huerfanosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = huerfano
        fields = ('Nombre','Raza','Descripcion','Fotografia','Estado')

