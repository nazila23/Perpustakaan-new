# Generated by Django 3.2.8 on 2022-02-02 07:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main2', '0005_auto_20220201_2244'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kembali',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tgl_pinjam', models.DateField(auto_now_add=True)),
                ('tgl_kembali', models.DateField(auto_now=True)),
                ('denda', models.CharField(max_length=200)),
                ('judul', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main2.buku')),
                ('no_panggil', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main2.exemplar')),
            ],
        ),
    ]