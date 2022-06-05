from django.db import models

# Create your models here.
class ProductItem(models.Model):
    product_name = models.CharField(max_length=300)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    ordered_quantity = models.PositiveIntegerField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    @property
    def dollar_amount(self):
        return "$%s" % self.product_price if self.product_price else ""

   
    def save(self, *args, **kwargs):
        self.total_amount = self.product_price*self.ordered_quantity
        super(ProductItem, self).save(*args, **kwargs)

    def __str__(self):
        return self.product_name    

    