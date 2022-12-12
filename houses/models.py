from django.db import models


class House(models.Model):

    """Model Definition for Houses"""

    name = models.CharField(max_length=140)
    price_per_night = models.PositiveBigIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=140)
    pets_allowed = models.BooleanField(
        verbose_name="pets Allowed?",
        default=True,
        help_text="Dose this house allow pets?"
    )

    def __str__(self):
        return self.name
