from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

# Create your views here
zodiak_info ={
    'oven':'1',
    'telec':'2',
    'bliznec': '3',
    'rak': '4',
    'lew': '5',
    'dewa': '6',
    'vesy': '7',
    'scorpion': '8',
    'strelec': '9',
    'kozerog': '10',
    'vodoley': '11',
    'ryby': '12',
}
def horoscopes(request):
    result = ''
    for el in zodiak_info:
        link = reverse("znak",args=[el])
        result += f'<li><a href="{link}">{el.title()}</a></li>'
    return HttpResponse(f'<ol>{result}</ol>')

def get_info (request,znak):
    return HttpResponse(f'{zodiak_info[znak]}')



