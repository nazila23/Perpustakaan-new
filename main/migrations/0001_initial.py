# Generated by Django 3.2.8 on 2022-01-30 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='usulan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=200)),
                ('pengarang', models.CharField(max_length=200)),
                ('tahun_terbit', models.DateField(auto_now_add=True)),
                ('penerbit', models.CharField(max_length=200)),
            ],
        ),
    ]
