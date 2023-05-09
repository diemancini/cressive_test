from rest_framework import serializers
from scraping.models import KeyWord


class StartScrapingSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeyWord
        ordering = ["name"]
        fields = (
            "id",
            "name",
            "date",
        )
