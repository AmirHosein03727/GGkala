from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from . import models
from Products.models import SexToys
from django.db.models import Count, Avg


class MainList(ListView):
    template_name = 'Category/sextoys_list.html'
    queryset = SexToys.object.return_published_product()


class CategoryList(ListView):
    paginate_by = 28
    template_name = 'Category/sex_toys_slug.html'

    def get_queryset(self):
        global category
        global sorted_by
        global averege_rate

        sorted_by = self.request.GET.get('sorted-by')
        slug = self.kwargs.get('slugname')
        category = get_object_or_404(models.Category.objects.return_truestatus(), slug=slug)
        f = category.sexy_toys_related_name.return_published_product()

        if sorted_by == "score":
            return f.annotate(res_off=Avg('review__rate')).order_by('-res_off')
        elif sorted_by == "newst":
            return f
        elif sorted_by == "price-down":
            return f.order_by('real')
        elif sorted_by == "price-up":
            return f.order_by('-real')
        else:
            return f.annotate(res_off=Count('hits')).order_by('-res_off')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cat'] = category
        context['val'] = sorted_by
        return context
