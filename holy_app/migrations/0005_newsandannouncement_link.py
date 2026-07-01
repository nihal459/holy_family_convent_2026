from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('holy_app', '0004_ytvideo_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsandannouncement',
            name='link',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]
