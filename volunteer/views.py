from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from todo_list.forms import TodoForm
from todo_list.models import Todo
from datetime import datetime
from django.utils.dateformat import DateFormat
# Create your views here.


def vol_index(request):
    vol_list = Volunteer.objects.all()
    today = DateFormat(datetime.now())
    print(today)
    return render(request, "volunteer/index.html", {"vol_list": vol_list,"today":today})
# 상세내용
def vol_detail(request,pk):
    detail = get_object_or_404(Volunteer,pk=pk)
    return render(request, 'volunteer/vol_detail.html', {'detail':detail})

@login_required(login_url="login")
def sign_vol(request, pk):
    sign_vol = get_object_or_404(Volunteer, pk=pk)
    sign_vol.sign_vol.add(request.user)

    return redirect("vol_detail", pk=pk)

@login_required(login_url="login")
def add_cal(request,pk):
    vol_detail = get_object_or_404(Volunteer,pk=pk)
    Todo.objects.create(
    title= vol_detail.organization.org_name,
    start_date= vol_detail.start_date,
    end_date =  vol_detail.end_date,
    description =  vol_detail.organization.addr,
    user = request.user
    )
    
    return redirect("todo_list")