# Generated by Django 3.2.6 on 2021-08-23 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shopp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_name', models.TextField(max_length=200)),
                ('shop_price', models.IntegerField(default=0, max_length=3)),
                ('shop_dsc', models.CharField(max_length=200)),
            ],
        ),
    ]
