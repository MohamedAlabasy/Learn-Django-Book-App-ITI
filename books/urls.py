from django.urls import path
from .views import list_books, show_book, list_authors, show_author

urlpatterns = [
    path('', list_books, name='list_books'),
    path('<int:book_id>', show_book, name="show_book"),
    path('author/', list_authors, name="list_authors"),
    path('author/<int:author_id>', show_author, name="show_author"),
]
