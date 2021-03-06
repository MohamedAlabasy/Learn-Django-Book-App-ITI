# Generated by Django 4.0.4 on 2022-04-21 23:39

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('details', models.CharField(max_length=250, null=True)),
                ('image', models.URLField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('summary', models.CharField(max_length=250)),
                ('publish_date', models.DateTimeField(auto_now_add=True)),
                ('image', models.URLField()),
                ('add_to_site', models.DateTimeField(default=django.utils.timezone.now)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('appropriate', models.CharField(choices=[('und', 'under 18'), ('ad', 'Adults')], default='ad', max_length=250)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.author')),
            ],
        ),
    ]
