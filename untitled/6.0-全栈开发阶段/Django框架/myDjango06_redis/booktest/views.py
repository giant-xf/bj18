from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def set_session(request):
    '''设置session'''
    request.session['name'] = 'smart'
    request.session['age'] = 20
    return HttpResponse('设置session')

def get_session(request):
    '''获取session'''
    name = request.session['name']
    age = request.session['age']
    return HttpResponse(name+':'+str(age))


