from django.contrib import admin
import nested_admin
from .models import Taxes, Currencies, Countries, Provinces, District, Categories, Notifications

# Register your models here.

class DistrictTabular(nested_admin.NestedTabularInline):
    model = District
    extra = 0
    min_num = 1

class ProvincesTabular(nested_admin.NestedTabularInline):
    model = Provinces
    extra = 0
    min_num = 1
    inlines = [DistrictTabular]
    
class CountriesAdmin(nested_admin.NestedModelAdmin):
    inlines = [ProvincesTabular]
    search_fields = ('name',)

class DistrictTab(admin.TabularInline):
    model = District
    extra = 0
    min_num = 1

class ProvincesAdmin(admin.ModelAdmin):
    inlines = [DistrictTab]
    search_fields = ('name',)

class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name','slug',)
    exclude = ('parent_id','lft','rgt','depth',)

admin.site.register(Provinces, ProvincesAdmin)
admin.site.register(Countries, CountriesAdmin)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register([Taxes, Currencies, Notifications])