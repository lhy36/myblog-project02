from django.shortcuts import render, redirect, get_object_or_404
from book.models import *
from django.views import View
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render



def my_info(request):
    return render(request,'my_info.html')

def cart(request):
    return render(request, 'cart.html')

def heart(request):
    return render(request, 'heart.html')



def my_info_view(request):
    # 여기에서 다른 앱에서 필요한 컨텍스트 데이터를 가져와서 템플릿에 전달
    # 예: 다른 앱에서의 관심 책 목록 가져오기

    context = {
        # 컨텍스트 변수 설정
    }
    
    return render(request, 'heart.html', context)


def my_info(request):
    print(request.user)
    return render(request, 'my_info.html', {'user': request.user})