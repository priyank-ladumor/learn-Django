
from django.contrib import admin
from .models import Blog, Tag, BlogComment # . means current directory & .models means models.py

# # Simple registration of models without any customizations
# admin.site.register(Blog)
# admin.site.register(Tag)
# admin.site.register(BlogComment)


# Inline model to show comments inside Blog admin page
class BlogCommentInline(admin.TabularInline): # TabularInline is the default inline form layout & can be replaced with StackedInline for a different layout
    model = BlogComment
    extra = 1  # Show 1 extra blank comment inline


# Custom Blog admin
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date', 'blog_type', 'draft')  # Columns shown in list view
    list_filter = ('blog_type', 'draft', 'tags')                # Sidebar filters
    search_fields = ('title', 'description')                    # Search bar
    filter_horizontal = ('tags',)                               # UI for many-to-many field tags on Blog admin form
    inlines = [BlogCommentInline]                               # Show related comments inline


# Custom Tag admin
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('tag_name',)
    search_fields = ('tag_name',)


# Custom BlogComment admin
@admin.register(BlogComment)
class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'blog', 'date') # Columns shown in list view
    # relationModelName__fieldName ex: blog__title # raverses the ForeignKey to User model and searches the username field. This is called Django ORM lookups or field traversal. 
    search_fields = ('comment', 'user__username', 'blog__title')  # Search by comment, username, or blog title & other modals value
    list_filter = ('date',) # Sidebar filter


#other way to register
# admin.site.register(Blog, BlogAdmin)
# admin.site.register(Tag, TagAdmin)
# admin.site.register(BlogComment, BlogCommentAdmin)