# Generated by Django 4.0.5 on 2022-07-25 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0005_perfil_delete_lugares_alter_post_fragmento'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='images/perfil/'),
        ),
        migrations.AddField(
            model_name='perfil',
            name='facebook_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='perfil',
            name='instagram_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='perfil',
            name='twitter_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='perfil',
            name='website_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
