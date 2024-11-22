from django.contrib import admin
from .models import ( 
    Department,
    Employee,
    About,
    Contact,
    Team,
    Slider,
    SEO
 )

admin.site.site_header = "Employees Admin "
admin.site.site_title= "Admin Panel"
admin.site.index_title = "Welcome dear Employees Admin"


class EmployeeAdmin(admin.ModelAdmin):
    list_display =("id","first_name", "last_name", "email", "salary","is_married")



class EmployeeInline(admin.TabularInline):
    model = Employee
    exclude = ["contract_exp","created_at"]
    extra = 1




class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    fieldsets= [
        (None, {"fields":["title"]}),
        ("Dates", {
            "fields": ["created_at"],
            "classes": ["collapse"]
        })
    ]
    inlines = [EmployeeInline]



admin.site.register(Department, DepartmentAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(About)
admin.site.register(Contact)
admin.site.register(Team)
admin.site.register(Slider)
admin.site.register(SEO)

