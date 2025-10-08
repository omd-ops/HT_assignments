from django.db import models

class Doctor(models.Model):
    DEPARTMENTS = (
        ('cardiology', 'Cardiology'),
        ('dermatology', 'Dermatology'),
        ('orthopedics', 'Orthopedics'),
        ('neurology', 'Neurology'),
    )

    name = models.CharField(max_length=100)
    department = models.CharField(max_length=50, choices=DEPARTMENTS)
    experience_years = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.get_department_display()})"


