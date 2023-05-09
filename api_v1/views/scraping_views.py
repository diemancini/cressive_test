from rest_framework import (
    viewsets,
    permissions,
    viewsets,
)
from rest_framework.response import Response
from scraping.models import KeyWord
from datetime import datetime


from api_v1.serializers.scraping import (
    StartScrapingSerializer,
)
from scraping.scraping import Scraping

class ScrapingStartViewSet(
    viewsets.GenericViewSet
):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = StartScrapingSerializer

    def list(self, request, pk=None):
        data = self.get_queryset()
        results = StartScrapingSerializer(data, many=True).data
        scraping = Scraping()
        response = scraping.start_scraping(results)

        return Response(response)
    
    def get_queryset(self):
        date = datetime.now()
        data = KeyWord.objects.filter(date=date).order_by('name')
        
        return data




