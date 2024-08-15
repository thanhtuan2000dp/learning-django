# Generated by Django 5.1 on 2024-08-15 15:50

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='online course', max_length=100)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='john', max_length=30)),
                ('last_name', models.CharField(default='doe', max_length=30)),
                ('dob', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='related_objects.user')),
                ('full_time', models.BooleanField(default=True)),
                ('total_learners', models.IntegerField()),
            ],
            bases=('related_objects.user',),
        ),
        migrations.CreateModel(
            name='Learner',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='related_objects.user')),
                ('occupation', models.CharField(choices=[('student', 'Student'), ('developer', 'Developer'), ('data_scientist', 'Data Scientist'), ('dba', 'Database Admin')], default='student', max_length=20)),
                ('social_link', models.URLField()),
            ],
            bases=('related_objects.user',),
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='title', max_length=200)),
                ('content', models.TextField()),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='related_objects.course')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='instructors',
            field=models.ManyToManyField(to='related_objects.instructor'),
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_enrolled', models.DateField(default=django.utils.timezone.now)),
                ('mode', models.CharField(choices=[('audit', 'Audit'), ('honor', 'Honor')], default='audit', max_length=5)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='related_objects.course')),
                ('learner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='related_objects.learner')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='learners',
            field=models.ManyToManyField(through='related_objects.Enrollment', to='related_objects.learner'),
        ),
    ]
