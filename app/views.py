from django.shortcuts import render
from django.views.generic import View 
from app.forms import * 

# Create your views here.
from django.http import HttpResponse
def FBV_string(request):

    return HttpResponse('this is FBV string')

class CBV_string(View):
    def get(self,request):
        return HttpResponse('this is CBV sring')




def FBV_html(request):
    
    return render(request,'FBV_html.html')

class CBV_html(View):
    def get(self,request):
        return render(request,'CBV_html.html')
    




def FBV_form(request):
    TFO=topicform()
    d={'TFO':TFO}
    if request.method=='POST':
        TFD=topicform(request.POST)
        if TFD.is_valid():
            TFD.save()
            return HttpResponse('data is inserted')
    return render(request,'FBV_form.html',d)


class CBV_form(View):
    def get(self,request):
        TFO=topicform()
        d1={'TFO':TFO}
        return render(request,'CBV_form.html',d1)

    def post(self,request):
        TFD=topicform(request.POST)
        if TFD.is_valid():
            TFD.save()
            return HttpResponse('data is inserted')










    