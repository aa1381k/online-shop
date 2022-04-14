from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.list import ListView
from .models import articlemodel, articlecategorymodel, articlecomments
from jalali_date import datetime2jalali, date2jalali
# Create your views here.

class articleslist(ListView):
    model = articlemodel
    paginate_by = 2
    template_name = 'article_module/articles_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(articleslist, self).get_context_data(*args,**kwargs)
        context['date'] = date2jalali(self.request.user.date_joined)
        return  context

    def get_queryset(self):
        query = super(articleslist, self).get_queryset()
        query = query.filter(is_active=True)
        category_name = self.kwargs.get('category')
        if category_name is not None:
            query = query.filter(selected_category__url_title__iexact=category_name)
        return  query


class articledetailview(DetailView):
    model = articlemodel
    template_name = 'article_module/article_detail.html'

    def get_queryset(self):
        query = super(articledetailview, self).get_queryset()
        query = query.filter(is_active=True)
        return query

    def get_context_data(self, **kwargs):
        query = super(articledetailview, self).get_context_data()
        query['comments'] = articlecomments.objects.filter(parent=None).prefetch_related('articlecomments_set')
        query['all_comments'] = articlecomments.objects.all
        return query




def article_categories_componnent(request):
    categories = articlecategorymodel.objects.filter(is_active=True,parrent_id=None)
    context = {
        'categories' : categories
    }
    return render(request,'componnents/componnents.html',context)