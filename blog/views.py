from django.shortcuts import render
from django.http import Http404
from blog.models import Article
from datetime import datetime

def tplbase(request):
    return render(request, 'base.html', locals())

def mapage(request):
    return render(request, 'blog/mapage.html', locals())

def tpl(request):
    return render(request, 'blog/tpl.html', {'current_date': datetime.now()})

def addition(request, nombre1, nombre2):
    total = int(nombre1) + int(nombre2)
    return render(request, 'blog/addition.html', locals())

# Create your views here.
#-*- coding: utf-8 -*-
from django.http import HttpResponse

def home(request):
    text = """<h1>Bienvenue sur mon blog !</h1>
<p>Les sites avec Django c'est cool !</p>"""
    return HttpResponse(text)

def view_article(request, id_article):
    text = "Vous avez demande l'article no {0} !".format(id_article)
    return HttpResponse(text)

def list_articles(request, month, year):
    text = "Vous avez demande les articles de {0} {1}.".format(month, year)
    return HttpResponse(text)

def tpls(request):
    sexe = "Femme"
    html = "Bonjour"
    if sexe == "Femme":
        html += "Madame"
    else:
        html += "Monsieur"
    html += "!"
    return HttpResponse(html)

#models examples

def accueil(request):
    articles = Article.objects.all()
    return render(request, 'blog/accueil.html', {'derniers_articles': articles})
def lire(request, id):
    try:
        article = Article.objects.get(id=id)
    except Article.DoesNotExit:
        raise Http404
    return render(request, 'blog/lire.html', {'article': article})
    #pass




