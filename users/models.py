from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Profile(models.Model):
    SKIN_TYPES=[
         ('Normal', 'Normal'),
         ('Dry', 'Dry'),
         ('Oily', 'Oily'),
         ('Combination', 'Combination'),
         ('Sensitive', 'Sensitive'),
         ('Acne-prone', 'Acne-prone'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='image/', null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    height = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # cm
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # kg
    skin_type = models.CharField(max_length=50,choices=SKIN_TYPES, blank=True, null=True)
    
    def age(self):
        if self.date_of_birth:
            today = date.today()
            return today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        return None
    
    def __str__(self):
        return f"{self.user.first_name}'s Profile"