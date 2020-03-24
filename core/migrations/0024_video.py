# Generated by Django 2.2.6 on 2020-03-24 01:41

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('core', '0023_merge_20200324_0050'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round', models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, 'VO'), (7, 'VQ'), (8, 'VS'), (9, 'VF'), (10, 'NQ'), (11, 'NS'), (12, 'NF')], default=0)),
                ('case', models.TextField()),
                ('description', models.TextField()),
                ('link', models.CharField(max_length=4096)),
                ('password', models.CharField(blank=True, max_length=1024)),
                ('permissions', models.IntegerField(choices=[(0, 'All'), (1, 'Accounts Only'), (2, 'Debaters in Round')], default=2)),
                ('lo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lo_videos', to='core.Debater')),
                ('mg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mg_videos', to='core.Debater')),
                ('mo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mo_videos', to='core.Debater')),
                ('pm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pm_videos', to='core.Debater')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='core.Tournament')),
            ],
        ),
    ]