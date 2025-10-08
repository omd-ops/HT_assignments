import django_filters
from .models import Doctor

class DoctorFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains', label='Name')
    department = django_filters.ChoiceFilter(field_name='department', choices=Doctor.DEPARTMENTS)

    class Meta:
        model = Doctor
        fields = ['name', 'department']
