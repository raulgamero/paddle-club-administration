# Generated by Django 4.2 on 2023-05-02 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('list_price', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('cost_price', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('salable', models.BooleanField()),
            ],
        ),
    ]
