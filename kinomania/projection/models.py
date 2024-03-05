from django.db import models
from kinomania.halls.models import Halls
from kinomania.movies.models import Movie
from django.template.defaultfilters import slugify
# Create your models here.
class Projection(models.Model):
    date = models.DateField(null=False, blank=False)
    hour = models.TimeField(null=False, blank=False)
    hall = models.ForeignKey(Halls, on_delete=models.CASCADE, null=False, blank=False)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=False, blank=False)
    slug = models.SlugField(editable=False, unique=True, null=False, blank=True, max_length=120)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f"{self.date}-{self.hour}-{self.hall.name}-{self.movie.name}")
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.date} - {self.hour.strftime('%H:%M')} - {self.hall} - {self.movie}"



class Seat(models.Model):
    projection = models.ForeignKey(Projection, on_delete=models.CASCADE, null=False, blank=False)
    row_n = models.CharField(null=False, blank=False)
    seat_n = models.CharField(null=False, blank=False)
    is_taken = models.BooleanField(default=False, null=False, blank=False)


