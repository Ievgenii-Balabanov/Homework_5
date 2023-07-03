import datetime


from catalog.models import City, Client, Logging, Person, Product, Supplier

from django.contrib import admin
from django.utils import timezone


class LoggingAdmin(admin.ModelAdmin):
    list_display = ["path", "method", "created_date", "method_checking"]

    fieldsets = [
        ("Path", {"fields": ["path"]}),
        ("Method", {"fields": ["method"]}),
    ]

    search_fields = ["path"]
    list_filter = ["created_date"]

    @admin.display(boolean=True, ordering="created_date", description="Was it created recently?")
    def method_checking(self, obj):
        now = timezone.now()
        return obj.created_date - datetime.timedelta(days=1) <= obj.created_date <= now


admin.site.register(Client)
admin.site.register(City)
admin.site.register(Product)
admin.site.register(Supplier)
admin.site.register(Person)
admin.site.register(Logging, LoggingAdmin)
