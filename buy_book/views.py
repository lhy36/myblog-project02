import json
from book.models import *
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.http import HttpResponse
# from django.http import JsonResponse
# from django.contrib.auth.decorators import login_required


def detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    context = {
        'book': book,
    }
    return render(request, 'detail.html', context)


def buy(request):
    book = Book.objects.all()
    if request.method == 'POST':
        search = request.POST.get('search')
        results = Book.objects.filter(Q(name__icontains=search))
        context = {
            'result':results
        }
        return render(request, 'main.html', context)

        
    context = {
        'book':book,
    }
    return render(request, 'main.html', context)




def books_sub(request, subdepartment): 
    # 문자열 값을 사용하여 SubDepartment 객체 검색
    subdepartment = SubDepartment.objects.get(name=subdepartment)
    books = subdepartment.booklist.all()

    # 페이지당 보여줄 항목 수
    items_per_page = 12
    paginator = Paginator(books, items_per_page)

    page = request.GET.get('page')
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)

    context = {
        'subdepartment': subdepartment,
        'books': books,
    }
    return render(request, 'books_sub.html', context)



def department_books(request, department_name):
    department = get_object_or_404(Department, name=department_name)
    subdepartments = SubDepartment.objects.filter(department=department)
    books = []
    for subdepartment in subdepartments:
        books.extend(subdepartment.booklist.all())

    context = {
        'department': department,
        'subdepartments': subdepartments,
        'books': books,
    }
    return render(request, 'books_sub_plus.html', context)

def pick_up(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'pick_up.html', {'book': book})

def pick_up_buy(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'pick_up_buy.html', {'book': book})


# def add_to_favorites(request, book_id):
#     if request.method == 'POST':
#         if request.user.is_authenticated:
#             book = get_object_or_404(Book, pk=book_id)
#             heart.objects.get_or_create(user=request.user, book=book)
#             return redirect('heart')
#         else:
#             # 사용자가 인증되지 않은 경우 처리
#             return redirect('login')  # 필요에 따라 로그인 페이지로 리디렉션 또는 처리
#     else:
#         return redirect('home')  # 필요에 따라 홈으로 리디렉션 또는 처리

# def favorited_books(request):
#     if request.user.is_authenticated:
#         favorited_books = heart.objects.filter(user=request.user)
#         return render(request, 'heart.html', {'favorited_books': favorited_books})
#     else:
#         # 사용자가 인증되지 않은 경우 처리
#         return redirect('login')  # 필요에 따라 로그인 페이지로 리디렉션 또는 처리

# def remove_from_favorites(request, book_id):
#     if request.method == 'POST':
#         if request.user.is_authenticated:
#             heart.objects.filter(user=request.user, book_id=book_id).delete()
#         return redirect('heart')
#     else:
#         return redirect('home')  # 필요에 따라 홈으로 리디렉션 또는 처리
