from django.contrib import admin

from ads.models import Location, User, Category, Ad


# admin.site.register(Ad)
@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'price', 'is_published')
    search_fields = ('name', 'description')
    list_filter = ('is_published',)


# admin.site.register(Category)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


# admin.site.register(Location)
@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    pass


# admin.site.register(User)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name')
    search_fields = ('username',)
    list_filter = ('role',)
