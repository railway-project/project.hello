from django.contrib import admin
from .models import Poem, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0


@admin.register(Poem)
class PoemAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'is_new', 'views')
    list_editable = ('views',)
    list_filter = ('category', 'is_new')
    search_fields = ('title', 'author')
    inlines = [CommentInline]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'poem', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
