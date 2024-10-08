# Generated by Django 5.0.7 on 2024-08-27 15:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Demo', '0002_alter_unimajor_subject_combination_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Combination',
            fields=[
                ('ID', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('ID', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameField(
            model_name='unimajor',
            old_name='Name',
            new_name='M_Name',
        ),
        migrations.RemoveField(
            model_name='unimajor',
            name='Score',
        ),
        migrations.RemoveField(
            model_name='unimajor',
            name='Subject_combination',
        ),
        migrations.AddField(
            model_name='unimajor',
            name='U_Name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='university',
            name='Max_Tuition_Fee',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='university',
            name='Min_Tuition_Fee',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=6, null=True),
        ),
        migrations.AddField(
            model_name='university',
            name='Score_Link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='university',
            name='Description',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.CreateModel(
            name='CombMajor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('M_Name', models.CharField(max_length=200)),
                ('Score', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Comb', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Demo.combination')),
                ('Major', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Demo.major')),
                ('Uni', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Demo.university')),
            ],
        ),
        migrations.CreateModel(
            name='Campus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Uni', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Demo.university')),
                ('Region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Demo.region')),
            ],
        ),
        migrations.CreateModel(
            name='UniField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Demo.fieldofstudy')),
                ('Uni', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Demo.university')),
            ],
        ),
    ]
