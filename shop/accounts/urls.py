from django.urls import path
from .views import CreateAdminView, CustomerSignupView, LoginView

urlpatterns = [
    path('admin/create/', CreateAdminView.as_view(), name='create-admin'),
    path('signup/', CustomerSignupView.as_view(), name='customer-signup'),
    path('login/', LoginView.as_view(), name='login'),
]