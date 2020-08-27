from django.contrib import admin
from .models import User, Category, Genre, Title, Review, Comment


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("pk", "email", "role", "bio")

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "slug")


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "slug")


@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "year", "description",)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("pk", "author", "text", "pub_date", "score", "title", "rating")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("pk", "author", "text", "pub_date", "review")
