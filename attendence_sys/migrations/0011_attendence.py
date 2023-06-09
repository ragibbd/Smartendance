

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendence_sys', '0010_delete_attendence'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Faculty_Name', models.CharField(blank=True, max_length=200, null=True)),
                ('Student_ID', models.CharField(blank=True, max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now=True, null=True)),
                ('period', models.CharField(max_length=200, null=True)),
                ('status', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
