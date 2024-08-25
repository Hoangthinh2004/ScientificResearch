from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpRequest
from .models import University, Major, FieldOfStudy, UniMajor
from django.db.models import Q

# Create your views here.
def home(request):
    unis = University.objects.all()
    majors = Major.objects.all()
    fieldOfMajors = {}
    for major in majors:
        fieldOfMajors |= {major.FieldID: major.FieldID.Name}
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
    uni = University.objects.all()
    if request.method == 'GET' and request.GET.get('u') is not None:
        u = request.GET.get('u')
        uni = University.objects.filter(Q(ID__icontains=u) |
                                    Q(Name__icontains=u))
    context = {'uni': uni}
    return render(request,'Demo/uni.html', context)

def showOneUniversity(request,pk):
    uni = get_list_or_404(UniMajor, Q(UniID=pk))
    context = {'uni': uni}
    return render(request,'Demo/uni.html', context)

def unimajor(request, uid, mid):
    uni_major = get_object_or_404(UniMajor, Q(UniID=uid) | Q(MajorID=mid))
    context = {'unimajor': unimajor}
    return render(request,'', context)

def listMajor(request):
    major = Major.objects.all()
    if request.method == 'GET' and request.GET.get('m') is not None:
        m = request.GET.get('m')
        major = Major.objects.filter(Q(ID__icontains=m) |
                                    Q(Name__icontains=m))
    context = {'majors': major}
    return render(request,'Demo/major.html', context)

def showOneMajor(request, pk):
    major = get_list_or_404(UniMajor, Q(MajorID_FieldID=pk) | Q(MajorID=pk))
    context = {'majors': major}
    return render(request,'Demo/major.html' , context)