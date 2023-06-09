

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendence_sys', '0007_faculty_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendence',
            name='faculty',
        ),
        migrations.RemoveField(
            model_name='attendence',
            name='student',
        ),
        migrations.AddField(
            model_name='attendence',
            name='Faculty_Name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='attendence',
            name='Student_ID',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='attendence',
            name='period',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='attendence',
            name='status',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
