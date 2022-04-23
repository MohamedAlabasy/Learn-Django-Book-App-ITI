from django.shortcuts import render, get_object_or_404
from .models import Book, Author
from django.shortcuts import redirect

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
    context = {
        "data": "Create New Books"
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
