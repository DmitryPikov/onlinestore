from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.models import Article


class ArticleListView(ListView):
    model = Article

    def get_queryset(self):
        return super().get_queryset().filter(publication_at=True)


class ArticleDetailView(DetailView):
    model = Article

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.quantity_count += 1
        self.object.save()
        return self.object


class ArticleCreateView(CreateView):
    model = Article
    fields = ('name', 'description', 'photo', 'publication_at', 'quantity_count')
    success_url = reverse_lazy('blog:article_list')


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ('name', 'description', 'photo', 'publication_at', 'quantity_count')
    success_url = reverse_lazy('blog:article_list')

    def get_success_url(self):
        return reverse('blog:article_detail', args=[self.kwargs.get('pk')])


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('blog:article_list')
