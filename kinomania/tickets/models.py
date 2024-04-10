from django.db import models
from django.core.validators import MinValueValidator
# Create your models here.
class Ticket(models.Model):
    ticket_type = models.CharField(null=False, blank=False)
    price = models.DecimalField(max_digits=4, decimal_places=2, validators=[MinValueValidator(0.01)], null=False, blank=False)
    weekend_price = models.DecimalField(max_digits=4, decimal_places=2, validators=[MinValueValidator(0.01)], null=False, blank=False)

    def __str__(self):
        return self.ticket_type