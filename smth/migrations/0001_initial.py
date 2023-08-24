# Generated by Django 4.2.4 on 2023-08-24 13:03

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
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('text', models.TextField()),
                ('category', models.CharField(choices=[('tank', 'Танки'), ('heal', 'Хиллеры'), ('dd', 'ДемеджДиллеры'), ('buyers', 'Торговцы'), ('guildmaster', 'Гилдмастеры'), ('quest', 'Квестгиверы'), ('smith', 'Кузнецы'), ('tanner', 'Кожевенники'), ('potion', 'Зельевары'), ('spellmaster', 'Мастера заклинаний')], default='quest', max_length=12)),
                ('upload', models.FileField(upload_to='uploads/')),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('status', models.BooleanField(default=False)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smth.article')),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
