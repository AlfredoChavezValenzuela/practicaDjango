from django.contrib import admin

# Register your models here.
from .models import Doctor
admin.site.register(Doctor)

from .models import Paciente
admin.site.register(Paciente)
