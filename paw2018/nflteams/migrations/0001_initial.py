# Generated by Django 2.0.8 on 2018-08-30 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('conference', models.CharField(choices=[('AFC', 'AFC'), ('NFC', 'NFC')], max_length=3)),
                ('division', models.CharField(choices=[('East', 'East'), ('North', 'North'), ('South', 'South'), ('West', 'West')], max_length=10)),
            ],
        ),
    ]
