from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile
from django.forms import Select

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from crispy_forms.bootstrap import TabHolder, Tab


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30,
                                 required=True)
    last_name = forms.CharField(max_length=30,
                                required=True)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "password1", "password2")


class UserProfileForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False
    helper.form_show_errors = False
    helper.layout = Layout(
        TabHolder(
            Tab(
                'Personal Information',
                'address',

                'phone_number',
                'emergency_contact_name',
                'emergency_contact_number',
            ),
            Tab(
                'Dog Information',
                'dog_name',
                'age',
                'gender',
                'breed',
                'weight',
                'dob',
                'friendly_with_kids',
                'friendly_with_dogs',
                'spray_neutered',
            ),
            Tab(
                'Medical Information',
                'medical_conditions',
                'specify_condition',
                'requires_medication',
                'which_medication',
                'house_trained',
                'separation_anxiety',
                'feel_at_home',
                'legible_tags',
                'good_on_leash',
            ),
            Tab(
                'Feeding',
                'food_brand',
                'directions',
                'treats',
                'food_allergy',
            ),
            Tab(
                'Vet Info',
                'vet_name',
                'ver_phone_number',
            ),
        ),
    )

    class Meta:
        model = UserProfile
        fields = ['address', 'phone_number', 'emergency_contact_name', 'emergency_contact_number',
                  'dog_name', 'age', 'gender', 'breed', 'weight', 'dob', 'friendly_with_kids',
                  'friendly_with_dogs', 'spray_neutered',
                  'medical_conditions', 'specify_condition', 'requires_medication', 'which_medication',
                  'house_trained', 'separation_anxiety', 'feel_at_home', 'legible_tags',
                  'good_on_leash',
                  'food_brand', 'directions', 'treats', 'food_allergy',
                  'vet_name', 'ver_phone_number']
        labels = {'address': 'Address \n',
                  'emergency_contact_name': 'Emergency contact\'s name',
                  'emergency_contact_number': 'Emergency contact\'s phone number',
                  'dog_name': 'Your dog\'s name',
                  'age': 'Dog\'s age',
                  'gender': 'Dog\'s gender',
                  'dob': 'Dog\'s date of birth',
                  'friendly_with_kids': 'Is your dog friendly with kids',
                  'friendly_with_dogs': 'Is your dog friendly with other dogs',
                  'spray_neutered': 'Is your dog sprayed or neutered',
                  'medical_conditions':'Does your dog have any medical conditions',
                  'specify_condition': 'Please describe the medical condition if your dog has one',
                  'requires_medication': 'Does your dog require any medication',
                  'which_medication': 'What medication(s) does your dog require',
                  'house_trained': 'Is your dog house trained',
                  'separation_anxiety': 'Does your dog have any separation anxiety',
                  'feel_at_home': 'What can we do to ensure your dog feels at home during his/her stay',
                  'legible_tags': 'Does your dog have legible dog tags',
                  'good_on_leash': 'Please describe how your dog is on the leash',
                  'food_brand': 'What brand of food do you feed your dog',
                  'directions': 'How much food, and what time do you feed your dog',
                  'food_allergy': 'Please describe any allergies your dog may have',
                  'vet_name': 'Vet\'s name',
                  'ver_phone_number': 'Vet\'s phone number',
                  }

"""
    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        #self.helper.form_class = 'form-inline'
        #self.helper.field_template = 'bootstrap3/layout/inline_field.html'
        #self.helper.label_class = 'col-md-12'
        #self.helper.field_class = 'col-md-8'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            TabHolder(
                Tab(
                    'Personal Information',
                    'address',
                    'phone_number',
                    'emergency_contact_name',
                    'emergency_contact_number',
                ),
                Tab(
                    'Dog Information',
                    'dog_name',
                    'age',
                    'gender',
                    'breed',
                    'weight',
                    'dob',
                    'friendly_with_kids',
                    'friendly_with_dogs',
                    'spray_neutered',
                ),
                Tab(
                    'Medical Information',
                    'medical_conditions',
                    'specify_condition',
                    'requires_medication',
                    'which_medication',
                    'house_trained',
                    'separation_anxiety',
                    'feel_at_home',
                    'legible_tags',
                    'good_on_leash',
                ),
                Tab(
                    'Feeding',
                    'food_brand',
                    'directions',
                    'treats',
                    'food_allergy',
                ),
                Tab(
                    'Vet Info',
                    'vet_name',
                    'ver_phone_number',
                ),

            ),
        ),
        self.helper.form_show_errors = False
"""

"""
fields = ['phone_number', 'emergency_contact_name', 'emergency_contact_number',
                  'dog_name', 'age', 'gender', 'breed', 'weight', 'dob', 'friendly_with_kids',
                  'friendly_with_dogs', 'spray_neutered',
                  'medical_conditions', 'specify_condition', 'requires_medication', 'which_medication',
                  'house_trained', 'separation_anxiety', 'feel_at_home', 'legible_tags',
                  'good_on_leash',
                  'food_brand', 'directions', 'treats', 'food_allergy',
                  'vet_name', 'ver_phone_number']
        labels = {'address': 'Address \n',
                  'emergency_contact_name': 'Emergency contact\'s name',
                  'emergency_contact_number': 'Emergency contact\'s phone number',
                  'dog_name': 'Your dog\'s name',
                  'age': 'Dog\'s age',
                  'gender': 'Dog\'s gender',
                  'dob': 'Dog\'s date of birth',
                  'friendly_with_kids': 'Is your dog friendly with kids',
                  'friendly_with_dogs': 'Is your dog friendly with other dogs',
                  'spray_neutered': 'Is your dog sprayed or neutered',
                  'medical_conditions':'Does your dog have any medical conditions',
                  'specify_condition': 'Please describe the medical condition if your dog has one',
                  'requires_medication': 'Does your dog require any medication',
                  'which_medication': 'What medication(s) does your dog require',
                  'house_trained': 'Is your dog house trained',
                  'separation_anxiety': 'Does your dog have any separation anxiety',
                  'feel_at_home': 'What can we do to ensure your dog feels at home during his/her stay',
                  'legible_tags': 'Does your dog have legible dog tags',
                  'good_on_leash': 'Please describe how your dog is on the leash',
                  'food_brand': 'What brand of food do you feed your dog',
                  'directions': 'How much food, and what time do you feed your dog',
                  'food_allergy': 'Please describe any allergies your dog may have',
                  'vet_name': 'Vet\'s name',
                  'ver_phone_number': 'Vet\'s phone number',
                  }
"""
