import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class HolidayRequest(models.Model):
    start_date = models.DateField("Start Date")
    end_date = models.DateField("End Date")
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    requested_date = models.DateField("Requested Date")
    requested_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="requested_by")
    approved = models.BooleanField("Approved?", null=True)
    approved_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="approved_by", null=True)

    def __str__(self):
        return f"Holiday Request: {self.start_date.strftime('%d/%m/%Y')} - {self.end_date.strftime('%d/%m/%Y')}"
    
