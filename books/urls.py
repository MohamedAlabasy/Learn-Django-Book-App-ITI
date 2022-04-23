from django.urls import path
from .views import list_books, show_book, list_authors, show_author, create_book, update_book, delete_book

urlpatterns = [
    path('', list_books, name='list_books'),
    path('<int:book_id>', show_book, name="show_book"),
    path('create_book', create_book, name="create_book"),
    path('update_book', update_book, name="update_book"),
    path('delete_book', delete_book, name="delete_book"),
    path('author/', list_authors, name="list_authors"),
    path('author/<int:author_id>', show_author, name="show_author"),
]
