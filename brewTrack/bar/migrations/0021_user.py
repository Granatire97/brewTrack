# Generated by Django 2.1.1 on 2018-11-24 05:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0020_auto_20181124_0028'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='unknown', max_length=20)),
                ('password', models.CharField(default='unknown', max_length=20)),
                ('bar', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bar.Bar')),
            ],
        ),
    ]
