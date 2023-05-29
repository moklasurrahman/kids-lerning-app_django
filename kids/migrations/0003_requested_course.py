# Generated by Django 4.0.6 on 2022-09-10 18:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('kids', '0002_alter_course_options_remove_course_publish_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='requested_course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'requested_course',
            },
        ),
    ]
