# Generated by Django 5.2.1 on 2025-05-22 23:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nestedcomment',
            name='parent_comment',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='nested_comments', to='comments.basecomment'),
        ),
    ]
