from django.shortcuts import render, resolve_url

# Create your views here.

def index(request):
    return render(request, 'index.html')



#### viws.py 걸열님 시작 ####
def gyl(request):
    return render(request, 'gyl.html')
    
def new_note(request):
    return render(request, 'new_note.html')
#### viws.py 걸열님 끝 ####


#### viws.py 경휘님 시작 ####
def ghl(request):
    return render(request, 'ghl.html')
#### viws.py 경휘님 끝 ####


#### viws.py 효수님 시작 ####
def hsp(request):
    return render(request, 'hsp.html')
#### viws.py 효수님 끝 ####