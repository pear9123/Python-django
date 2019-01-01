from django.shortcuts import render, redirect
from .forms import LoginForm, SignupForm
from django.contrib.auth import login as django_login, logout as django_logout, authenticate

# Create your views here.
def login(request):
    if request.method == 'POST':
        #Data bounded form 인스턴스 생성
        login_form = LoginForm(request.POST)
        #유효성 검증에 성공할 경우
        if login_form.is_valid():
            #form으로부터 username,password값을 가져옴
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']

            #가져온 usernamer과 password에 해당하는 user가 있는지 판단한다
            #존재할경우 user변수에는 User인스턴스가 할당되며,
            #존재하지 않으면 none이 할당된다
            user = authenticate(
                username = username,
                password = password
            )

            #인증에 성공했을 경우
            if user:
                #django의 auth앱에서 제공하는 login함수를 실행해 앞으로의 요청/응답에 세션을 유지한다
                django_login(request,user)
                #post목록 화면으로 이동
                return redirect('post:post_list')

            #인증에 실패하면 login_form애 non_field_error를 추가한다
            login_form.add_error(None, '아이디 또는 비밀번호가 올바르지 않습니다.')

    else:
        login_form = LoginForm()
    context = {
        'login_form':login_form,
    }
    return render(request,'member/login.html', context)

def logout(request):
    django_logout(request)
    return redirect('post:post_list')


def signup(request):
    if request.method == 'POST':
        signup_form = SignupForm(request.POST)
        # 유효성 검증에 통과한 경우 (username의 중복과 password1,2의 일치 여부)
        if signup_form.is_valid():
            #SignupForm의 인스턴스 메서드인 signup() 실행, 유저 생성
            signup_form.signup()
            return redirect('post:post_list')
    else:
        signup_form = SignupForm()

    context = {
        'singup_form':signup_form,
    }
    return render(request,'member/signup.html',context)
