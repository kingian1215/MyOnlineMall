from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from.forms import CustomUserCreationForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False #用戶註冊後需管理員審核後才能登入
            user.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
        
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        # 驗證表單
        if form.is_valid(): 
            # 認證成功
            user = form.get_user()
            if user.is_approved:
                # 登入成功
                login(request, user)
                if user.is_teacher:
                    return redirect('teacher_home')
                else:
                    return redirect('student_home')
            else:
                return render(request, 'login.html', {'form': form, 'error': '您的帳號尚未通過審核，請聯繫管理員'})
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request) #登出
    return redirect('login')

def student_home(request):
    return render(request,'student_home.html')

def teacher_home(request):
    return render(request, 'teacher_home.html')