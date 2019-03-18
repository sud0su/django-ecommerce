from django.db import models
from django.utils.translation import gettext as _
from decimal import Decimal
# Create your models here.

class Taxes(models.Model):
    name = models.CharField(_("Name"), max_length=100, blank=True, null=True)
    value = models.DecimalField(_("Value"), max_digits=13, decimal_places=2, default=Decimal('0.00'))

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'ref_taxes'

class Currencies(models.Model):
    name = models.CharField(_("Name"), max_length=100, blank=True, null=True)
    iso = models.CharField(_("ISO"), max_length=50, blank=True, null=True)
    value = models.DecimalField(_("Value"), max_digits=13, decimal_places=2, blank=True, null=True)
    default = models.IntegerField(_("Default"), default=0)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'ref_currencies'

class Countries(models.Model):
    code = models.CharField(_("Country Code"), max_length=50, blank=True, null=True)
    name = models.CharField(_("Name"), max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'ref_countries'


class Provinces(models.Model):
    code = models.CharField(_("Province Code"), max_length=50, blank=True, null=True)
    name = models.CharField(_("Name"), max_length=100, blank=True, null=True)
    country = models.ForeignKey(Countries, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'ref_provinces'

class District(models.Model):
    code = models.CharField(_("District Code"), max_length=50, blank=True, null=True)
    name = models.CharField(_("Name"), max_length=100, blank=True, null=True)
    province = models.ForeignKey(Provinces, on_delete=models.DO_NOTHING, related_name="province")

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'ref_districts'

class Categories(models.Model):
    parent_id = models.IntegerField(_("Parent Category"), null=True, default=0)
    name = models.CharField(_("Name"), max_length=100, blank=True, null=True)
    slug = models.SlugField(_("Slug"), max_length=100, blank=True, null=True)
    lft = models.IntegerField(_("Lft"), null=True, default=0)
    rgt = models.IntegerField(_("Rgt"), null=True, default=0)
    depth = models.IntegerField(_("Depth"), null=True, default=0)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'categories'

class Notifications(models.Model):
    name = models.CharField(_("Name"), max_length=100, blank=True, null=True)
    slug = models.SlugField(_("Slug"), max_length=100, blank=True, null=True)
    model = models.CharField(_("Model"), max_length=100, blank=True, null=True)
    body = models.TextField(_("Body"), blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'notifications'