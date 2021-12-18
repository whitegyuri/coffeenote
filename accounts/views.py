from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth


# Create your views here.
def sign_up(request):
    context = {}

    if request.method == 'POST':
        if (request.POST.get('username') and
            request.POST.get('password') and
            request.POST.get('password') == request.POST.get('password_check')):

            if User.objects.filter(username=request.POST.get('username')):
                context['error'] = '이미 사용중인 아이디 입니다.'


            else: 
                new_user = User.objects.create_user(
                username = request.POST.get('username'),
                password = request.POST.get('password'),
                )

                auth.login(request, new_user)
                return redirect('index')

        else:
            context['error'] = '아이디와 비밀번호를 다시 확인해주세요.'

    return render(request, 'accounts/sign_up.html', context)


def login(request):
    context = {}

    if request.method == 'POST':
        if request.POST.get('username') and request.POST.get('password'):

            user = auth.authenticate(
                request,
                username = request.POST.get('username'),
                password = request.POST.get('password'),
            )

            if user is not None:
                auth.login(request, user)
                return redirect('index')
            else:
                context['error'] = '아이디와 비밀번호를 다시 확인해주세요.'

        else: 
            context['error'] = '아이디와 비밀번호를 모두 입력해주세요.'

    return render(request, 'accounts/login.html', context)


def logout(request):
    if request.method == 'POST':
        auth.logout(request)

    return redirect('index')