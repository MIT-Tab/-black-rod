# Generated by Django 2.2.6 on 2020-03-27 17:49

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='case',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='lo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lo_videos', to='core.Debater', verbose_name='LO'),
        ),
        migrations.AlterField(
            model_name='video',
            name='mg',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mg_videos', to='core.Debater', verbose_name='MG'),
        ),
        migrations.AlterField(
            model_name='video',
            name='mo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mo_videos', to='core.Debater', verbose_name='MO'),
        ),
        migrations.AlterField(
            model_name='video',
            name='password',
            field=models.CharField(blank=True, help_text='If needed', max_length=1024),
        ),
        migrations.AlterField(
            model_name='video',
            name='pm',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pm_videos', to='core.Debater', verbose_name='PM'),
        ),
        migrations.AlterField(
            model_name='video',
            name='round',
            field=models.IntegerField(choices=[(0, 'UNKNOWN'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (6, 'Varsity Octafinals'), (7, 'Varsity Quarterfinals'), (8, 'Varsity Semifinals'), (9, 'Varsity Finals'), (10, 'Novice Quarterfinals'), (11, 'Novice Semifinals'), (12, 'Novice Finals'), (13, 'Demo Round')], default=0),
        ),
        migrations.AlterField(
            model_name='video',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]