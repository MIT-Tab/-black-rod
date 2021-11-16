# Generated by Django 3.1.6 on 2021-11-16 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0035_auto_20211116_1926'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AddField(
            model_name='user',
            name='can_view_private_videos',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='coty',
            name='season',
            field=models.CharField(choices=[('2021', '2021-22'), ('2020', '2020-21'), ('2019', '2019-20'), ('2018', '2018-19'), ('2017', '2017-18'), ('2016', '2016-17'), ('2015', '2015-16'), ('2014', '2014-15'), ('2013', '2013-14'), ('2012', '2012-13'), ('2011', '2011-12'), ('2010', '2010-11'), ('2009', '2009-10'), ('2008', '2008-09'), ('2007', '2007-08'), ('2006', '2006-07'), ('2005', '2005-06')], default='2021', max_length=16),
        ),
        migrations.AlterField(
            model_name='noty',
            name='season',
            field=models.CharField(choices=[('2021', '2021-22'), ('2020', '2020-21'), ('2019', '2019-20'), ('2018', '2018-19'), ('2017', '2017-18'), ('2016', '2016-17'), ('2015', '2015-16'), ('2014', '2014-15'), ('2013', '2013-14'), ('2012', '2012-13'), ('2011', '2011-12'), ('2010', '2010-11'), ('2009', '2009-10'), ('2008', '2008-09'), ('2007', '2007-08'), ('2006', '2006-07'), ('2005', '2005-06')], default='2021', max_length=16),
        ),
        migrations.AlterField(
            model_name='onlinequal',
            name='season',
            field=models.CharField(choices=[('2021', '2021-22'), ('2020', '2020-21'), ('2019', '2019-20'), ('2018', '2018-19'), ('2017', '2017-18'), ('2016', '2016-17'), ('2015', '2015-16'), ('2014', '2014-15'), ('2013', '2013-14'), ('2012', '2012-13'), ('2011', '2011-12'), ('2010', '2010-11'), ('2009', '2009-10'), ('2008', '2008-09'), ('2007', '2007-08'), ('2006', '2006-07'), ('2005', '2005-06')], default='2021', max_length=16),
        ),
        migrations.AlterField(
            model_name='qual',
            name='season',
            field=models.CharField(choices=[('2021', '2021-22'), ('2020', '2020-21'), ('2019', '2019-20'), ('2018', '2018-19'), ('2017', '2017-18'), ('2016', '2016-17'), ('2015', '2015-16'), ('2014', '2014-15'), ('2013', '2013-14'), ('2012', '2012-13'), ('2011', '2011-12'), ('2010', '2010-11'), ('2009', '2009-10'), ('2008', '2008-09'), ('2007', '2007-08'), ('2006', '2006-07'), ('2005', '2005-06')], default='2021', max_length=16),
        ),
        migrations.AlterField(
            model_name='qualpoints',
            name='season',
            field=models.CharField(choices=[('2021', '2021-22'), ('2020', '2020-21'), ('2019', '2019-20'), ('2018', '2018-19'), ('2017', '2017-18'), ('2016', '2016-17'), ('2015', '2015-16'), ('2014', '2014-15'), ('2013', '2013-14'), ('2012', '2012-13'), ('2011', '2011-12'), ('2010', '2010-11'), ('2009', '2009-10'), ('2008', '2008-09'), ('2007', '2007-08'), ('2006', '2006-07'), ('2005', '2005-06')], default='2021', max_length=16),
        ),
        migrations.AlterField(
            model_name='soty',
            name='season',
            field=models.CharField(choices=[('2021', '2021-22'), ('2020', '2020-21'), ('2019', '2019-20'), ('2018', '2018-19'), ('2017', '2017-18'), ('2016', '2016-17'), ('2015', '2015-16'), ('2014', '2014-15'), ('2013', '2013-14'), ('2012', '2012-13'), ('2011', '2011-12'), ('2010', '2010-11'), ('2009', '2009-10'), ('2008', '2008-09'), ('2007', '2007-08'), ('2006', '2006-07'), ('2005', '2005-06')], default='2021', max_length=16),
        ),
        migrations.AlterField(
            model_name='toty',
            name='season',
            field=models.CharField(choices=[('2021', '2021-22'), ('2020', '2020-21'), ('2019', '2019-20'), ('2018', '2018-19'), ('2017', '2017-18'), ('2016', '2016-17'), ('2015', '2015-16'), ('2014', '2014-15'), ('2013', '2013-14'), ('2012', '2012-13'), ('2011', '2011-12'), ('2010', '2010-11'), ('2009', '2009-10'), ('2008', '2008-09'), ('2007', '2007-08'), ('2006', '2006-07'), ('2005', '2005-06')], default='2021', max_length=16),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='season',
            field=models.CharField(choices=[('2021', '2021-22'), ('2020', '2020-21'), ('2019', '2019-20'), ('2018', '2018-19'), ('2017', '2017-18'), ('2016', '2016-17'), ('2015', '2015-16'), ('2014', '2014-15'), ('2013', '2013-14'), ('2012', '2012-13'), ('2011', '2011-12'), ('2010', '2010-11'), ('2009', '2009-10'), ('2008', '2008-09'), ('2007', '2007-08'), ('2006', '2006-07'), ('2005', '2005-06')], default='2021', max_length=16),
        ),
    ]
