from django.shortcuts import render
from .models import Book
from .forms import LoginForm, AddBookForm, SignupForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def home(request):
    books = Book.objects.order_by('-id').all()
    return render(request, 'book/home.html', {'books': books})


def loginAdmin(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']

                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, "Logged in Successfully")
                    return HttpResponseRedirect('/book/admin')
        else:
            form = LoginForm()
        return render(request, 'book/login.html', {'form': form})
    else:
        return HttpResponseRedirect('/book/admin')


def signupAdmin(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = SignupForm(data=request.POST)
            if form.is_valid():
                user = form.save()
                messages.success(request, "You have successfully Signed up !!!")
                return HttpResponseRedirect('/book/admin')
        else:
            form = SignupForm()
        return render(request, 'book/signup.html', {'form': form})
    else:
        logout(request)
        return signupAdmin(request)

def logoutAdmin(request):
    if request.user.is_authenticated:
        logout(request)
        return home(request)
    else:
        return home(request)


def books(request):
    return render(request, 'book/books.html')


def add(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AddBookForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                author = form.cleaned_data['author']
                pubDate = form.cleaned_data['pubDate']

                book = Book(title=title, author=author, pubDate=pubDate)
                book.save()
                form = AddBookForm()
                messages.success(request, "Book Added Successfully")
                return HttpResponseRedirect('/book/admin')
        else:
            form = AddBookForm()
        return render(request, 'book/addBook.html', {'form': form})
    else:
        return HttpResponseRedirect('/book/admin')


def adminPage(request):
    if request.user.is_authenticated:
        books = Book.objects.order_by('-id').all()
        return render(request, 'book/adminPage.html', {"books": books, "admin": request.user.username})
    else:
        return loginAdmin(request=request)


def update(request, id):
    if request.user.is_authenticated:
        oldBook = Book.objects.filter(id=id).first()
        initial = {'title': oldBook.title, 'author': oldBook.author, 'pubDate': oldBook.pubDate }
        if request.method == 'POST':
            form = AddBookForm(request.POST, initial=initial)
            if form.is_valid():
                title = form.cleaned_data['title']
                author = form.cleaned_data['author']
                pubDate = form.cleaned_data['pubDate']
                book = Book(id=id, title=title, author=author, pubDate=pubDate)
                book.save()
                form = AddBookForm(initial=initial)
                messages.success(request, "Book Added Successfully")
                return HttpResponseRedirect('/book/admin')
        else:
            form = AddBookForm(initial=initial)
        return render(request, 'book/updateBook.html', {'form': form})
    else:
        return render(request, 'book/login.html')


def delete(request, id):
    if request.user.is_authenticated:
        book = Book.objects.filter(id=id).first()
        book.delete()
        messages.success(request, "Book Deleted Successfully")
        return adminPage(request)
    else:
        return render(request, 'book/login.html')
