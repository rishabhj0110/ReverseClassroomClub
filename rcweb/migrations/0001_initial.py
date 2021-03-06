# Generated by Django 3.0.5 on 2021-03-27 15:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('sub', models.CharField(max_length=500)),
                ('msg', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ctitle', models.CharField(max_length=200)),
                ('cdesc', models.CharField(max_length=1000)),
                ('cdoclink', models.URLField(max_length=500)),
                ('ciname', models.CharField(max_length=200)),
                ('cidesc', models.CharField(max_length=1000)),
                ('cilink', models.URLField(max_length=500)),
                ('csdate', models.CharField(max_length=150)),
                ('cedate', models.CharField(max_length=150)),
                ('ctime', models.CharField(max_length=150)),
                ('capply', models.URLField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Emailsystem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=200)),
                ('sub', models.CharField(max_length=500)),
                ('msg', models.CharField(max_length=1000)),
                ('time', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=150)),
                ('desc', models.CharField(max_length=1000)),
                ('qual', models.CharField(max_length=1000)),
                ('link', models.URLField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Ngo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ngoname', models.CharField(max_length=200)),
                ('ngodetails', models.CharField(max_length=1000)),
                ('ntitle', models.CharField(max_length=200)),
                ('ndesc', models.CharField(max_length=1000)),
                ('ndoclink', models.URLField(max_length=500)),
                ('niname', models.CharField(max_length=200)),
                ('nidesc', models.CharField(max_length=1000)),
                ('nilink', models.URLField(max_length=500)),
                ('nsdate', models.CharField(max_length=150)),
                ('nedate', models.CharField(max_length=150)),
                ('ntime', models.CharField(max_length=150)),
                ('napply', models.URLField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='SignUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150)),
                ('password', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phoneno', models.CharField(max_length=100)),
                ('pemail', models.EmailField(max_length=254)),
                ('descr', models.CharField(max_length=1000)),
                ('year', models.CharField(max_length=100)),
                ('degree', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=500)),
                ('college', models.CharField(max_length=300)),
                ('link', models.URLField(max_length=300)),
                ('utype', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('etitle', models.CharField(max_length=200)),
                ('edesc', models.CharField(max_length=1000)),
                ('edoclink', models.URLField(max_length=500)),
                ('einame', models.CharField(max_length=200)),
                ('eidesc', models.CharField(max_length=1000)),
                ('eilink', models.URLField(max_length=500)),
                ('edate', models.CharField(max_length=150)),
                ('etime', models.CharField(max_length=150)),
                ('eapply', models.URLField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usernames', models.CharField(max_length=200)),
                ('phoneno', models.CharField(max_length=150)),
                ('pemail', models.EmailField(max_length=254)),
                ('college', models.CharField(max_length=250)),
                ('degree', models.CharField(max_length=150)),
                ('year', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=500)),
                ('desc', models.CharField(max_length=1000)),
                ('link', models.URLField(max_length=500)),
                ('utype', models.CharField(max_length=150)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
