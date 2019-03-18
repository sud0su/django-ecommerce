# Generated by Django 2.1.7 on 2019-03-18 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Name')),
                ('type', models.CharField(blank=True, choices=[('text', 'Text'), ('textarea', 'Text Area'), ('date', 'Date'), ('multiple_select', 'Multiple Select'), ('dropdown', 'Dropdown'), ('media', 'Media')], max_length=50, null=True, verbose_name='Type')),
            ],
            options={
                'db_table': 'attributes',
            },
        ),
        migrations.CreateModel(
            name='AttributeAttributeSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='attribute.Attribute')),
            ],
        ),
        migrations.CreateModel(
            name='AttributeSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Name')),
            ],
            options={
                'db_table': 'attribute_set',
            },
        ),
        migrations.CreateModel(
            name='AttributeValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(blank=True, max_length=100, null=True, verbose_name='Value')),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='attribute.Attribute')),
            ],
            options={
                'db_table': 'attribute_value',
            },
        ),
        migrations.AddField(
            model_name='attributeattributeset',
            name='attributeset',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='attribute.AttributeSet'),
        ),
    ]
