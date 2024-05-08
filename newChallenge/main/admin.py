from django.contrib import admin
from .models import User, Ads, Comments
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ['id', 'email', 'is_authorized', 'created_ts', 'is_staff', 'is_deleted']

@admin.register(Ads)
class AdsAdmin(admin.ModelAdmin):
    model = Ads
    list_display = ['id', 'user', 'title', 'content', 'created_ts', 'is_active', 'is_deleted']
    
@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    model = Comments
    list_display = ['id', 'user', 'ad', 'content', 'created_ts', 'is_deleted']