# Generated by Django 2.2.6 on 2024-11-26 21:52

from django.db import migrations, models
from django.conf import settings

class Migration(migrations.Migration):
    
    dependencies = [
        ('core', '0036_auto_20211116_2047'),
    ]
    if settings.ENV == "DEV":
        operations = [
            migrations.AlterField(
            model_name='coty',
            name='season',
            field=models.CharField(choices=[('2019', '2019-20'), ('2018', '2018-19'), ('2017', '2017-18'), ('2016', '2016-17'), ('2015', '2015-16'), ('2014', '2014-15'), ('2013', '2013-14'), ('2012', '2012-13'), ('2011', '2011-12'), ('2010', '2010-11'), ('2009', '2009-10'), ('2008', '2008-09'), ('2007', '2007-08'), ('2006', '2006-07'), ('2005', '2005-06')], default='2019', max_length=16),
        ),
        migrations.AlterField(
            model_name='noty',
            name='season',
            field=models.CharField(choices=[('2019', '2019-20'), ('2018', '2018-19'), ('2017', '2017-18'), ('2016', '2016-17'), ('2015', '2015-16'), ('2014', '2014-15'), ('2013', '2013-14'), ('2012', '2012-13'), ('2011', '2011-12'), ('2010', '2010-11'), ('2009', '2009-10'), ('2008', '2008-09'), ('2007', '2007-08'), ('2006', '2006-07'), ('2005', '2005-06')], default='2019', max_length=16),
        ),
        migrations.AlterField(
            model_name='onlinequal',
            name='season',
            field=models.CharField(choices=[('2019', '2019-20'), ('2018', '2018-19'), ('2017', '2017-18'), ('2016', '2016-17'), ('2015', '2015-16'), ('2014', '2014-15'), ('2013', '2013-14'), ('2012', '2012-13'), ('2011', '2011-12'), ('2010', '2010-11'), ('2009', '2009-10'), ('2008', '2008-09'), ('2007', '2007-08'), ('2006', '2006-07'), ('2005', '2005-06')], default='2019', max_length=16),
        ),
        migrations.AlterField(
            model_name='qual',
            name='season',
            field=models.CharField(choices=[('2019', '2019-20'), ('2018', '2018-19'), ('2017', '2017-18'), ('2016', '2016-17'), ('2015', '2015-16'), ('2014', '2014-15'), ('2013', '2013-14'), ('2012', '2012-13'), ('2011', '2011-12'), ('2010', '2010-11'), ('2009', '2009-10'), ('2008', '2008-09'), ('2007', '2007-08'), ('2006', '2006-07'), ('2005', '2005-06')], default='2019', max_length=16),
        ),
        migrations.AlterField(
            model_name='qualpoints',
            name='season',
            field=models.CharField(choices=[('2019', '2019-20'), ('2018', '2018-19'), ('2017', '2017-18'), ('2016', '2016-17'), ('2015', '2015-16'), ('2014', '2014-15'), ('2013', '2013-14'), ('2012', '2012-13'), ('2011', '2011-12'), ('2010', '2010-11'), ('2009', '2009-10'), ('2008', '2008-09'), ('2007', '2007-08'), ('2006', '2006-07'), ('2005', '2005-06')], default='2019', max_length=16),
        ),
        migrations.AlterField(
            model_name='soty',
            name='season',
            field=models.CharField(choices=[('2019', '2019-20'), ('2018', '2018-19'), ('2017', '2017-18'), ('2016', '2016-17'), ('2015', '2015-16'), ('2014', '2014-15'), ('2013', '2013-14'), ('2012', '2012-13'), ('2011', '2011-12'), ('2010', '2010-11'), ('2009', '2009-10'), ('2008', '2008-09'), ('2007', '2007-08'), ('2006', '2006-07'), ('2005', '2005-06')], default='2019', max_length=16),
        ),
        migrations.AlterField(
            model_name='toty',
            name='season',
            field=models.CharField(choices=[('2019', '2019-20'), ('2018', '2018-19'), ('2017', '2017-18'), ('2016', '2016-17'), ('2015', '2015-16'), ('2014', '2014-15'), ('2013', '2013-14'), ('2012', '2012-13'), ('2011', '2011-12'), ('2010', '2010-11'), ('2009', '2009-10'), ('2008', '2008-09'), ('2007', '2007-08'), ('2006', '2006-07'), ('2005', '2005-06')], default='2019', max_length=16),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='season',
            field=models.CharField(choices=[('2019', '2019-20'), ('2018', '2018-19'), ('2017', '2017-18'), ('2016', '2016-17'), ('2015', '2015-16'), ('2014', '2014-15'), ('2013', '2013-14'), ('2012', '2012-13'), ('2011', '2011-12'), ('2010', '2010-11'), ('2009', '2009-10'), ('2008', '2008-09'), ('2007', '2007-08'), ('2006', '2006-07'), ('2005', '2005-06')], default='2019', max_length=16),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='first name'),
        ),
        ]
    elif settings.ENV == "PROD":
        operations = [
            migrations.AlterField(
                model_name='coty',
                name='season',
                field=models.CharField(choices=[('2025', '2025-26'), ('2024', '2024-25'), ('2023', '2023-24'), ('2022', '2022-23'), ('2021', '2021-22'), ('2020', '2020-21'), ('2019', '2019-20'), ('2018', '2018-19'), ('2017', '2017-18'), ('2016', '2016-17'), ('2015', '2015-16'), ('2014', '2014-15'), ('2013', '2013-14'), ('2012', '2012-13'), ('2011', '2011-12'), ('2010', '2010-11'), ('2009', '2009-10'), ('2008', '2008-09'), ('2007', '2007-08'), ('2006', '2006-07'), ('2005', '2005-06')], default='2023', max_length=16),
            ),
            migrations.AlterField(
                model_name='noty',
                name='season',
                field=models.CharField(choices=[('2025', '2025-26'), ('2024', '2024-25'), ('2023', '2023-24'), ('2022', '2022-23'), ('2021', '2021-22'), ('2020', '2020-21'), ('2019', '2019-20'), ('2018', '2018-19'), ('2017', '2017-18'), ('2016', '2016-17'), ('2015', '2015-16'), ('2014', '2014-15'), ('2013', '2013-14'), ('2012', '2012-13'), ('2011', '2011-12'), ('2010', '2010-11'), ('2009', '2009-10'), ('2008', '2008-09'), ('2007', '2007-08'), ('2006', '2006-07'), ('2005', '2005-06')], default='2023', max_length=16),
            ),
            migrations.AlterField(
                model_name='onlinequal',
                name='season',
                field=models.CharField(choices=[('2025', '2025-26'), ('2024', '2024-25'), ('2023', '2023-24'), ('2022', '2022-23'), ('2021', '2021-22'), ('2020', '2020-21'), ('2019', '2019-20'), ('2018', '2018-19'), ('2017', '2017-18'), ('2016', '2016-17'), ('2015', '2015-16'), ('2014', '2014-15'), ('2013', '2013-14'), ('2012', '2012-13'), ('2011', '2011-12'), ('2010', '2010-11'), ('2009', '2009-10'), ('2008', '2008-09'), ('2007', '2007-08'), ('2006', '2006-07'), ('2005', '2005-06')], default='2023', max_length=16),
            ),
            migrations.AlterField(
                model_name='qual',
                name='season',
                field=models.CharField(choices=[('2025', '2025-26'), ('2024', '2024-25'), ('2023', '2023-24'), ('2022', '2022-23'), ('2021', '2021-22'), ('2020', '2020-21'), ('2019', '2019-20'), ('2018', '2018-19'), ('2017', '2017-18'), ('2016', '2016-17'), ('2015', '2015-16'), ('2014', '2014-15'), ('2013', '2013-14'), ('2012', '2012-13'), ('2011', '2011-12'), ('2010', '2010-11'), ('2009', '2009-10'), ('2008', '2008-09'), ('2007', '2007-08'), ('2006', '2006-07'), ('2005', '2005-06')], default='2023', max_length=16),
            ),
            migrations.AlterField(
                model_name='qualpoints',
                name='season',
                field=models.CharField(choices=[('2025', '2025-26'), ('2024', '2024-25'), ('2023', '2023-24'), ('2022', '2022-23'), ('2021', '2021-22'), ('2020', '2020-21'), ('2019', '2019-20'), ('2018', '2018-19'), ('2017', '2017-18'), ('2016', '2016-17'), ('2015', '2015-16'), ('2014', '2014-15'), ('2013', '2013-14'), ('2012', '2012-13'), ('2011', '2011-12'), ('2010', '2010-11'), ('2009', '2009-10'), ('2008', '2008-09'), ('2007', '2007-08'), ('2006', '2006-07'), ('2005', '2005-06')], default='2023', max_length=16),
            ),
            migrations.AlterField(
                model_name='soty',
                name='season',
                field=models.CharField(choices=[('2025', '2025-26'), ('2024', '2024-25'), ('2023', '2023-24'), ('2022', '2022-23'), ('2021', '2021-22'), ('2020', '2020-21'), ('2019', '2019-20'), ('2018', '2018-19'), ('2017', '2017-18'), ('2016', '2016-17'), ('2015', '2015-16'), ('2014', '2014-15'), ('2013', '2013-14'), ('2012', '2012-13'), ('2011', '2011-12'), ('2010', '2010-11'), ('2009', '2009-10'), ('2008', '2008-09'), ('2007', '2007-08'), ('2006', '2006-07'), ('2005', '2005-06')], default='2023', max_length=16),
            ),
            migrations.AlterField(
                model_name='toty',
                name='season',
                field=models.CharField(choices=[('2025', '2025-26'), ('2024', '2024-25'), ('2023', '2023-24'), ('2022', '2022-23'), ('2021', '2021-22'), ('2020', '2020-21'), ('2019', '2019-20'), ('2018', '2018-19'), ('2017', '2017-18'), ('2016', '2016-17'), ('2015', '2015-16'), ('2014', '2014-15'), ('2013', '2013-14'), ('2012', '2012-13'), ('2011', '2011-12'), ('2010', '2010-11'), ('2009', '2009-10'), ('2008', '2008-09'), ('2007', '2007-08'), ('2006', '2006-07'), ('2005', '2005-06')], default='2023', max_length=16),
            ),
            migrations.AlterField(
                model_name='tournament',
                name='season',
                field=models.CharField(choices=[('2025', '2025-26'), ('2024', '2024-25'), ('2023', '2023-24'), ('2022', '2022-23'), ('2021', '2021-22'), ('2020', '2020-21'), ('2019', '2019-20'), ('2018', '2018-19'), ('2017', '2017-18'), ('2016', '2016-17'), ('2015', '2015-16'), ('2014', '2014-15'), ('2013', '2013-14'), ('2012', '2012-13'), ('2011', '2011-12'), ('2010', '2010-11'), ('2009', '2009-10'), ('2008', '2008-09'), ('2007', '2007-08'), ('2006', '2006-07'), ('2005', '2005-06')], default='2023', max_length=16),
            ),
            migrations.AlterField(
                model_name='user',
                name='first_name',
                field=models.CharField(blank=True, max_length=30, verbose_name='first name'),
            ),
        ]