from django.shortcuts import render, resolve_url

# Create your views here.

def index(request):
    return render(request, 'index.html')


#### viws.py 걸열님 시작 ####
    
#### viws.py 걸열님 끝 ####


#### viws.py 경휘님 시작 ####

#### viws.py 경휘님 끝 ####


#### viws.py 효수님 시작 ####
def hsp(request):
    return render(request, 'hsp.html')

def coffeenote_datail1(request):
    return render(request, 'coffeenote_detail1.html')

def coffeenote_datail2(request):
    return render(request, 'coffeenote_detail2.html')

def coffeenote_datail3(request):
    return render(request, 'coffeenote_detail3.html')
#### viws.py 효수님 끝 ####

