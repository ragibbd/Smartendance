

import attendence_sys.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendence_sys', '0004_auto_20200626_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=attendence_sys.models.user_directory_path),
        ),
    ]
