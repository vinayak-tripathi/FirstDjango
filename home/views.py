from django.shortcuts import render,HttpResponse
from home.models import info
from django.contrib import messages
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

def get_dta(url):
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup.find_all('a', attrs={"class":"black-link"})
    urls= dict()
    for i in tags:
        temp =url
        u=i.get('href', None)
        temp = temp.replace("series/big-bash-league-2021-22-1269637/squads",u)
        name = i.get("data-hover",None)
        urls[name] = temp
    print(len(urls))
    inf = dict()
    for i,v in urls.items():
        link = v
        soup = BeautifulSoup(urlopen(link, context=ctx).read(), "html.parser")
        tags = soup.find_all('div', attrs={"class":"player-page-name"})
        inf[i] = tags
        print(i,v)
    return inf

# Create your views here.
def index(request):
    if request.method =="POST":
        url =  request.POST.get('name')
        url_value = get_dta(url)
        for key,values in url_value.items():
            i = info(squad=key,teams = values)
            i.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'index.html')

def about(request):
    return HttpResponse("THis is about page")