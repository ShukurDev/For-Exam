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
    categoryid = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    price = models.DecimalField(max_digits=50, decimal_places=2)
    description = models.TextField()
    barcode = models.CharField(max_length=100)

    # created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'exam_product'
    # @property
    # def total_product(self):
    #     return self.name.count
    #
    # def total_summa(self):
    #     return sum(self.price)
    # def __str__(self):
    #     return self.name


class Deliver(models.Model):
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=150)
    adress = models.CharField(max_length=150)

    class Meta:
        db_table = 'exam_deliver'

    def __str__(self):
        return self.name


class Order(models.Model):
    product = models.ForeignKey(Product, related_name='orders', on_delete=models.CASCADE)
    jami_soni = models.IntegerField(null=True, blank=True)
    deliver = models.ForeignKey(Deliver, on_delete=models.CASCADE, null=True)
    base_price = models.DecimalField(max_digits=50, decimal_places=10)
    price = models.DecimalField(max_digits=50, decimal_places=2)

    # expired = models.DateField()
    # created_at = models.DateTimeField(auto_now_add=True)

    # class Meta:
    #     db_table = 'exam_order'
    def product_name(self):
        return self.product.name

    def jami_summa(self):
        total = self.price * self.jami_soni
        return total

    def foyda(self):
        return self.price - self.base_price
