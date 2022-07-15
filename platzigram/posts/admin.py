# Django
from django.contrib import admin
# Models
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'modified')
    list_display_links = ('user',)

    search_fields = (
        'user__email',
        'user__username',
        'user__first_name',
        'user__last_name',
        'title'
    )

    list_filter = (
        'user__is_active',
        'user__is_staff',
        'modified',
    )

    fieldsets = (
        ('User info', {
            'fields': (('user', 'profile'),)
        }),
        ('Post info', {
            'fields': (
                ('title', 'photo'),
            )
        }),
        ('Metadata', {
            'fields': (('created', 'modified'),),
        })
    )

    readonly_fields = ('created', 'modified',)
