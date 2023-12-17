from django.shortcuts import render, redirect, get_object_or_404
from .forms import UsedBookCategoryForm, UsedBookForm, SearchForm
from .models import DetailImage, UsedBook  # 모델 임포트 필요
from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Comment
from django.contrib import messages
import json

def search(request):
    form = SearchForm(request.GET)
    used_books = UsedBook.objects.all()

    if form.is_valid():
        search_query = form.cleaned_data['search_query']
        if search_query:
            used_books = used_books.filter(
                Q(title__icontains=search_query) | Q(author__icontains=search_query)
            )

    return render(request, 'used_home.html', {'used_books': used_books, 'form': form})

def used(request):
    category_form = UsedBookCategoryForm(request.POST or None)
    used_books = UsedBook.objects.all()

    if category_form.is_valid():
        category = category_form.cleaned_data['category']
        if category:
            used_books = used_books.filter(category=category)

    items_per_page = 9
    paginator = Paginator(used_books, items_per_page)  # Change variable name to `used_books`
    page = request.GET.get('page')
    try:
        used_books = paginator.page(page)  # Change variable name to `used_books`
    except PageNotAnInteger:
        used_books = paginator.page(1)
    except EmptyPage:
        used_books = paginator.page(paginator.num_pages)

    context = {
        'used_books': used_books,
        'category_form': category_form,
    }
    return render(request, 'used_home.html', context)

def expage(request):
    return render(request, 'used_ex.html')  

# def used(request):
#     if request.method == 'POST':
#         category_form = UsedBookCategoryForm(request.POST)
#         if category_form.is_valid():
#             # Process the form data as needed
#             category = category_form.cleaned_data['category']
#             # Save or perform other actions with the category data




def used_up(request):
    form = UsedBookForm()  # 먼저 form을 정의합니다.

    if request.method == 'POST':
        form = UsedBookForm(request.POST, request.FILES)
        if form.is_valid():
            used_book = form.save(commit=False)
            used_book.user = request.user
            used_book.save()

            detail_images = request.FILES.getlist('detail_images')
            for image in detail_images:
                detail_image = DetailImage.objects.create(image=image, used_book=used_book)
                used_book.detail_images.add(detail_image)

            return redirect('add_used_book_success')
        
    return render(request, 'used_up.html', {'form': form})


    

    # return HttpResponse("Form submission failed.")

def add_used_book_success(request):
    return render(request, 'used_home.html')


# def used_detail(request, used_id):
#     used_book = get_object_or_404(UsedBook, pk=used_id)
#     return render(request, 'used_detail.html', {'used_book': used_book})
def used_detail(request, used_id):
    used_book = get_object_or_404(UsedBook, pk=used_id)
    # detail_images = used_book.detail_images.all()  # UsedBook 인스턴스의 모든 이미지 가져오기
    detail_images = [used_book.detail_images] if used_book.detail_images else []
    return render(request, 'used_detail.html', {'used_book': used_book, 'detail_images': detail_images})


# def edit_book(request, used_id):
#     used_book = get_object_or_404(UsedBook, pk=used_id)

#     if request.method == 'POST':
#         form = UsedBookForm(request.POST, request.FILES, instance=used_book)
#         if form.is_valid():
#             form.save()
#             # Redirect or add additional logic as needed
#     else:
#         form = UsedBookForm(instance=used_book)

#     return render(request, 'used_up.html', {'form': form, 'used_book': used_book})


def edit_book(request, used_id):
    used_book = get_object_or_404(UsedBook, pk=used_id)

    if request.method == 'POST':
        form = UsedBookForm(request.POST, request.FILES, instance=used_book)
        if form.is_valid():
            form = form.save(commit=False)
            form.detail_images.clear()  # 기존 이미지 삭제
            form.save()

            detail_images = request.FILES.getlist('detail_images')
            for image in detail_images:
                detail_image = DetailImage.objects.create(image=image, used_book=form)
                form.detail_images.add(detail_image)

            # Redirect to the appropriate URL after successful update
            return redirect('add_used_book_success')
    else:
        form = UsedBookForm(instance=used_book)

    return render(request, 'used_up.html', {'form': form, 'used_book': used_book})


# mmmmmmmmmmmmm

# @login_required 
# def edit_book(request, used_id):
#     used_book = get_object_or_404(UsedBook, pk=used_id)

#     if request.method == 'POST':
#         form = UsedBookForm(request.POST, request.FILES, instance=used_book)
#         if form.is_valid():
#             form.save()
#             return redirect('used') 
#     else:
#         form = UsedBookForm(instance=used_book)

#     return render(request, 'used_up.html', {'form': form, 'used_book': used_book})

@login_required 
def delete_book(request, used_id):
    used_book = get_object_or_404(UsedBook, pk=used_id)
    
    if request.method == 'POST':
        used_book.delete()
        return redirect('used')  # Redirect to the desired page after deletion

    return render(request, 'used_home.html', {'used_book': used_book})

@login_required  # 사용자 로그인이 필요한 경우
def add_heart(request, book_id):
    book = get_object_or_404(UsedBook, id=book_id)
    user_hearts = request.user.profile.hearts.all()
    context = {
        "book": book,
        "user_hearts": user_hearts,
    }
    if request.is_ajax():
        return JsonResponse({"message": "책을 관심 목록에 추가했습니다."})
    else:
        # 사용자가 브라우저에서 요청을 보낸 경우, 다른 앱의 템플릿을 렌더링하고 context 변수를 전달
        return render(request, 'heart.html', context)

@login_required
def add_cart(request, book_id):
    book = get_object_or_404(UsedBook, id=book_id)
    # 여기에서 장바구니에 책을 추가하는 로직을 구현
    return JsonResponse({"message": "책을 장바구니에 추가했습니다."})


def save_comment(request):
    if request.method == 'POST' and request.is_ajax():
        data = json.loads(request.body)
        userid = data.get('userid', '사용자')
        content = data.get('content', '')
        date = data.get('date', '')

        # Comment 모델을 사용하여 DB에 저장
        Comment.objects.create(userid=userid, content=content, date=date)

        return JsonResponse({'success': True})
    return JsonResponse({'success': False})