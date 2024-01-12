from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
class AbstractModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Category(AbstractModel):
    name = models.CharField(max_length=15)
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        verbose_name_plural = "Categories"
        verbose_name = "Category"
        db_table = "category"

    def __str__(self):
        return self.name

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug=slugify(self.name)
        super().save(force_insert, force_update, using, update_fields)
class Book(AbstractModel):
    name = models.CharField(max_length=28)
    category = models.ManyToManyField(Category, related_name="subjects")
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Books"
        verbose_name = "Book"
        db_table = "book"

    def __str__(self):
        return self.name

class BookRecord(AbstractModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ManyToManyField(Book, related_name="subjects")
    day = models.IntegerField()

    def __str__(self):
        return f"{self.user}-{self.book.name}"

    class Meta:
        verbose_name_plural = "Record of Book"
        verbose_name = "Record of Book"
        db_table = "BookRecord"

