from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class HolidayRequest(models.Model):
    start_date = models.DateField("Start Date")
    end_date = models.DateField("End Date")
    id = models.UUIDField(primary_key=True, unique=True)
    requested_by = models.ForeignKey(User, on_delete=models.CASCADE)

class HolidayResponse(models.Model):
    approved = models.BooleanField("Approved?")
    responded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    responded_to = models.ForeignKey(HolidayRequest, on_delete=models.CASCADE)