from django.contrib import admin
from .models import std_registration, mntr_registration

# Register your models here.
admin.site.register(std_registration)
admin.site.register(mntr_registration)
