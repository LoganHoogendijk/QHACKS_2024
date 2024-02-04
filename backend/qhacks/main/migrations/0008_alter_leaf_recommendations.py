# Generated by Django 3.2.23 on 2024-02-04 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_remove_leaf_crop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaf',
            name='recommendations',
            field=models.ManyToManyField(blank=True, related_name='leaves', to='main.Recommendation'),
        ),
    ]
