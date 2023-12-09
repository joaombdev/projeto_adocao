from django.contrib import admin
from pets.models import Breed
from pets.models import Pet

# Register your models here.
class BreedAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )

admin.site.register(Breed, BreedAdmin)

class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'sex', 'weight', 'age', 'species', 'size', 'breed', 'local', 'about', 'photo')
    search_fields = ('name', )

admin.site.register(Pet, PetAdmin)