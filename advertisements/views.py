from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from advertisements.models import Advertisement
from advertisements.serializers import AdvertisementSerializer
from django_filters import rest_framework as filters
from .filters import AdvertisementFilter
from .permissions import IsAdvertisementOwner


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = (filters.DjangoFilterBackend)
    filterset_class = AdvertisementFilter

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create"]:
            return [IsAuthenticated()]
        elif self.action in["update", "partial_update", "delete"]:
            return [IsAuthenticated(), IsAdvertisementOwner()]
        return []
