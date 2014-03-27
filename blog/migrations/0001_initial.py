# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = []

    operations = [
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('nom', models.CharField(max_length=30),)],
            bases = (models.Model,),
            options = {},
            name = 'Categorie',
        ),
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('titre', models.CharField(max_length=100),), ('auteur', models.CharField(max_length=42),), ('contenu', models.TextField(null=True),), ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date de parution'),), ('categorie', models.ForeignKey(to='blog.Categorie', to_field=u'id'),)],
            bases = (models.Model,),
            options = {},
            name = 'Article',
        ),
    ]
