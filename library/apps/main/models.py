from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Author(models.Model):

	name = models.CharField(max_length=100)
	photo = models.ImageField(upload_to = 'authors')

	def __unicode__(self):
		return self.name

class Book(models.Model):

	author = models.ForeignKey(Author)
	title = models.CharField(max_length=100)
	slug = models.SlugField(editable=False)
	image = models.ImageField(upload_to = 'books')
	description = models.TextField(max_length=250)

	def __unicode__(self):
		return self.title

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(Book, self).save(*args, **kwargs)

class Comment(models.Model):

	user = models.ForeignKey(User)
	book = models.ForeignKey(Book)
	comment = models.TextField(max_length=250)
	created = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return "%s / %s" % (self.user.username, self.book.title)

class Favourite(models.Model):

	user = models.ForeignKey(User)
	book = models.ForeignKey(Book)