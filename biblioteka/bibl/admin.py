from django.contrib import admin
from .models import Translator, Genre, Book, Author, BookGenres, BookAuthors, BookTranslators, Rating


class RatingInline(admin.TabularInline):
    model = Rating
    extra = 2
    def has_change_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        if obj is None:
            return True
        return any(rating.user == request.user for rating in obj.rating_set.all())


class BookGenresInline(admin.TabularInline):
    model = BookGenres
    extra = 1

class BookAuthorsInline(admin.TabularInline):
    model = BookAuthors
    extra = 1

class BookTranslationsInline(admin.TabularInline):
    model = BookTranslators
    extra = 1

class BookAdmin(admin.ModelAdmin):
    exclude = ("added_by",)
    list_display = ("title", "issue_date", "added_by", "available",)
    list_filter = ("available",)
    inlines = [BookGenresInline, BookAuthorsInline, BookTranslationsInline, RatingInline]

    def has_change_permission(self, request, obj=None):
        if obj is None:
            return True
        return obj.added_by == request.user

    def has_delete_permission(self, request, obj=None):
        if obj is None:
            return True
        return obj.added_by == request.user

    def save_model(self, request, obj, form, change):
        obj.added_by = request.user
        return super(BookAdmin, self).save_model(request, obj, form, change)


admin.site.register(Translator)
admin.site.register(Genre)
admin.site.register(Book, BookAdmin)
admin.site.register(Author)
