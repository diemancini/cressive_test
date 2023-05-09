from django.contrib import admin
from scraping.models import (
    KeyWord,
    Organic,
    Sponsored,
)

admin.site.register(Sponsored)
admin.site.register(Organic)
admin.site.register(KeyWord)