from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def string_1(request):
    return HttpResponse('<h1>this is app1 of string_1</h2>')


def string_2(request):
    return HttpResponse('<h1>this is app1 of string_2</h1>')