# Generated by Django 3.1.3 on 2022-03-03 12:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('database_main', '0001_initial'),
        ('database_general', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='society',
            name='society_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='society_category', to='database_general.tag'),
        ),
        migrations.AddField(
            model_name='society',
            name='society_college',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='society_college', to='database_main.college'),
        ),
        migrations.AddField(
            model_name='society',
            name='society_tags',
            field=models.ManyToManyField(blank=True, related_name='society_tags', to='database_general.Tag'),
        ),
        migrations.AddField(
            model_name='faculty',
            name='faculty_user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='faculty_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='college',
            name='college_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='college_address', to='database_general.address'),
        ),
    ]