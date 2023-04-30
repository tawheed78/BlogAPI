import django_filters
from .models import Post

class PostContentFilter(django_filters.FilterSet):
    q = django_filters.CharFilter(method='search_posts')

    class Meta:
        model = Post
        fields = ['q']

    def search_posts(self, queryset, name, value):
        return queryset.filter(title__icontains=value) | queryset.filter(body__icontains=value)