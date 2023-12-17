from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Book
from django.contrib.auth.models import User
from django.contrib import auth
from django.views import View
from django.db.models import Q
from django.shortcuts import render

def home(request):
    book = Book.objects.all()
    if request.method == 'POST':
        search = request.POST.get('search')
        results = Book.objects.filter(Q(name__icontains=search))
        context = {
            'result':results
        }
        return render(request, 'home.html', context)

        
    context = {
        'book':book,
    }
    return render(request, 'home.html', context)



def login(request):
    if request.method == "POST":
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Username or password is incorrect!'})
    else:
        return render(request, 'login.html', {'user': request.user})  # Pass the user object to the template


def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username = request.POST['username'])
                return render(request,'signup.html',{'error':"Username is already taken"})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                auth.login(request,user)
                return redirect('home')

    return render(request,'signup.html')

@login_required
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')

