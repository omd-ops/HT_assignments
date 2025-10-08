from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Doctor

def doctor_list(request):
    # Get query params
    q = request.GET.get('q', '').strip()
    department = request.GET.get('department', '').strip()

    # Base queryset
    qs = Doctor.objects.filter(is_active=True).order_by('-created_at')

    # Search by name
    if q:
        qs = qs.filter(name__icontains=q)

    # Filter by department
    if department:
        qs = qs.filter(department=department)

    # Distinct departments for dropdown
    departments = Doctor.objects.values_list('department', flat=True).distinct()

    # Pagination (10 per page)
    paginator = Paginator(qs, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Preserve query params for pagination links
    params = request.GET.copy()
    if 'page' in params:
        params.pop('page')
    query_string = params.urlencode()

    context = {
        'page_obj': page_obj,
        'q': q,
        'department': department,
        'departments': departments,
        'query_string': query_string,
    }
    return render(request, 'doctor/doctor_list.html', context)

"""from rest_framework import generics, filters
from .models import Doctor
from .serializers import DoctorSerializer
from rest_framework.pagination import PageNumberPagination

# Step 1: Create Pagination class
class DoctorPagination(PageNumberPagination):
    page_size = 2  # show 2 records per page
    page_size_query_param = 'page_size'
    max_page_size = 10

# Step 2: Create a List API View
class DoctorListView(generics.ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    pagination_class = DoctorPagination

    # Step 3: Enable Search and Filter
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'specialization']  # fields to search on
    ordering_fields = ['name', 'experience']    # fields to order by
"""