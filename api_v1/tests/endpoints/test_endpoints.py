import pytest
import json

from model_bakery import baker
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token


@pytest.mark.django_db
class TestEndpoint:
    def setup_context(self):
        api_client = APIClient()
        token = baker.make(Token)

        return (
            api_client,
            token,
        )

    def test_authentication(self):
        (api_client, token) = self.setup_context()

        # Should return a 401 as not authenticated
        response = api_client.get("/api/v1/scraping/start/")
        assert response.status_code == 401

    def test_client_required(self):
        (api_client, token) = self.setup_context()
        api_client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

        response = api_client.get("/api/v1/scraping/start/")

        assert response.status_code == 200
        content = json.loads(response.content)
        expected_content = {"request": {"status": "started!"}}
        assert content == expected_content
