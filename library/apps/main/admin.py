from django.contrib import admin

from .models import Author, Book, Comment, Favourite

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
	pass

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	pass

@admin.register(Favourite)
class FavouriteAdmin(admin.ModelAdmin):
	pass