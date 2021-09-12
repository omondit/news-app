from articles.models import Article, Comment
from django.contrib import admin


class CommentInline(admin.TabularInline):  # new
    model = Comment
    extra = 0


class ArticleAdmin(admin.ModelAdmin):  # new
    inlines = [CommentInline, ]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
