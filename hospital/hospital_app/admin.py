from django.contrib import admin
from .models import *

class HospitalDrugsInline(admin.TabularInline):
    model = HospitalDrugs
    extra = 1

class HospitalAdmin (admin.ModelAdmin):
    inlines = [HospitalDrugsInline,]
    exclude = ("added_by",)

    def get_readonly_fields(self, request, obj = None):
        if obj is None or obj.added_by ==request.user:
            return []
        return ["name","address",]

    def save_model(self, request, obj, form, change):
        obj.added_by = request.user
        return super(HospitalAdmin,self).save_model(request, obj, form, change)

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj = None):
        return obj and obj.added_by == request.user

    def has_change_permission(self, request, obj=None):
        return obj and request.user.is_superuser

class DoctorAdmin (admin.ModelAdmin):
    exclude = ("added_by",)

    def save_model(self, request, obj, form, change):
        obj.added_by = request.user
        return super(DoctorAdmin, self).save_model(request, obj, form, change)

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return obj and obj.added_by == request.user

    def has_change_permission(self, request, obj=None):
        return obj and obj.added_by == request.user

class PatientAdmin (admin.ModelAdmin):
    exclude = ("added_by",)

    def save_model(self, request, obj, form, change):
        obj.added_by = request.user
        return super(PatientAdmin, self).save_model(request, obj, form, change)

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return obj and obj.added_by == request.user

    def has_change_permission(self, request, obj=None):
        return obj and obj.added_by == request.user

class DrugAdmin (admin.ModelAdmin):
    list_filter = ["drug_type","prescription_required",]
admin.site.register(Hospital,HospitalAdmin)
admin.site.register(Address)
admin.site.register(Patient, PatientAdmin)
admin.site.register(Drug, DrugAdmin)
admin.site.register(Doctor,DoctorAdmin)