# Generated by Django 4.2.1 on 2023-08-16 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('dob', models.DateField()),
                ('grade', models.CharField(choices=[('BIM', 'Bachelor of Information Management'), ('BBM', 'Bachelor of Business Management'), ('BBA', 'Bachelor of Business Administration'), ('BCA', 'Bachelor of Computer Applications'), ('CSIT', 'Bachelor of Computer Science and Information Technology')], max_length=4)),
                ('semester', models.CharField(choices=[('1', '1st Semester'), ('2', '2nd Semester'), ('3', '3rd Semester'), ('4', '4th Semester'), ('5', '5th Semester'), ('6', '6th Semester'), ('7', '7th Semester'), ('8', '8th Semester')], max_length=1)),
                ('emailid', models.EmailField(max_length=254)),
                ('phone', models.BigIntegerField()),
                ('address', models.CharField(max_length=100)),
            ],
        ),
    ]