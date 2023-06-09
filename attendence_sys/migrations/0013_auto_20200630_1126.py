

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendence_sys', '0012_auto_20200629_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendence',
            name='branch',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='attendence',
            name='section',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='attendence',
            name='year',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='attendence',
            name='status',
            field=models.CharField(default='Absent', max_length=200, null=True),
        ),
    ]
