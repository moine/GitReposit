from django.db import models

# Create your models here.


class Article(models.Model):
    titre = models.CharField(max_length=100)
    auteur = models.CharField(max_length=42)
    contenu = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False,
    verbose_name="Date de parution")
    categorie = models.ForeignKey('Categorie')
    def __unicode__(self):
        return u"%s" % self.titre

class Categorie(models.Model):
    nom = models.CharField(max_length = 30)
    def __unicode__(self):
        return self.nom
