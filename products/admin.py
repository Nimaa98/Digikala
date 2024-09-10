from django.contrib import admin
from .models import Product,ProductPrice,ProductOption,Question,Answer,Image,Comment,Category



# Register your models here.

class ImageInline(admin.TabularInline):
    model = Image
    extra = 1


class ProductOptionInline(admin.TabularInline):
    model = ProductOption
    extra = 1


class ProductPriceInline(admin.TabularInline):
    model = ProductPrice
    extra = 1



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'en_name', 'name', 'category']
    list_filter = ['category']
    search_fields = ['en_name', 'name']

    inlines = [ImageInline,ProductOptionInline,ProductPriceInline]
    ##admin.site.register(Image)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'parent']
    list_filter = ['parent']
    search_fields = ['name','description']
    fieldsets = (
        ('details',{
            'fields':('name','slug',
                      'parent',
                      'description')
        }),
        ('images', {
            'fields': ('icon', 'image'),
        }),
    )



@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass








# @admin.register(Image)
# class ImageAdmin(admin.ModelAdmin):
#     pass




