from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):
    list_display_links = (
        'location',
        'caption',
    )

    search_fields = (
        'location',
        'caption',
    )

    list_filter = (
        'location',
        'caption',
    )

    list_display = (
        'file',
        'location',
        'caption',
        'creator',
        'created_at',
        'updated_at',
    )


@admin.register(models.Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = (
        'image',
        'creator',
        'created_at',
        'updated_at',
    )


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'image',
        'message',
        'creator',
        'created_at',
        'updated_at',
    )
