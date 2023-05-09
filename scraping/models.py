from django.db import models


class KeyWord(models.Model):
    class Meta:
        db_table = "Keyword"

    name = models.CharField(max_length=254, null=True, blank=True)
    date = models.DateField()

    def __str__(self):
        return self.name


class BaseScraping(models.Model):
    class Meta:
        db_table = "BaseScraping"

    title = models.CharField(max_length=254)
    description = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=13, decimal_places=2)
    rating = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return self.title


class Sponsored(BaseScraping):
    class Meta:
        db_table = "Sponsored"


class Organic(BaseScraping):
    class Meta:
        db_table = "Organic"
