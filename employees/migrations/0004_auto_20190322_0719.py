# Generated by Django 2.1.7 on 2019-03-22 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_auto_20190321_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountdetail',
            name='account_number',
            field=models.IntegerField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='accountdetail',
            name='account_type',
            field=models.CharField(blank=True, default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='accountdetail',
            name='bank_name',
            field=models.CharField(blank=True, default=1, max_length=100),
            preserve_default=False,
        ),
    ]