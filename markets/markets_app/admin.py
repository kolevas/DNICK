
from django.contrib import admin
from .models import *


class MarketProductInline(admin.TabularInline):
    model = MarketProducts
    extra = 1

class MarketAdmin(admin.ModelAdmin):
    inlines = [MarketProductInline, ]
    exclude = ("added_by",)
    list_display = ("name",)

    def save_model(self, request, obj, form, change):
        obj.added_by = request.user
        return super(MarketAdmin, self).save_model(request, obj, form, change)

    def has_delete_permission(self, request, obj = None):
        if obj and obj.added_by == request.user and request.user.is_superuser:
            return True
        return False
    def has_change_permission(self, request, obj = None):
        if obj and obj.added_by == request.user and request.user.is_superuser:
            return True
        return False

    def has_add_permission(self, request, obj = None):
        if request.user.is_superuser:
            return True
        return False

class EmployeeAdmin(admin.ModelAdmin):
    exclude = ("employer",)
    list_display = ("first_name","last_name",)
    def save_model(self, request, obj, form, change):
        obj.employer = request.user
        return super(EmployeeAdmin, self).save_model(request, obj, form, change)
    def has_delete_permission(self, request, obj = None):
        if obj and obj.employer == request.user:
            return True
        return False
    def has_change_permission(self, request, obj = None):
        if obj and obj.employer == request.user:
            return True
        return False


class ProductAdmin(admin.ModelAdmin):
    list_filter =("product_type","is_homemade",)
    list_display = ("name","product_type","is_homemade", "code",)



admin.site.register(Market, MarketAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(ContactInfo)