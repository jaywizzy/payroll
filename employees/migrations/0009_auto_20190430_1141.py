# Generated by Django 2.2 on 2019-04-30 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0008_auto_20190430_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='department',
            field=models.CharField(choices=[('Applications', 'Applications'), ('Network & Security', 'Network & Security'), ('Solutions', 'Solutions'), ('Sales', 'Sales'), ('Finance', 'Finance'), ('Infrastructure', 'Infrastructure'), ('Projects', 'Projects'), ('Research & Development', 'Research & Development')], max_length=100),
        ),
    ]
