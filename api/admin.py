from django.contrib.admin import ModelAdmin, register

from .models import Category, Comment, Genre, Review, Title, User


@register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ('id', 'name', 'slug')
    search_fields = ('name',)
    empty_value_display = '-пусто-'


@register(Genre)
class GenreAdmin(ModelAdmin):
    list_display = ('id', 'name', 'slug')
    search_fields = ('name',)
    empty_value_display = '-пусто-'


@register(Title)
class TitleAdmin(ModelAdmin):
    list_display = ('id', 'name', 'year', 'description', 'category')
    search_fields = ('name',)
    list_filter = ('year',)
    empty_value_display = '-пусто-'


@register(Review)
class ReviewAdmin(ModelAdmin):
    list_display = ('id', 'text', 'author', 'score', 'pub_date')
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


@register(Comment)
class CommentAdmin(ModelAdmin):
    list_display = ('id', 'text', 'author', 'pub_date')
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


@register(User)
class UserAdmin(ModelAdmin):
    list_display = ('email', 'username', 'role')
    search_fields = ('username',)
    empty_value_display = '-пусто-'
