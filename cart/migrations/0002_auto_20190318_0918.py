# Generated by Django 2.1.7 on 2019-03-18 09:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cart', '0001_initial'),
        ('references', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartrulescustomers',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cartrulescombinations',
            name='cart_rule_id1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='cart_rule_id1', to='cart.CartRules'),
        ),
        migrations.AddField(
            model_name='cartrulescombinations',
            name='cart_rule_id2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='cart_rule_id2', to='cart.CartRules'),
        ),
        migrations.AddField(
            model_name='cartrulescategories',
            name='cart_rule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cart.CartRules'),
        ),
        migrations.AddField(
            model_name='cartrulescategories',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='references.Categories'),
        ),
        migrations.AddField(
            model_name='cartrules',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cartrules',
            name='gift_product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='products.Product'),
        ),
        migrations.AddField(
            model_name='cartrules',
            name='minimum_ammount_currency_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='minimum_ammount_currency_id', to='references.Currencies'),
        ),
        migrations.AddField(
            model_name='cartrules',
            name='reduction_currency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='reduction_currency', to='references.Currencies'),
        ),
    ]