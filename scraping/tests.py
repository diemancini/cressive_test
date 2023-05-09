from django.test import TestCase

import pytest
from rest_framework.test import APIClient
#from resttest.models import F1Driver

client = APIClient()

@pytest.mark.django_db
def test_start_scraping():
    response = client.get('/api/v1/scraping/start/')
    assert response.status_code == 200
    #f1driver = F1Driver.objects.first()
    #assert f1driver is  None# Create your tests here.
