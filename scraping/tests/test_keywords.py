import pytest
from model_bakery import baker
from scraping.models import KeyWord


@pytest.mark.django_db
class TestKeywords:
    def test_create_keywords(self):
        # Create the data to be inserted in db
        keywords_expected = baker.make(KeyWord)
        # Create the data in db
        keywords_db = KeyWord.objects.create(
            name=keywords_expected.name,
            date=keywords_expected.date,
        )
        # Update db
        keywords_db.refresh_from_db()
        # Check each of the values against the expected
        assert keywords_expected.name == keywords_db.name
        assert keywords_expected.date == keywords_db.date

    def test_read_keywords(self):
        # Create the data to be inserted in db
        keywords_expected = baker.make(KeyWord)
        # Create the data in db
        keywords_db = KeyWord.objects.create(
            name=keywords_expected.name,
            date=keywords_expected.date,
        )
        keywords_db.refresh_from_db()
        read_keywords_db = KeyWord.objects.get(id=keywords_db.id)
        # Check each of the values against the expected
        assert keywords_expected.name == read_keywords_db.name
        assert keywords_expected.date == read_keywords_db.date

    def test_update_keywords(self):
        # Create the data to be inserted in db
        keywords_expected = baker.make(KeyWord)
        # Create the data in db
        keywords_db = KeyWord.objects.create(
            name=keywords_expected.name,
            date=keywords_expected.date,
        )
        keywords_db.refresh_from_db()
        read_keywords_db = KeyWord.objects.get(id=keywords_db.id)
        # Check each of the values against the expected
        assert keywords_expected.name == read_keywords_db.name
        assert keywords_expected.date == read_keywords_db.date
        update_keywords_expected = {"name": "FakeName2", "date": "2023-06-10"}
        read_keywords_db.name = update_keywords_expected["name"]
        read_keywords_db.date = update_keywords_expected["date"]
        read_keywords_db.save()

        assert update_keywords_expected["name"] == read_keywords_db.name
        assert update_keywords_expected["date"] == read_keywords_db.date

    def test_delete_keywords(self):
        # Create the data to be inserted in db
        keywords_expected = baker.make(KeyWord)
        # Create the data in db
        keywords_db = KeyWord.objects.create(
            name=keywords_expected.name,
            date=keywords_expected.date,
        )
        keywords_db.refresh_from_db()
        read_keywords_db = KeyWord.objects.get(id=keywords_db.id)

        # Check each of the values against the expected
        assert keywords_expected.name == read_keywords_db.name
        assert keywords_expected.date == read_keywords_db.date

        read_keywords_db.delete()
        # Try to read the same data that was deleted before
        # Should return zero results.
        read_deleted_keywords_db = KeyWord.objects.filter(id=keywords_db.id)
        assert len(read_deleted_keywords_db) == 0
