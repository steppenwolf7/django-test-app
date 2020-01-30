from django.db import models
from django.urls import reverse

# Create your models here.
# https://docs.djangoproject.com/en/2.2/ref/models/fields/#field-types

class Products(models.Model):
    title       = models.CharField(max_length=120)
    description = models.TextField()
    price       = models.DecimalField(null=False, decimal_places=2, max_digits=1000)
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={"id": self.id})

      
    # blank=False - pole jest wymagane w panelu admin
    # null=False - pole moze być puste w bazie danych  