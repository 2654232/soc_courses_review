# Generated by Django 2.2.28 on 2023-03-09 20:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('Course_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=34)),
                ('Tag', models.CharField(max_length=34)),
                ('Description', models.CharField(max_length=2000)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name_plural': 'Courses',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('Review_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Rating', models.IntegerField(default=0)),
                ('comment', models.CharField(max_length=2000)),
                ('Course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviewer.Course')),
            ],
        ),
    ]
