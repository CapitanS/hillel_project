from django.contrib import admin

# Register your models here.
from .models import Author, Book, BookInstance, Genre, Language

# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)
# admin.site.register(BookInstance)
admin.site.register(Language)


class BooksInline(admin.TabularInline):
    """Defines format of inline book insertion (used in AuthorAdmin)"""
    model = Book
    extra = 0


# Define the admin class
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """Administration object for Author models.
        Defines:
         - fields to be displayed in list view (list_display)
         - orders fields in detail view (fields),
           grouping the date fields horizontally
         - adds inline addition of books in author view (inlines)
        """
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BooksInline]


class BookInstanceInline(admin.TabularInline):
    """Defines format of inline book instance insertion (used in BookAdmin)"""
    model = BookInstance
    extra = 0


# Define the Admin classes for Book
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """Administration object for Book models.
        Defines:
         - fields to be displayed in list view (list_display)
         - adds inline addition of book instances in book view (inlines)
        """
    list_display = ('title', 'author', 'display_genre')
    inlines = [BookInstanceInline]


# Define the Admin classes for BookInstance
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    """Administration object for BookInstance models.
        Defines:
         - fields to be displayed in list view (list_display)
         - filters that will be displayed in sidebar (list_filter)
         - grouping of fields into sections (fieldsets)
        """
    list_display = ('book', 'status', 'id')
    list_filter = ('status',)

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status',)
        }),
    )


