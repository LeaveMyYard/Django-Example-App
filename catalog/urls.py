from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("books", views.BookListView.as_view(), name="books"),
    path("book/<int:pk>", views.BookDetailView.as_view(), name="book"),
    path(
        "book_instance/borrowed",
        views.BorrowedBookInstancesListView.as_view(),
        name="book-instance-borrowed",
    ),
    path(
        "book/instance/<uuid:pk>/reserve",
        views.reserve_book_form,
        name="reserve-book-form",
    ),
    path(
        "book/instance/<uuid:pk>/set_loaned",
        views.set_book_loaned_form,
        name="set-loaned-book-form",
    ),
    path("author/create", views.AuthorCreateView.as_view(), name="author-create"),
    path(
        "author/update/<int:pk>", views.AuthorUpdateView.as_view(), name="author-update"
    ),
    path(
        "author/delete/<int:pk>", views.AuthorDeleteView.as_view(), name="author-delete"
    ),
]
