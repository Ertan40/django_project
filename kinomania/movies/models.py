from django.db import models
from kinomania.movies.validators import validate_file_size, validate_year
from django.template.defaultfilters import slugify

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=120, unique=True, null=False, blank=False)
    year = models.PositiveIntegerField(validators=(validate_year,), null=False, blank=False)
    genres = models.CharField(max_length=50, default="Action | Comedy | Romance | Horror | Thriller")
    description = models.TextField(null=False, blank=False)
    image = models.ImageField(upload_to='images/', validators=(validate_file_size,), null=True, blank=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    duration = models.CharField(max_length=20, null=False, blank=False)
    trailer = models.CharField(max_length=300, default="null")
    rdate = models.CharField(max_length=20, default="null")
    imdb_link = models.URLField(null=False, blank=False, verbose_name="Link to IMDB")
    slug = models.SlugField(null=False, blank=True, unique=True, editable=False)
    is_active = models.BooleanField(default=True, null=False, blank=False)

    def save(self, *args, **kwargs):
        # create/update
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f'{self.name}-{self.year}')
        # update # slug: the-beekeeper-2023
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} ({self.year})'
