from django.contrib import admin
# Register your models here.
from .models import Listing

# either use this decorator or admin.site... at the end(!)
@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
    list_display_links = ('id', 'title')
    list_filter = ('realtor',) # , at the end to make it a tuple
    list_editable = ('is_published',) # , at the end to make it a tuple 
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')
    list_per_page = 20

#admin.site.register(Listing, ListingAdmin) # needs to be at the end / use the decorator instead.
