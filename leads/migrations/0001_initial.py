# Generated by Django 3.1.6 on 2021-02-03 16:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sugarLevel', models.CharField(max_length=4)),
                ('dose', models.CharField(max_length=4)),
                ('takenAtDate', models.DateField(auto_now_add=True, null=True)),
                ('takenAtTime', models.TimeField(auto_now_add=True, null=True)),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='leads', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
