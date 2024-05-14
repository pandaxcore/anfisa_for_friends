# Generated by Django 3.2.16 on 2023-01-31 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ice_cream', '0004_auto_20221230_0039'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('output_order',), 'verbose_name': 'категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='icecream',
            options={'verbose_name': 'мороженое', 'verbose_name_plural': 'Мороженое'},
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=64, unique=True, verbose_name='Слаг'),
        ),
        migrations.AlterField(
            model_name='topping',
            name='slug',
            field=models.SlugField(max_length=64, unique=True, verbose_name='Слаг'),
        ),
    ]