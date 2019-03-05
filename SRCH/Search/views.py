from django.shortcuts import render
# from django.http import HttpResponse
from django.template import loader
import http.client, urllib.parse, json


from .forms import NameForm
# import random
# from SRCH.Search.Entity.Result import Results
from .joinResult import joinR
import urllib
subscriptionKey = "3ff2d1ad65c34ec884f8d30326cf623f"
host = "api.cognitive.microsoft.com"
path = "/bing/v7.0/search"

term = "Dog"
# Create your views here.
# def fetch(key):
#     exampleSearch = key
#     print('Searching web for ' + key)
#     # encoded = urllib.quote(exampleSearch)
#     url = 'https://www.googleapis.com/customsearch/v1?key=AIzaSyD8-zQW_mMM-dOyny75J0RdRDgyMP1P8hw&cx=003369086800144489281:fnxwb3klqza&q='
#     urlup = url + key
#     rawData = urllib.request.urlopen(urlup).read()
#     jsonData = json.loads(rawData)
#     links = []
#
#     for i in range(10):
#         link = json.dumps(jsonData['items'][i]['link'], indent=4)
#         snippet = json.dumps(jsonData['items'][i]['snippet'], indent=4)
#         title = json.dumps(jsonData['items'][i]['title'], indent=4)
#         ele = Results(title, link, snippet, 2)
#         links.append(ele)
#     for i in range(10):
#         print(links[i].name)
#     return links


def index(request):

    template=loader.get_template('Search/index.html')
    if len(subscriptionKey) == 32:

        print('Searching the Web for: ', term)

        headers, result = BingWebSearch(term)
        print("\nRelevant HTTP Headers:\n")
        print("\n".join(headers))
        print("\nJSON Response:\n")
        res = json.loads(result);
        # for i in range(10):
        #     print(json.dumps(res['webPages']['value'][i]['url'], indent=4))
        return render(request, 'Search/index.html', {
            'url1': res['webPages']['value']
        })


def BingWebSearch(search):
        "Performs a Bing Web search and returns the results."

        headers = {'Ocp-Apim-Subscription-Key': subscriptionKey}
        conn = http.client.HTTPSConnection(host)
        query = urllib.parse.quote(search)
        conn.request("GET", path + "?q=" + query, headers=headers)
        response = conn.getresponse()
        headers = [k + ": " + v for (k, v) in response.getheaders()
                   if k.startswith("BingAPIs-") or k.startswith("X-MSEdge-")]
        return headers, response.read().decode("utf8")

def homepage(request):
    template=loader.get_template('Search/homepage.html')
    return render(request,'Search/homepage.html')

def get_name(request):

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            search=form.cleaned_data['search']
            print(search)
            str(request.body, encoding='utf-8')
            if len(subscriptionKey) == 32:
                print('Searching the Web for: ', search)
                ob = joinR()
                url1=ob.merge(search)
                return render(request, 'Search/index.html', {

                    'url1': url1, 'search':search
                })


    # form = NameForm()
    # return render(request,'Search/index.html',{'form':form})
            # return HttpResponse(template.render({'name':'name'},request))
    # else:
    #         form = NameForm()
    #         template = loader.get_template("Search/homepage.html")
    #         context = {'form': form}
    #         return HttpResponse(template.render(context, request))







