from .models import University, Major, FieldOfStudy

def global_parameters(request):
    unis_global = University.objects.all()
    majors_global = Major.objects.all()
    fields_global = FieldOfStudy.objects.all()
    return {'unis_globals': unis_global,
            'majors_globals': majors_global,
            'fields_globals': fields_global
            }