# Generated by Django 2.1.7 on 2019-03-22 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0004_auto_20190322_0719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountdetail',
            name='account_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='accountdetail',
            name='account_type',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='accountdetail',
            name='bank_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]