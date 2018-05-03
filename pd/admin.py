from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import UserProfile, Department, Vehicle, Task


class Police_Officer_Inline(admin.TabularInline):
    model = UserProfile
    verbose_name = 'userprofile'
    verbose_name_plural = 'userprofiles'



class CrimeAdmin(admin.ModelAdmin):
    model = Task
    list_display = ('Title', 'Description', 'isComplete', 'Dudate', 'Executed_by')



class DepartmentAdmin(admin.ModelAdmin):
    model = Department
    list_display = ('Name', 'Zip_code', 'Number_of_weapons', 'Number_of_vehicles', 'Number_of_workers', 'Head', 'Area')


class VehicleAdmin(admin.ModelAdmin):
    model = Vehicle
    list_display = ('BelongsTo', 'Plate_number', 'Model', 'isInUse', 'Using_by',)


class TaskAdmin(admin.TabularInline):
    model = Task
    verbose_name = 'task'
    verbose_name_plural = 'tasks'
    list_display = ('Title', 'Description', 'isComplete', 'Dudate', 'Executed_by')



class OfficerAdmin(BaseUserAdmin):
    inlines = (Police_Officer_Inline, TaskAdmin )


admin.site.unregister(User)
admin.site.register(User, OfficerAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(Task, CrimeAdmin)
