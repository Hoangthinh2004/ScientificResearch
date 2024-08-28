from .models import University, Major, FieldOfStudy, Region, Campus

def getType(uni):
    type = set()
    for x in uni:
        type.add(x.Type)
    return type

def global_parameters(request):
    unis_global = University.objects.all()
    majors_global = Major.objects.all()
    fields_global = FieldOfStudy.objects.all()
    region_global = Region.objects.all()
    campus_global = Campus.objects.all()
    type_global = getType(unis_global)
    return {'unis_globals': unis_global,
            'majors_globals': majors_global,
            'fields_globals': fields_global,
            'region_globals': region_global,
            'type_globals': type_global,
            'campus_globals': campus_global,
            }