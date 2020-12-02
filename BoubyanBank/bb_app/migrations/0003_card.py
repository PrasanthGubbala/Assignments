# Generated by Django 3.1.1 on 2020-11-26 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bb_app', '0002_auto_20201126_1800'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('card_no', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bb_app.user')),
            ],
        ),
    ]