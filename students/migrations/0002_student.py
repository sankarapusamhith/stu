# Generated by Django 4.1.7 on 2023-03-14 17:48

from django.db import migrations


def create_data(apps, schema_editor):
    Student = apps.get_model('students', 'Student')
    Student(name="Sam Harper", email="sam@email.com", age="23", phone="00000000").save()

class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_data),
    ]