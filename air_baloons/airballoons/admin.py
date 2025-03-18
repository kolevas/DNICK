
from django.contrib import admin
from .models import Airline,AirlinePilot,AirBalloon,Flight,Pilot


class AirlinePilotInline(admin.TabularInline):
    model = AirlinePilot
    extra = 1

class AirlineAdmin(admin.ModelAdmin):
    inlines = [AirlinePilotInline,]


class FlightAdmin(admin.ModelAdmin):
    exclude = ("added_by",)

    def save_model(self, request, obj, form, change):
        obj.added_by = request.user
        return super(FlightAdmin, self).save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        if obj is None:
            return True
        return request.user == obj.added_by
    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(AirBalloon)
admin.site.register(Pilot)
admin.site.register(Airline, AirlineAdmin)
admin.site.register(Flight, FlightAdmin)