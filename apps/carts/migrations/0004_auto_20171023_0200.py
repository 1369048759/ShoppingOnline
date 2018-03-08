# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-10-23 02:00
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('carts', '0003_cartforuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartsForUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RenameModel(
            old_name='CartForVisitor',
            new_name='CartsInfo',
        ),
        migrations.RemoveField(
            model_name='cartforuser',
            name='user',
        ),
        migrations.DeleteModel(
            name='CartForUser',
        ),
        migrations.AddField(
            model_name='cartsforuser',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carts.CartsInfo', verbose_name='购物车'),
        ),
        migrations.AddField(
            model_name='cartsforuser',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
    ]