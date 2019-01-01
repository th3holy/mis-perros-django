from core.models import huerfano
from .Serializers import huerfanosSerializer
from rest_framework import viewsets


# Create your views here.
class HuerfanosViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = huerfano.objects.all()
    serializer_class = huerfanosSerializer
