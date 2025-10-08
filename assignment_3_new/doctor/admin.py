from django.contrib import admin
from .models import Doctor

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'experience_years', 'is_active')
    list_filter = ('department', 'is_active')
    search_fields = ('name',)
