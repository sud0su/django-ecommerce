from django.db import models
from decimal import Decimal
from django.utils.translation import gettext as _
from attribute.models import AttributeSet, Attribute
from references.models import Taxes, Categories

class ProductGroups(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'product_groups'

class Product(models.Model):
    name = models.CharField(_("Name"), max_length=100, blank=True, null=True)
    description = models.TextField(_("Description"), blank=True, null=True)
    price = models.DecimalField(_("Price"), max_digits=13, decimal_places=2, default=Decimal('0'))
    sku = models.CharField(_("SKU"), max_length=100, blank=True, null=True, unique=True)
    stock = models.IntegerField(_("Stock"), default=0)

    attribute = models.ForeignKey(AttributeSet, on_delete=models.DO_NOTHING)
    tax = models.ForeignKey(Taxes, on_delete=models.DO_NOTHING)
    group = models.ForeignKey(ProductGroups, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'products'

class ProductImages(models.Model):
    name = models.ImageField(_("Name"), upload_to='uploads/products/', null=True, blank=True)
    # name = models.CharField(_("Name"), max_length=100, blank=True, null=True)
    order = models.IntegerField(_("Order"))
    
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'product_images'


class AttributeProductValue(models.Model):
    value = models.CharField(_("Value"), max_length=100, blank=True, null=True)
    attribute = models.ForeignKey(Attribute, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.value

    class Meta:
        db_table = "attribute_product_value"

class CategoryProduct(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.DO_NOTHING)
    attributeset = models.ForeignKey(AttributeSet, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class SpesificPrice(models.Model):
    reduction = models.DecimalField(_("Reduction"), max_digits=13, decimal_places=2, default=Decimal('0'))
    DISCOUNT_TYPE = (
        (0, 'Ammount'),
        (1, 'Percent'),
    )
    discount_type = models.CharField(_("Discount Type"),choices=DISCOUNT_TYPE, max_length=1, default=0)
    start_date = models.DateTimeField(_("Start Date"),auto_now=True, editable=True)
    expiration_date = models.DateTimeField(_("Expiration Date"))
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'spesific_prices'

