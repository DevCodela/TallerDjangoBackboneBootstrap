from rest_framework import serializers

from .models import Book, Author, Favourite, Comment

class AuthorSerializer(serializers.ModelSerializer):

	class Meta:
		model = Author
		fields = ('id', 'name', 'photo')


class BookSerializer(serializers.ModelSerializer):

	author = AuthorSerializer()
	favourites = serializers.SerializerMethodField()
	comments = serializers.SerializerMethodField()

	def get_favourites(self, book):
		return Favourite.objects.filter(book = book).count()

	def get_comments(self, book):
		return Comment.objects.filter(book = book).count()

	class Meta:
		model = Book
		fields = ('id','author' ,'title', 'slug', 'image', 
					'description', 'favourites', 'comments')


class FavouriteSerializer(serializers.ModelSerializer):

	class Meta:
		model = Favourite
		fields = ('id' ,'user', 'book')


class CommentSerializer(serializers.ModelSerializer):

	class Meta:
		model = Comment