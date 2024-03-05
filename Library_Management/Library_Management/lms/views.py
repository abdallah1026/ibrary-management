from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import LMSForm, CategoryForm


# Create your views here.

def index(request):
    if request.method == 'POST':
        add_book = LMSForm(request.POST, request.FILES)
        if add_book.is_valid():
            add_book.save()
        add_category = CategoryForm(request.POST)
        if add_category.is_valid():
            add_category.save()

    context = {
        'books': Book.objects.all(),
        'categories': Category.objects.all(),
        'form': LMSForm(),
        'cat': CategoryForm(),
        'allbooks': Book.objects.filter(active=True).count(),
        'soldbook': Book.objects.filter(status='sold').count(),
        'avaiablebook': Book.objects.filter(status='available').count(),
        'rentedbook': Book.objects.filter(status='rented').count(),

    }

    return render(request, 'pages/index.html', context)


def books(request):
    search = Book.objects.all()
    title= None
    if "search_name" in request.GET:
        title = request.GET['search_name']
        if title:
            search = search.filter(title__icontains=title)



    context = {
        'books': search,
        'categories': Category.objects.all(),
    }

    return render(request, 'pages/books.html', context)


def update(request, id):
    book_id = Book.objects.get(id=id)
    if request.method == 'POST':
        form = LMSForm(request.POST, request.FILES, instance=book_id)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = LMSForm(instance=book_id)
    context = {
        'form': form
    }
    return render(request, 'pages/update.html', context)


def delete(request, id):
    book_id = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book_id.delete()
        return redirect('/')
    return render(request, 'pages/delete.html')

