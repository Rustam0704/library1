from django.contrib import admin

from libr.models import Book, Category, BookRecord


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass
    # list_display = ('name', 'category')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
    # list_display = ('name',)

@admin.register(BookRecord)
class BookRecordAdmin(admin.ModelAdmin):
    # list_display = ('user', 'book', 'day')
    # list_filter = ('user',)
    pass
