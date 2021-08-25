from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Shopp
from haystack.forms import  ModelSearchForm
from haystack.query import EmptySearchQuerySet
def index(request):
    shop_list = Shopp.objects.all()
    context = {
        'query': '',
        'shop_list': shop_list
    }
    return render(request, 'searchshop/index.html', context)

def search(request,  load_all=True, form_class=ModelSearchForm, searchqueryset=None):
    if request.GET.get('q'):
        form = form_class(request.GET, searchqueryset=searchqueryset, load_all=load_all)

        if form.is_valid():
            query = form.cleaned_data['q']
            results = form.search()
            context = {
                'query': query,
                'shop_list': results
            }
            return render(request, 'searchshop/index.html', context)
            # results = form.search()
        return HttpResponse(request.GET.get('q'))
    return HttpResponse('查询')