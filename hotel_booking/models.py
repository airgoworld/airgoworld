from django.core.exceptions import ValidationError
from user.models import CustomUser as User
from django.utils.timezone import now
from hotel.models import Hotel
from django.db import models


class HotelBooking(models.Model):
    total_bill = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booked_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    display = models.BooleanField(default=True)
    check_out_date = models.DateTimeField()
    check_in_date = models.DateTimeField()
    occupants = models.IntegerField()
    
    def __str__(self):
        return self.total_bill

    def save(self, *args, **kwargs):
        if self.check_in_date and self.check_in_date < now():
            raise ValidationError("Check-in date must be from today onwards.")
        if self.check_in_date and self.check_out_date:
            num_days = (self.check_out_date - self.check_in_date).days
            if num_days <= 0:
                raise ValidationError("Check-out date must be after check-in date.")
            self.total_bill = self.price * num_days
        super().save(*args, **kwargs)
