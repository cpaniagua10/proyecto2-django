from django.contrib import admin
from .models import Ticket, Seat
# Register your models here.

def delete_and_free_seat(modeladmin, request, queryset):
    for ticket in queryset:
        seat = ticket.seat
        Seat.objects.filter(pk=seat.pk).update(full=False)
        ticket.delete()

class TicketAdmin(admin.ModelAdmin):

    def has_delete_permission(self, request, obj=None):
        return False
        
    actions = [delete_and_free_seat]

admin.site.register(Ticket, TicketAdmin)
admin.site.register(Seat)
