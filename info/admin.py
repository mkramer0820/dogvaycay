from django.contrib import admin
from .models import Dog, DogInfo, DogMedicalInfo, DogFeeding, Contact
# Register your models here.


admin.site.register(Dog)
admin.site.register(DogInfo)
admin.site.register(DogMedicalInfo)
admin.site.register(DogFeeding)
admin.site.register(Contact)