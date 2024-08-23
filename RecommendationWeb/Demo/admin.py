from django.contrib import admin
from .models import FieldOfStudy, University, Major, UniMajor

admin.site.register(FieldOfStudy)
admin.site.register(University)
admin.site.register(Major)
admin.site.register(UniMajor)