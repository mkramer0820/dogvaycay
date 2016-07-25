from django.db import models


YES_NO_Choices = (
    ('Yes', 'Yes'),
    ('No', 'No')
)


class Dog(models.Model):
    """model for dog name"""
    dogs_name = models.CharField(max_length=30)

    def __str__(self):
        return self.dogs_name


class DogInfo(models.Model):
    dog_name = models.ForeignKey(Dog)
    age = models.IntegerField()
    gender = models.CharField(max_length=6, choices=(('Male', 'Male'), ('Female', 'Female')))
    breed = models.CharField(max_length=20)
    weight_pounds = models.IntegerField()
    birthday = models.DateField()
    friendly_with_kids = models.CharField(max_length=3, choices=YES_NO_Choices)
    friendly_with_other_dogs = models.CharField(max_length=3, choices=YES_NO_Choices)
    house_trained = models.CharField(max_length=3, choices=YES_NO_Choices)
    feel_at_home = models.TextField()
    clearly_identifiable_dog_tags = models.CharField(max_length=3, choices=YES_NO_Choices)
    dog_good_on_leash = models.TextField()


class DogMedicalInfo(models.Model):
    dog_name = models.ForeignKey(Dog)
    rabies_vaccination = models.BooleanField(default=False)
    bordetella_vaccination = models.BooleanField(default=False)
    DHLP_vaccination = models.BooleanField(default=False)
    neutered = models.CharField(max_length=3, choices=YES_NO_Choices)
    medical_condition = models.CharField(max_length=3, choices=YES_NO_Choices, )
    medical_condition_description = models.TextField()
    medication = models.CharField(max_length=3, choices=YES_NO_Choices)
    medication_type = models.TextField()
    separation_anxiety = models.CharField(max_length=3, choices=YES_NO_Choices)


class DogFeeding(models.Model):
    dog_name = models.ForeignKey(Dog)
    food_brand = models.CharField(max_length=30)
    food_directions = models.TextField()
    breakfast_feed_time = models.TimeField()
    dinner_feed_time = models.TimeField()
    treats = models.CharField(max_length=3, choices=YES_NO_Choices)
    any_allergies = models.TextField()


class Contact(models.Model):
    dog_name = models.ForeignKey(Dog)
    parent_name = models.CharField(max_length=25)
    telephone_number = models.CharField(max_length=12)
    email = models.EmailField(max_length=35)
    address = models.CharField(max_length=250)
    zip = models.CharField(max_length=5)
    emergency_contact_name = models.CharField(max_length=25)
    emergency_contact_number = models.CharField(max_length=12)
    vet_name = models.CharField(max_length=25)
    ver_number = models.CharField(max_length=12)
    sig = models.CharField(max_length=30)
    date_signed = models.DateTimeField(auto_now_add=True)

