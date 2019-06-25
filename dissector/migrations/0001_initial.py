# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-17 22:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('layerindex', '0044_dissector'),
    ]

    state_operations = [
        migrations.CreateModel(
            name='ImageComparison',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('from_branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagecomparison_from_set', to='layerindex.Branch')),
                ('to_branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagecomparison_to_set', to='layerindex.Branch')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ImageComparisonRecipe',
            fields=[
                ('recipe_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='layerindex.Recipe')),
                ('cover_pn', models.CharField(blank=True, max_length=100, verbose_name='Covering recipe')),
                ('cover_status', models.CharField(choices=[('U', 'Unknown'), ('N', 'Not available'), ('S', 'Distro-specific'), ('O', 'Obsolete'), ('E', 'Equivalent functionality'), ('D', 'Direct match')], default='U', max_length=1)),
                ('cover_comment', models.TextField(blank=True)),
                ('sha256sum', models.CharField(blank=True, max_length=64)),
                ('comparison', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dissector.ImageComparison')),
                ('cover_layerbranch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='layerindex.LayerBranch', verbose_name='Covering layer')),
            ],
            bases=('layerindex.recipe',),
        ),
        migrations.CreateModel(
            name='VersionComparison',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('I', 'In progress'), ('F', 'Failed'), ('S', 'Succeeded')], default='I', max_length=1)),
                ('from_branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='versioncomparison_from_set', to='layerindex.Branch')),
                ('to_branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='versioncomparison_to_set', to='layerindex.Branch')),
            ],
        ),
        migrations.CreateModel(
            name='VersionComparisonDifference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pn', models.CharField(max_length=100)),
                ('change_type', models.CharField(choices=[('A', 'Add'), ('U', 'Upgrade'), ('D', 'Downgrade'), ('V', 'Version changes'), ('R', 'Remove'), ('M', 'Modification')], max_length=1)),
                ('oldvalue', models.CharField(blank=True, max_length=255)),
                ('newvalue', models.CharField(blank=True, max_length=255)),
                ('comparison', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dissector.VersionComparison')),
                ('from_layerbranch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='versioncomparisondifference_from_set', to='layerindex.LayerBranch')),
                ('to_layerbranch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='versioncomparisondifference_to_set', to='layerindex.LayerBranch')),
            ],
        ),
        migrations.CreateModel(
            name='VersionComparisonFileDiff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('I', 'In progress'), ('F', 'Failed'), ('S', 'Succeeded')], default='I', max_length=1)),
                ('difference', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dissector.VersionComparisonDifference')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='imagecomparison',
            unique_together=set([('user', 'name')]),
        ),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(state_operations=state_operations)
    ]