

import attendence_sys.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendence_sys', '0015_auto_20200702_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='profile_pic',
            field=models.ImageField(blank=True, height_field='600', null=True, upload_to=attendence_sys.models.student_directory_path, width_field='600'),
        ),
    ]
