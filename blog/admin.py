from django.contrib import admin
from .models import Post, BookReview

#admin.site.register(Post)

# or StackedInline

# class CommentInline(admin.TabularInline):
# 	model = Comment
# 	extra = 0
# 	list_display = ('name', 'text', 'date')


# class PostAdmin(admin.ModelAdmin):
    
#     inlines = [CommentInline]
#     list_display = ('title', 'description', 'date')
#     list_filter = ['date']
#     search_fields = ['text']

# admin.site.register(Post, PostAdmin)


class PostAdmin(admin.ModelAdmin):
    
    list_display = ('title', 'description', 'date')

admin.site.register(Post, PostAdmin)

admin.site.register(BookReview)


