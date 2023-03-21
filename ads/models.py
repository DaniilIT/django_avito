from django.db import models


class Ads(models.Model):
    name = models.CharField(max_length=40)
    author = models.CharField(max_length=40)
    # author_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    price = models.PositiveIntegerField()  # DecimalField(max_digits=15, decimal_places=2, null=True)
    description = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=200)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Category(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40, db_index=True)

    def __str__(self):
        return self.name
