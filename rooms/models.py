from django.db import models
from common.models import CommonModel

class Room(CommonModel):

    """ Room model Definition"""
    class RoomKindChoices(models.TextChoices):
        ENTIRE_PLACE = ("entire_place", "Entire Place")
        PRUVARE_ROOM = ("private_room", "Private Room")
        SHARED_ROOM = "shared_room", "shared Room"

    name = models.CharField(
        max_length=180, 
        default= ""
    )    

    contry = models.CharField(
        max_length=50, 
        default="한국",
    )
    city = models.CharField(
        max_length=80, 
        default="서울"
    )
    price = models.PositiveIntegerField(

    )
    rooms = models.PositiveIntegerField(

    )
    toilets = models.PositiveIntegerField(

    )
    description = models.TextField(

    )
    address = models.CharField(
        max_length=250,
    )
    pet_friendly = models.BooleanField(
        default=True,
    )
    kind = models.CharField(
        max_length=20, 
        choices=RoomKindChoices.choices,
    )
    owner = models.ForeignKey(
        "users.User", 
        on_delete=models.CASCADE
    )
    amenities = models.ManyToManyField(
        "rooms.Amenity",
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self) -> str:
        return self.name
    
     

class Amenity(CommonModel):

    """ Amenity Definition """

    name = models.CharField(
        max_length=150
    )
    description = models.CharField(
        max_length=150,
        null=True     
    )

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name_plural = "Amenities"