from django.contrib import admin
from .models import Products, Order

# Register your models here.
admin.site.site_header = "E-Commerce Website"
admin.site.site_title = "ABC Shopping"
admin.site.index_title = "Manage ABC Shopping"

class ProductAdmin(admin.ModelAdmin):

    def change_category_to_default(self, request, queryset):
        queryset.update(category="no-category")

    list_display = ('title', 'price', 'discount_price', 'category', 'description')
    search_fields = ('title',)  # Add a comma to make it a tuple
    actions = ('change_category_to_default',)  # Add a comma to make it a tuple
    fields = ('title','price',) # Add a comma to make it a tuple
    list_editable = ('category','price',) # Add a comma to make it a



admin.site.register(Products, ProductAdmin)
admin.site.register(Order)