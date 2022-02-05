from django.db import models
import uuid

from django.contrib.auth.models import User

# Create your models here.


class Author(models.Model):
    name = models.CharField(
        max_length=100,
        null=False,
        help_text="An author's full name. (Example: W. Shakespear or Mihail Afanasievich Bulgakov)",
    )
    date_of_birth = models.DateField(
        null=True,
        blank=True,
        help_text="A date of author's birth (or Null, if unknown).",
    )
    date_of_death = models.DateField(
        null=True,
        blank=True,
        help_text="A date of author's death (or Null, if alive or unknown).",
    )

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self) -> str:
        return f"/catalog/author/{self.pk}"


class Genre(models.Model):
    name = models.CharField(
        max_length=100, help_text="A book genre. (example: Science Fiction)"
    )

    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    summary = models.TextField()
    language = models.CharField(max_length=100)
    author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL)
    genres = models.ManyToManyField(Genre)

    def __str__(self) -> str:
        return f"{self.author.name} - {self.title!r}"

    def get_absolute_url(self) -> str:
        return f"/catalog/book/{self.pk}"


class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    imprint = models.CharField(max_length=100)
    year = models.SmallIntegerField()
    book = models.ForeignKey(Book, null=False, on_delete=models.CASCADE)
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        permissions = [
            ("can_mark_returned", "Set book as returned"),
            ("can_mark_on_loan", "Set book as on loan"),
        ]

    LOAN_STATUS = (
        ("o", "On loan"),
        ("a", "Available"),
        ("r", "Reserved"),
    )

    status = models.CharField(
        max_length=1, choices=LOAN_STATUS, default="a", null=False
    )
    due_back = models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{str(self.id)[:8]} ({self.book})"

    def get_display_status(self) -> str:
        return dict(self.LOAN_STATUS)[self.status] + (
            "" if self.status != "o" else f" until {self.due_back}"
        )
