# from django.test import TestCase

# from faker import Faker
import pytest
from model_bakery import baker
from scraping.models import KeyWord
from api_v1.serializers.scraping import StartScrapingSerializer


@pytest.mark.django_db
def test_keywords_serializer():
    """
    Should serialize a Venue into a format expected by the V1 API
    """

    # Create resources, forcing the optional related resource to be set

    keywords = baker.make(KeyWord, _fill_optional=True)

    expected_keywords_attrs = (
        "id",
        "name",
        "date",
    )
    serializer = StartScrapingSerializer(keywords)

    # Check all the expected fields on the task level are there
    assert set(serializer.data.keys()) == set(expected_keywords_attrs)
