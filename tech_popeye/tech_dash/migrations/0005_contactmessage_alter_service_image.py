# Generated by Django 4.2.1 on 2023-06-10 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tech_dash', '0004_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(upload_to='static/img/service_images'),
        ),
    ]
