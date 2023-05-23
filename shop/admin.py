from django.contrib import admin
from .models import Category, Product, Brand, Review, Contact


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    prepopulated_fields = {'slug': ('name',)}



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'price', 'available', 'created', 'updated')
    list_filter = ('available', 'created', 'updated')
    list_editable = ('price', 'available')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('brand', 'slug',)
    prepopulated_fields = {'slug': ('brand',)}

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email','review_text')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email','message')
