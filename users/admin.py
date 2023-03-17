from django.contrib import admin
from .models import Posts, LikedPost, Comments, Friends

@admin.register(Posts)
class UsersPostsTable(admin.ModelAdmin):
    list_display = ['user', 'total_likes', 'posted']

@admin.register(LikedPost)
class LikedPostsTable(admin.ModelAdmin):
    list_display = ['id', 'username', 'liked']


@admin.register(Comments)
class CommentsTable(admin.ModelAdmin):
    list_display = ['name', 'comment']

@admin.register(Friends)
class FriendsTable(admin.ModelAdmin):
    list_display = ['following', 'followed', 'created']