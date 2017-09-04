from django.db import models

# Create your models here.


class Merchant(models.Model):

    merchantFirstName = models.CharField(max_length=100)
    merchantLastName = models.CharField(max_length=100)
    merchantDisplayName = models.CharField(max_length=200)
    merchantPhoneNum = models.BigIntegerField(unique=True)
    merchantEmail = models.EmailField(unique=True)

    def __str__(self):
        name = self.merchantFirstName + ' ' + self.merchantLastName
        return str(self.id) + '-' + name


class DealProvider(models.Model):

    merchant = models.ForeignKey(Merchant)
    dealCategory = models.CharField(max_length=100)
    dealProName = models.CharField(max_length=200)
    dealProAddress = models.CharField(max_length=500)
    dealProLocLat = models.SmallIntegerField()
    dealProLocLong = models.SmallIntegerField()
    dealProPhoneNum = models.BigIntegerField()
    dealProEmail = models.EmailField()

    def __str__(self):
        return self.dealCategory + '-' + self.dealProName


class Deals(models.Model):

    dealPro = models.ForeignKey(DealProvider)
    dealName = models.CharField(max_length=100)
    dealSummary = models.CharField(max_length=100)
    dealDesc = models.CharField(max_length=500)
    dealDuration = models.IntegerField()
    dealImg = models.CharField(max_length=1000)

    def __str__(self):
        return self.dealName + '-' + self.dealSummary


