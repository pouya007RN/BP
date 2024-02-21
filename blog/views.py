from rest_framework.viewsets import ReadOnlyModelViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin
from .models import Content, ContentRate
from .serializers import ContentRateSerializer, ContentSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny


class ContentViewSet(ReadOnlyModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    permission_classes = [AllowAny]
    
    

class ContentRateViewSet(CreateModelMixin, GenericViewSet):
    queryset = ContentRate.objects.all()
    serializer_class = ContentRateSerializer
    permission_classes = [IsAuthenticated]
