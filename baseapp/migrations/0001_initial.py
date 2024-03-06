# Generated by Django 5.0.3 on 2024-03-06 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VisitorDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visitor_name', models.CharField(max_length=100)),
                ('visitor_location', models.CharField(max_length=255)),
                ('visitor_mobile_number', models.CharField(max_length=15)),
            ],
        ),
    ]
