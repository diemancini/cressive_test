import pytest
from model_bakery import baker
from scraping.models import Organic


@pytest.mark.django_db
class TestOrganics:
    def test_create_sponsored(self):
        # Create the data to be inserted in db
        organics_expected = baker.make(Organic)
        # Create the data in db
        organics_db = Organic.objects.create(
            title=organics_expected.title,
            rating=organics_expected.rating,
            price=organics_expected.price,
            description=organics_expected.description,
        )
        # Update db
        organics_db.refresh_from_db()
        # Check each of the values against the expected
        assert organics_expected.title == organics_db.title
        assert organics_expected.rating == organics_db.rating
        assert organics_expected.price == organics_db.price
        assert organics_expected.description == organics_db.description

    def test_read_sponsored(self):
        # Create the data to be inserted in db
        organics_expected = baker.make(Organic)
        # Create the data in db
        organics_db = Organic.objects.create(
            title=organics_expected.title,
            rating=organics_expected.rating,
            price=organics_expected.price,
            description=organics_expected.description,
        )
        organics_db.refresh_from_db()
        read_organics_db = Organic.objects.get(id=organics_db.id)
        # Check each of the values against the expected
        assert organics_expected.title == read_organics_db.title
        assert organics_expected.rating == read_organics_db.rating
        assert organics_expected.price == read_organics_db.price
        assert organics_expected.description == read_organics_db.description

    def test_update_sponsored(self):
        # Create the data to be inserted in db
        organics_expected = baker.make(Organic)
        # Create the data in db
        organics_db = Organic.objects.create(
            title=organics_expected.title,
            rating=organics_expected.rating,
            price=organics_expected.price,
            description=organics_expected.description,
        )
        organics_db.refresh_from_db()
        read_organics_db = Organic.objects.get(id=organics_db.id)
        # Check each of the values against the expected
        assert organics_expected.title == read_organics_db.title
        assert organics_expected.rating == read_organics_db.rating
        assert organics_expected.price == read_organics_db.price
        assert organics_expected.description == read_organics_db.description
        update_organics_expected = {
            "title": "FakeTitle2",
            "rating": 4.6,
            "price": 15.17,
            "description": "FakeDescription",
        }
        read_organics_db.title = update_organics_expected["title"]
        read_organics_db.rating = update_organics_expected["rating"]
        read_organics_db.price = update_organics_expected["price"]
        read_organics_db.description = update_organics_expected["description"]
        read_organics_db.save()

        assert update_organics_expected["title"] == read_organics_db.title
        assert update_organics_expected["rating"] == read_organics_db.rating
        assert update_organics_expected["price"] == read_organics_db.price
        assert update_organics_expected["description"] == read_organics_db.description

    def test_delete_sponsored(self):
        # Create the data to be inserted in db
        organics_expected = baker.make(Organic)
        # Create the data in db
        organics_db = Organic.objects.create(
            title=organics_expected.title,
            rating=organics_expected.rating,
            price=organics_expected.price,
            description=organics_expected.description,
        )
        organics_db.refresh_from_db()
        read_organics_db = Organic.objects.get(id=organics_db.id)

        # Check each of the values against the expected
        assert organics_expected.title == read_organics_db.title
        assert organics_expected.rating == read_organics_db.rating
        assert organics_expected.title == read_organics_db.title
        assert organics_expected.rating == read_organics_db.rating

        read_organics_db.delete()
        # Try to read the same data that was deleted before
        # Should return zero results.
        read_deleted_organics_db = Organic.objects.filter(id=organics_db.id)
        assert len(read_deleted_organics_db) == 0
