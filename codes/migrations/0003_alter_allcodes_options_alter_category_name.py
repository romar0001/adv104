# Generated by Django 4.0.3 on 2022-03-25 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codes', '0002_alter_category_options_alter_codes_code'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='allcodes',
            options={'ordering': ['-id']},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
