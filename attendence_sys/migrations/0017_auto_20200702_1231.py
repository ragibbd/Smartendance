

import attendence_sys.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendence_sys', '0016_auto_20200702_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=attendence_sys.models.student_directory_path),
        ),
    ]
