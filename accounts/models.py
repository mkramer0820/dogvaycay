from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    user = models.ForeignKey(User)
    address = models.TextField(max_length=100)
    phone_number = models.CharField(max_length=13)
    emergency_contact_name = models.CharField(max_length=25)
    emergency_contact_number = models.CharField(max_length=13)


    # Guest Pupinfo
    dog_name = models.CharField(max_length=25)
    age = models.CharField(max_length=2)
    gender = models.CharField(max_length=1)
    breed = models.CharField(max_length=25)
    weight = models.CharField(max_length=3)
    dob = models.DateField(auto_now_add=False)
    friendly_with_kids = models.CharField(max_length=3)
    friendly_with_dogs = models.CharField(max_length=3)
    spray_neutered = models.CharField(max_length=3)

    # Behavioral and medical info
    medical_conditions = models.CharField(max_length=3)
    specify_condition = models.TextField(max_length=200)
    requires_medication = models.CharField(max_length=3)
    which_medication = models.TextField(max_length=200)
    house_trained = models.CharField(max_length=3)
    separation_anxiety = models.CharField(max_length=3)
    feel_at_home = models.TextField(max_length=200)
    legible_tags = models.CharField(max_length=3)
    good_on_leash = models.TextField(max_length=100)

    # feeding
    food_brand = models.CharField(max_length=25)
    directions = models.TextField(max_length=100)
    treats = models.CharField(max_length=3)
    food_allergy = models.TextField(max_length=200)

    # vet info
    vet_name = models.CharField(max_length=25)
    ver_phone_number = models.CharField(max_length=13)

    def __str__(self):
        return self.user.username












