from django.db import models

class CommonModel(models.Model):
    """Common Model Definition"""

    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True

