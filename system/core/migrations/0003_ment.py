

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_medical'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approved', models.BooleanField(default=False)),
                ('time', models.CharField(max_length=200, null=True)),
                ('ment_day', models.DateTimeField(null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dor', to=settings.AUTH_USER_MODEL)),
                ('medical', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='medical', to='core.Medical')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pat', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
