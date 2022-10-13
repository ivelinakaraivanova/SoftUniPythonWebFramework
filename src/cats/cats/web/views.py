from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView

from cats.web.models import Cat


def index(request):
    context = {
        'title': 'Hello from FBV',

    }
    return render(request, 'index.html', context)


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Hello from CBV'
        }


def show_cats(request):
    cats = Cat.objects.all()
    context = {
        'cats': cats,
        'cats_title': 'Hello FBV cats'
    }

    return render(request, 'cats-list.html', context)


class CatCreateView(CreateView):
    model = Cat
    fields = '__all__'
    template_name = 'create-cat.html'
    success_url = reverse_lazy('cbv show cats')


class ShowCatsListView(ListView):
    model = Cat
    template_name = 'cats-list.html'
    context_object_name = 'cats'

    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['cats_title'] = 'Hello CBV cats'
        return context
