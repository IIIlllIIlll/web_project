from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login
from .forms import UserForm,RegisterForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from .models import *

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.auth.forms import AuthenticationForm


def signup(request):
    """
    회원가입
    get - 비어 있는 UserForm
    post - 바인딩 된 UserForm
    """
    if request.method == "POST":
        form = UserForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserForm()
    return render(request,"user/signup.html",{"form":form})

def profile(request):
    profile_detail = get_object_or_404(Profile,id=request.user.id)
    if request.method == "POST":
        form = RegisterForm(request.POST, request.FILES, instance=profile_detail)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect("profile")
    else:
        form = RegisterForm(instance=profile_detail)
    return render(request, 'users/profile.html',{"form":form})

# def isLogin(request):

#     if request.method == "POST":
#         # username, password 가져오기
#         username = request.POST['email']
#         password = request.POST['password']

#         print("para", username, password)

#         # db 확인(사용자의 입력값과 데이터베이스 내용과 확인)
#         user = authenticate(request, username=username, password=password)

#         # 세션에 정보 저장
#         if user is not None:
#             login(request, user)
#             return redirect("main")
#         else:
#             messages.error(request, "이메일과 비밀번호를 확인해 주세요")
#             return render(request,"user/login.html")           

#     return render(request,"user/login.html")


class UserPasswordResetView(PasswordResetView):
    form_class = UserForm
    template_name = "user/password_reset_form.html"
    success_url = reverse_lazy("password_reset_done")
    email_template_name ="user/password_reset_email.txt"

    def form_valid(self, form):

        if User.objects.filter(email=self.request.POST.get("email")).exists():
            return super().form_valid(form)
        else:
            messages.info(self.request, "이메일을 확인해 주세요")
            return redirect("password_reset")

class UserPasswordResetDoneView(PasswordResetDoneView):
    template_name = "user/password_reset_done.html"

class UserPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = "user/password_reset_confirm.html"

class UserPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = "user/password_reset_complete.html"
