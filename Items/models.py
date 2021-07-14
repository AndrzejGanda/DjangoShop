from django.db import models


class Creator(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=60)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = "Creator"
        verbose_name_plural = "Creators"


class Category(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Items(models.Model):
    def __str__(self):
        return self.name

    # budujemy relacje
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)
    statistics = models.TextField(blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"


