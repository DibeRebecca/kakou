from django.shortcuts import render
from django.http import HttpResponse
from .models import Categories , Articles, Reservation , Contact
from django.template import loader

# Create your views here.
def index(request):
    articles=Articles.objects.filter(available=True).order_by('-created_at')[:12]
    formatted_articles=["<li>{}</li>".format(article.name)for article in articles]
    template=loader.get_template('store/index.html')
    context={'articles':articles}
    #return HttpResponse(template.render(context,request=request))
    return render(request, 'store/index.html', context)


def listing(request):
    articles=Articles.objects.filter(available=True)
    formatted_articles=["<li>{}</li>".format(article.name)for article in articles]
    message="""<ul>{}</ul>""".format("\n".join(formatted_articles))
    return HttpResponse(message)


"""def detail(request,article_id):
    articles=Articles.objects.get(pk=article_id)
    articles="".join([article['name'] for article in articles['articles']])
    message="Le nom de l'album est {} , il a te ecrit par {}".format(categorie['name'],articles)
    return HttpResponse(message)"""
def search(request):
    """obj=str(request.GET)
    query=request.GET['query']
    message="la requette est {}, le resultat est {} ".format(obj,query)
    return HttpResponse(message)"""
    query=request.GET.get('query')
    if not query:
        articles=Articles.objects.all()
    else:
        articles=Articles.objects.filter(name_icontains=query)
        if not articles.exists():
            articles=Articles.objects.all()
        else:
            articles=[
                    "<li>{}</li>".format(article.name) for article in articles ]
            message="""
                Nous avons trouvé les albums correpondants à votre requete :
                <ul>
                {}
                </ul>""".format("</li><li>".join(articles))
           
               
    return HttpResponse(message)