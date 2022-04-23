from django.shortcuts import render, get_object_or_404
from .models import Book, Author
from django.shortcuts import redirect
from .forms import CreateBooks
from django.utils import timezone


# Create your views here.


def list_books(request):
    all_books = Book.objects.all()
    authors = all_books.prefetch_related('author')
    context = {
        "books": all_books,
        "author": authors
    }
    print(authors)
    return render(request, 'books/list_books.html', context=context)


def show_book(request, book_id):
    context = {
        "book": Book.objects.get(id=book_id),
    }
    return render(request, 'books/show_book.html', context=context)


def list_authors(request):
    context = {
        "authors":  Author.objects.all(),
    }
    return render(request, 'books/list_authors.html', context=context)


def show_author(request, author_id):
    context = {
        "author": Author.objects.get(id=author_id),
        "books": Book.objects.filter(author_id=author_id).all(),
    }
    return render(request, 'books/show_author.html', context=context)


def create_book(request):
    if request.method == 'POST':  # if request from create page => to create new book
        form = CreateBooks(request.POST)
        if form.is_valid():
            new_book = form.save()

           # name = form.cleaned_data["name"]
           # summary = form.cleaned_data["summary"]
           # image = form.cleaned_data["image"]
           # price = form.cleaned_data["price"]
           # appropriate = form.cleaned_data["appropriate"]
           # author = form.changed_data["author"]
           # new_book = Book.objects.create(
           #     name=name,
           #     summary=summary,
           #     publish_date=timezone.now(),
           #     image=image,
           #     add_to_site=timezone.now(),
           #     price=price,
           #     appropriate=appropriate,
           #     author=1,
           # )

        context = {
            "form": form
        }
        return render(request, 'books/create_book.html', context=context)
    else:  # if request from home page => to show form in create page
        form = CreateBooks(request.POST)
        context = {
            "form": form
        }
        return render(request, 'books/create_book.html', context=context)


def update_book(request):
    context = {
        "data": "update book"
    }
    return render(request, 'books/update_book.html', context=context)


def delete_book(request):
    response = redirect('list_books')
    return response
