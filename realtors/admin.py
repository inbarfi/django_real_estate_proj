from django.contrib import admin
# Register your models here.
from .models import Realtor

#@admin.register(Realtor)
class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'hire_date')
    list_display_links = ('id', 'name')
    search_fields = ('name',) # put , to make it a touple
    list_per_page = 20

admin.site.register(Realtor, RealtorAdmin) #has to be at the end id decorator not beeing used at top