# Generated by Django 3.2.6 on 2021-08-08 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_rename_scope_article_tag'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ArticleScopeTag',
            new_name='Scopes',
        ),
    ]
