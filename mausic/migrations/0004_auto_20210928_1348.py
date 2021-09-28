# Generated by Django 3.2.7 on 2021-09-28 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mausic', '0003_alter_music_size'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('video', models.FileField(null=True, upload_to='video/')),
            ],
        ),
        migrations.AlterModelOptions(
            name='music',
            options={},
        ),
        migrations.RemoveField(
            model_name='music',
            name='downloaded',
        ),
        migrations.RemoveField(
            model_name='music',
            name='single',
        ),
        migrations.RemoveField(
            model_name='music',
            name='size',
        ),
        migrations.AddField(
            model_name='music',
            name='music',
            field=models.FileField(null=True, upload_to='music/'),
        ),
        migrations.DeleteModel(
            name='Singer',
        ),
    ]
