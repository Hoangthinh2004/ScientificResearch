from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpRequest
from .models import University, Major, FieldOfStudy, UniMajor, Region, Campus, CombMajor
from django.db.models import Q

# Create your views here.
def home(request):
    unis = University.objects.all()
    majors = Major.objects.all()
    fieldOfMajors = FieldOfStudy.objects.all()
    if request.method == 'GET' and request.GET.get('s') != None:
        s = request.GET.get('s') 
        unis = University.objects.filter(Q(ID__icontains=s) |
                                    Q(Name__icontains=s) |
                                    Q(Type__icontains=s) |
                                    Q(Description__icontains=s) 
                                    )
        majors = Major.objects.filter(Q(ID__icontains=s) |
                                    Q(Name__icontains=s) |
                                    Q(FieldID__ID__icontains=s) |
                                    Q(FieldID__Name__icontains=s) 
                                    )
        
    context = {'unis': unis, 'majors': majors, 'fieldOfMajors': fieldOfMajors}
    return render(request, 'Demo/home.html', context)

def listUniversity(request):
    unis = University.objects.all()
    if request.method == 'GET':
        u = request.GET.get('u')
        unis = University.objects.filter(Q(ID__icontains=u) |
                                    Q(Name__icontains=u))
    context = {'unis': unis}
    return render(request,'Demo/uni.html', context)

def showOneUniversity(request,pk):
    uni = University.objects.get(ID=pk)
    uni_majors = UniMajor.objects.filter(UniID__ID=pk)
    comb_majors = CombMajor.objects.filter(Uni__ID=pk)
    context = {'uni': uni, 'uni_majors': uni_majors, 'comb_majors': comb_majors}
    return render(request,'Demo/uni.html', context)

def unimajor(request, uid, mid):
    uni_major = get_object_or_404(UniMajor, Q(UniID=uid) | Q(MajorID=mid))
    context = {'unimajor': unimajor}
    return render(request,'', context)

def listMajor(request):
    majors = UniMajor.objects.all()
    if request.method == 'GET' and request.GET.get('m') is not None:
        m = request.GET.get('m')
        majors = UniMajor.objects.filter(Q(MajorID__ID__icontains=m) |
                                    Q(MajorID__Name__icontains=m))
    context = {'majors': majors}
    return render(request,'Demo/major.html', context)

def showOneMajor(request, pk):
    major = Major.objects.get(ID=pk)
    uni_majors = UniMajor.objects.filter(Q(MajorID__FieldID__ID=pk) | Q(MajorID__ID=pk))
    comb_majors = CombMajor.objects.filter(Major__ID=pk, Major__FieldID__ID=pk)
    context = {'uni_majors': uni_majors, 'comb_majors': comb_majors, 'major': major}
    return render(request,'Demo/major.html' , context)

def filterRegion(request):
    major_id = request.GET.get('major_id', '')
    uni_id = request.GET.get('uni_id', '')
    region_id = request.GET.get('region', '')
    if (major_id != '' and uni_id != ''):
        uni_majors = getUniMajorByRegionAndMajorAndUniversity(region_id, major_id, uni_id)
        return render(request, 'Demo/major.html', {'uni_majors': uni_majors})
    elif major_id != '':
        majors = getUniMajorByRegionAndMajor(region_id, major_id)
        return render(request, 'Demo/major.html', {'majors': majors})
    else:
        unis = getUniMajorByRegionAndUniversity(region_id, uni_id)
        return render(request, 'Demo/uni.html', {'unis': unis})

def getUniMajorByRegionAndMajorAndUniversity(region_id, major_id, uni_id):
    checkExist = Campus.objects.filter(Region__ID=region_id, Uni__ID=uni_id).exists()
    if checkExist:
        uni_majors = UniMajor.objects.filter(UniID__ID=uni_id, MajorID__ID=major_id)
        return uni_majors
    else:
        return UniMajor.objects.none()
    
def getUniMajorByRegionAndMajor(region_id, major_id):
    campus = Campus.objects.filter(Region__ID=region_id)
    university_ids = campus.values_list('Uni__ID', flat=True)
    majors = UniMajor.objects.filter(UniID__ID__in=university_ids, MajorID__ID=major_id)
    return majors

def getUniMajorByRegionAndUniversity(region_id, uni_id):
    checkExist = Campus.objects.filter(Region__ID=region_id, Uni__ID=uni_id).exists()
    if checkExist:
        uni_majors = UniMajor.objects.filter(UniID__ID=uni_id)
        return uni_majors
    else:
        return UniMajor.objects.none()
    
def filterType(request):
    major_id = request.GET.get('major_id', '')
    uni_id = request.GET.get('uni_id', '')
    uni_type = request.GET.get('type', '')
    if (major_id != '' and uni_id != ''):
        uni_majors = getUniMajorByTypeAndMajorAndUniversity(uni_type, major_id, uni_id)
        return render(request, 'Demo/major.html', {'uni_majors': uni_majors})
    elif major_id != '':
        majors = getUniMajorByTypeAndMajor(uni_type, major_id)
        return render(request, 'Demo/major.html', {'majors': majors})
    else:
        unis = getUniMajorByTypeAndUniversity(uni_type, uni_id)
        return render(request, 'Demo/uni.html', {'unis': unis})
    
def getUniMajorByTypeAndMajorAndUniversity(type, major_id, uni_id):
    uni_majors = UniMajor.objects.filter(UniID__ID=uni_id, UniID__Type=type, MajorID=major_id)
    return uni_majors

def getUniMajorByTypeAndMajor(type, major_id):
    uni_majors = UniMajor.objects.filter(UniID__Type=type, MajorID=major_id)
    return uni_majors

def getUniMajorByTypeAndUniversity(type, uni_id):
    uni_majors = UniMajor.objects.filter(UniID__ID=uni_id, UniID__Type=type)
    return uni_majors
    