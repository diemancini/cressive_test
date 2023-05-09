import pytest
from model_bakery import baker
from scraping.models import Sponsored


@pytest.mark.django_db
class TestSponsored:
    def test_create_sponsored(self):
        # Create the data to be inserted in db
        sponsored_expected = baker.make(Sponsored)
        # Create the data in db
        sponsored_db = Sponsored.objects.create(
            title=sponsored_expected.title,
            rating=sponsored_expected.rating,
            price=sponsored_expected.price,
            description=sponsored_expected.description,
        )
        # Update db
        sponsored_db.refresh_from_db()
        # Check each of the values against the expected
        assert sponsored_expected.title == sponsored_db.title
        assert sponsored_expected.rating == sponsored_db.rating
        assert sponsored_expected.price == sponsored_db.price
        assert sponsored_expected.description == sponsored_db.description

    def test_read_sponsored(self):
        # Create the data to be inserted in db
        sponsored_expected = baker.make(Sponsored)
        # Create the data in db
        sponsored_db = Sponsored.objects.create(
            title=sponsored_expected.title,
            rating=sponsored_expected.rating,
            price=sponsored_expected.price,
            description=sponsored_expected.description,
        )
        sponsored_db.refresh_from_db()
        read_sponsored_db = Sponsored.objects.get(id=sponsored_db.id)
        # Check each of the values against the expected
        assert sponsored_expected.title == read_sponsored_db.title
        assert sponsored_expected.rating == read_sponsored_db.rating
        assert sponsored_expected.price == read_sponsored_db.price
        assert sponsored_expected.description == read_sponsored_db.description

    def test_delete_sponsored(self):
        # Create the data to be inserted in db
        sponsored_expected = baker.make(Sponsored)
        # Create the data in db
        sponsored_db = Sponsored.objects.create(
            title=sponsored_expected.title,
            rating=sponsored_expected.rating,
            price=sponsored_expected.price,
            description=sponsored_expected.description,
        )
        sponsored_db.refresh_from_db()
        read_sponsored_db = Sponsored.objects.get(id=sponsored_db.id)
        # Check each of the values against the expected
        assert sponsored_expected.title == read_sponsored_db.title
        assert sponsored_expected.rating == read_sponsored_db.rating
        assert sponsored_expected.price == read_sponsored_db.price
        assert sponsored_expected.description == read_sponsored_db.description
        update_sponsored_expected = {
            "title": "FakeTitle2",
            "rating": 4.6,
            "price": 15.17,
            "description": "FakeDescription",
        }
        read_sponsored_db.title = update_sponsored_expected["title"]
        read_sponsored_db.rating = update_sponsored_expected["rating"]
        read_sponsored_db.price = update_sponsored_expected["price"]
        read_sponsored_db.description = update_sponsored_expected["description"]
        read_sponsored_db.save()

        assert update_sponsored_expected["title"] == read_sponsored_db.title
        assert update_sponsored_expected["rating"] == read_sponsored_db.rating
        assert update_sponsored_expected["price"] == read_sponsored_db.price
        assert update_sponsored_expected["description"] == read_sponsored_db.description

    def test_update_sponsored(self):
        # Create the data to be inserted in db
        sponsored_expected = baker.make(Sponsored)
        # Create the data in db
        sponsored_db = Sponsored.objects.create(
            title=sponsored_expected.title,
            rating=sponsored_expected.rating,
            price=sponsored_expected.price,
            description=sponsored_expected.description,
        )
        sponsored_db.refresh_from_db()
        read_sponsored_db = Sponsored.objects.get(id=sponsored_db.id)

        # Check each of the values against the expected
        assert sponsored_expected.title == read_sponsored_db.title
        assert sponsored_expected.rating == read_sponsored_db.rating
        assert sponsored_expected.title == read_sponsored_db.title
        assert sponsored_expected.rating == read_sponsored_db.rating

        read_sponsored_db.delete()
        # Try to read the same data that was deleted before
        # Should return zero results.
        read_deleted_sponsored_db = Sponsored.objects.filter(id=sponsored_db.id)
        assert len(read_deleted_sponsored_db) == 0
