# Generated by Django 2.1.7 on 2019-03-18 09:18

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartRules',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, null=True, verbose_name='Name')),
                ('code', models.CharField(blank=True, max_length=100, null=True, verbose_name='Code')),
                ('priority', models.IntegerField(blank=True, null=True, verbose_name='Priority')),
                ('start_date', models.DateTimeField(auto_now=True, verbose_name='Start Date')),
                ('expiration_date', models.DateTimeField(verbose_name='Expiration Date')),
                ('status', models.BooleanField(default=0, verbose_name='Status')),
                ('highlight', models.BooleanField(default=0, verbose_name='Highlight')),
                ('minimum_amount', models.IntegerField(default=0, verbose_name='Minimum Amount')),
                ('free_delivery', models.BooleanField(default=0, verbose_name='Free Delivery')),
                ('total_available', models.IntegerField(blank=True, null=True, verbose_name='Total Available')),
                ('total_available_each_user', models.IntegerField(blank=True, null=True, verbose_name='Total Available Each User')),
                ('promo_label', models.CharField(blank=True, max_length=250, null=True, verbose_name='Promo Label')),
                ('promo_text', models.TextField(blank=True, null=True, verbose_name='Promo Text')),
                ('multiply_gift', models.IntegerField(default=1, verbose_name='Multiply Gift')),
                ('min_nr_products', models.IntegerField(default=0, verbose_name='Min Nr Products')),
                ('discount_type', models.CharField(choices=[(0, 'Percent - order'), (1, 'Percent - selected products'), (2, 'Percent - cheapest product'), (3, 'Percent - most expensive product'), (4, 'Amount - order')], default=0, max_length=1, verbose_name='Discount Type')),
                ('reduction_amount', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=13, verbose_name='Reduction Amount')),
            ],
            options={
                'db_table': 'cart_rules',
            },
        ),
        migrations.CreateModel(
            name='CartRulesCategories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CartRulesCombinations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CartRulesCustomers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('cart_rule', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cart.CartRules')),
            ],
        ),
        migrations.CreateModel(
            name='CartRulesProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('cart_rule', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cart.CartRules')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='products.Product')),
            ],
        ),
        migrations.CreateModel(
            name='CartRulesProductsGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('cart_rule', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cart.CartRules')),
                ('product_group', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='products.ProductGroups')),
            ],
        ),
    ]