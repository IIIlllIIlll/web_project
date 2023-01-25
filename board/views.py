from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from board.models import Care
from .forms import CareForm
from django.core.paginator import Paginator
# Create your views here.

# 리스트


def index(request):
    list = Care.objects.order_by("-created_at")
    page = request.GET.get("page", 1)
    paginator = Paginator(list, 4)
    list = paginator.get_page(page)
    return render(request, "board/board_index.html", {"list": list})


# 글작성
@login_required(login_url='login')
def update(request):
    if request.method == "POST":
        form = CareForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            form.save_m2m()
            return redirect("board_index")
    else:
        form = CareForm()
    return render(request, "board/board_write.html", {"form": form})

# 글 디테일


def detail(request, pk):
    post = get_object_or_404(Care, pk=pk)
    return render(request, "board/board_detail.html", {"post": post})

#  글 삭제


def remove(request, pk):
    post = get_object_or_404(Care, pk=pk)
    post.delete()
    return redirect("board_index")


def edit(request, pk):
    post = Care.objects.get(pk=pk)
    if request.method == "POST":
        form = CareForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            form.save_m2m()
            return redirect("board_index")
    else:
        form = CareForm(instance=post)
    return render(request, "board/board_write.html", {"form": form})
