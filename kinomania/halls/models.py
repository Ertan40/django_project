from django.db import models
from kinomania.movies.validators import validate_file_size
from django.template.defaultfilters import slugify
# Create your models here.
class Halls(models.Model):
    name = models.CharField(max_length=40, null=False, blank=False)
    rows = models.PositiveIntegerField(null=False, blank=False)
    seats_per_row = models.PositiveIntegerField(null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    image = models.ImageField(upload_to='images/', validators=(validate_file_size,), null=False, blank=False)
    slug = models.CharField(unique=True, null=False, blank=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f"{self.name}-{self.id}")
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"
