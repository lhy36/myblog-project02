from django.shortcuts import render, redirect
from book.models import *
from .forms import BookRequestForm
from django.contrib import messages





def add(request):
    if request.method == 'POST':
        form = BookRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '작성이 완료되었습니다.')
            return redirect('bookadd_bookadd_changelist')
    else:
        form = BookRequestForm()
    
    return render(request,'add_home.html', {'form': form})

def bookadd_bookadd_changelist(request):
    return render(request, 'add_home.html')

