from django.shortcuts import render, get_object_or_404
from .models import Book, Author
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
