# Generated by Django 3.2.3 on 2021-11-02 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_profile_id'),
        ('blog', '0015_auto_20211025_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
    ]