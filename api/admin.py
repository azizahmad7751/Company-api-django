from django.contrib import admin
from api.models import Company, Employee


#customazation in company admin panel
class CompanyAdmin(admin.ModelAdmin):
	list_display=('name','location','type')
	#Creating Search field in company section
	search_fields=('name',)
#customazation in Employee admin panel
class EmployeeAdmin(admin.ModelAdmin):
	list_display=('name', 'address','about')
    #Creating Search field in employee section
	search_fields=('name',)
	#creating filter to search employees company wise.
	list_filter=('Company',)
# Register your models here.
admin.site.register(Company, CompanyAdmin)
admin.site.register(Employee, EmployeeAdmin)