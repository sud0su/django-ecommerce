# Generated by Django 2.1.7 on 2019-03-25 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carrier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Name')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=13, null=True, verbose_name='Price')),
                ('delivery_text', models.CharField(blank=True, max_length=255, null=True, verbose_name='Delivery Text')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='uploads/carriers/logo/')),
            ],
            options={
                'db_table': 'carriers',
            },
        ),
    ]
