from django.db import models
from account.models import User
from django.template.defaultfilters import truncatechars
from django.utils.html import format_html
from django.utils.formats import date_format
from django.urls import reverse

# from multiselectfield import MultiSelectField | for multiplay chois

# Manager


class CategoryManager(models.Manager):
    def return_truestatus(self):
        return self.filter(status="True")


class Category(models.Model):
    parent = models.ForeignKey('self', default=None, blank=True, null=True, on_delete=models.SET_NULL, related_name='parents_related')
    category_name = models.CharField(max_length=100)
    page_title = models.CharField(max_length=30, default="جی جی کالا")
    slug = models.SlugField(unique=True)
    status = models.BooleanField(default=True)
    caption = models.TextField(default="")
    photo = models.ImageField(upload_to="Sex-Toys-photo", blank=True)
    position = models.IntegerField(unique=True)

    class Meta:
        ordering = ['parent__id', 'position']

    def __str__(self):
        return self.category_name

    objects = CategoryManager()


def show_category(obj):
    return ", ".join([cat.category_name for cat in obj.category.return_truestatus()])
