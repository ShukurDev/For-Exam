from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        db_table = 'exam_category'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    price = models.DecimalField(max_digits=50, decimal_places=2)
    description = models.TextField()
    barcode = models.CharField(max_length=100)
    #created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'exam_product' 

    def __str__(self):
        return self.name


class Deliver(models.Model):
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=150)
    adress = models.CharField(max_length=150)

    class Meta:
        db_table = 'exam_deliver'
    def __str__(self):
        return self.name


class Order(models.Model):
    product = models.ForeignKey(Product,related_name='orders' ,on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True, blank=True)
    deliver = models.ForeignKey(Deliver, on_delete=models.CASCADE, null=True)
    base_price = models.DecimalField(max_digits=50, decimal_places=10)
    price = models.DecimalField(max_digits=50, decimal_places=2)
    #expired = models.DateField()
    #created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'exam_order'

    def get_total(self):
        total = self.price * self.quantity
        return total
