from django.shortcuts import render
from django.views import generic
from .models import Book, Author, BookInstance, Genre
from typing import Any

# Create your views here.


class BookListView(generic.ListView):
    model = Book
    context_object_name = "book_list"
    queryset = Book.objects.all()
    template_name = "book/list.html"

    # def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
    #     return super().get_context_data(**kwargs) | {"book_list": Book.objects.all()}


class BookDetailView(generic.DetailView):
    model = Book
    template_name = "book/detail.html"


def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact="a").count()
    num_authors = Author.objects.all().count()

    return render(
        request,
        "index.html",
        context={
            "num_books": num_books,
            "num_instances": num_instances,
            "num_instances_available": num_instances_available,
            "num_authors": num_authors,
        },
    )
