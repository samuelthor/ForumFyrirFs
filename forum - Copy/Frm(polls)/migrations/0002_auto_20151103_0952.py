# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Frm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.RenameModel(
            old_name='Question',
            new_name='Post',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='question',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='question_text',
            new_name='post_text',
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(to='Frm.Post'),
        ),
    ]
