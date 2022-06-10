from django.db import models


class ProductModel(models.Model):
    class Meta:
        db_table = "Product"

    product_name = models.CharField(max_length=256)
    product_category = models.CharField(max_length=256)
    image = models.CharField(max_length=256)
    description = models.TextField(max_length=256)
    price = models.CharField(max_length=256)
    inventory = models.CharField(max_length=256)


class CategoryModel(models.Model):
    class Meta:
        db_table = "Category"

    category = models.ForeignKey(ProductModel, max_length=256)


class OrderStatusModel(models.Model):
    class Meta:
        db_table = "OrderStatus"

    order_complete = models.CharField(max_length=256)
    payment_complete = models.CharField(max_length=256)
    cancellation = models.CharField(max_length=256)
    delivery_departure = models.CharField(max_length=256)
    delivery_complete = models.CharField(max_length=256)