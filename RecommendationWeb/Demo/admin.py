from django.contrib import admin
from .models import FieldOfStudy, University, Major, UniMajor, Campus, Combination, CombMajor, Region, UniField

admin.site.register(FieldOfStudy)
admin.site.register(University)
admin.site.register(Major)
admin.site.register(UniMajor)
admin.site.register(Campus)
admin.site.register(Combination)
admin.site.register(CombMajor)
admin.site.register(Region)
admin.site.register(UniField)