from ckeditor.fields import RichTextField
from django.db import models
from django.conf import settings
# Create your models here.


class Site(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    logo = models.ImageField(upload_to='logo/')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    description = models.TextField()

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    description = models.TextField()

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    content = RichTextField()
    featured_image = models.ImageField(upload_to='images/')
    is_published = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateField(auto_now=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)

    def __str__(self):
        return self.title
