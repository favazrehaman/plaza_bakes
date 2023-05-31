# Generated by Django 4.2.1 on 2023-05-30 14:53

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
            name='buy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
                ('discription', models.CharField(max_length=100)),
                ('image', models.FileField(upload_to='')),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('productname', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
                ('discription', models.CharField(max_length=100)),
                ('image', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='customerdetails1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_holder_name', models.CharField(max_length=50)),
                ('card_number', models.IntegerField()),
                ('date', models.CharField(max_length=50)),
                ('security_code', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='productmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shopid', models.IntegerField()),
                ('productname', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
                ('discription', models.CharField(max_length=100)),
                ('image', models.FileField(upload_to='myapp/static')),
            ],
        ),
        migrations.CreateModel(
            name='shopregmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_name', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=100)),
                ('idm', models.IntegerField()),
                ('mail', models.EmailField(max_length=254)),
                ('ph', models.IntegerField()),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('productname', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
                ('discription', models.CharField(max_length=100)),
                ('image', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auth_token', models.CharField(max_length=100)),
                ('is_verified', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]