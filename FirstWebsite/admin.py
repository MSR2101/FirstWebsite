from django.contrib import admin
from FirstWebsite import models

# Register your models here.
model = (models.Merchant, models.DealProvider, models.Deals)
admin.site.register(model)
