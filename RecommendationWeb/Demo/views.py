from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpRequest
from .models import University, Major, FieldOfStudy, UniMajor, Region, Campus, CombMajor
from django.db.models import Q
from django.urls import reverse
import re

# Create your views here.
def home(request):
    url = 'filter'
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
                                    Q(Name__icontains=s))
    context = {'unis': unis, 'majors': majors, 'fieldOfMajors': fieldOfMajors, 'url': reverse(url)}
    return render(request, 'Demo/home.html', context)

def listUniversity(request):
    url = 'filter-university'
    unis = University.objects.all()
    if request.method == 'GET' and request.GET.get('u') is not None:
        u = request.GET.get('u')
        unis = University.objects.filter(Q(ID__icontains=u) |
                                    Q(Name__icontains=u))
    context = {'unis': unis, 'url': reverse(url)}
    return render(request,'Demo/uni.html', context)

def showOneUniversity(request,pk):
    url = 'filter-one-university'
    uni = University.objects.get(ID=pk)
    uni_majors = UniMajor.objects.filter(Q(UniID__ID=pk))
    comb_majors = CombMajor.objects.filter(Q(Uni__ID=pk))
    context = {'uni': uni, 'uni_majors': uni_majors, 'comb_majors': comb_majors, 'url': reverse(url,  args=[pk])}
    return render(request,'Demo/uni.html', context)

def unimajor(request, uid, mid):
    uni_major = get_object_or_404(UniMajor, Q(UniID=uid) | Q(MajorID=mid))
    context = {'unimajor': unimajor, 'url': reverse(url)}
    return render(request,'', context)

def listMajor(request):
    url = 'filter-major'
    print("filter function called")
    majors = Major.objects.all()
    if request.method == 'GET' and request.GET.get('m') is not None:
        m = request.GET.get('m')
        majors = Major.objects.filter(Q(ID=m) | Q(FieldID__ID=m))
    context = {'majors': majors, 'url': reverse(url)}
    return render(request,'Demo/major.html', context)

def showOneMajor(request, pk):
    url = 'filter-one-major'
    major = Major.objects.get(ID=pk)
    uni_majors = UniMajor.objects.filter(Q(MajorID__FieldID__ID=pk) | Q(MajorID__ID=pk))
    comb_majors = CombMajor.objects.filter(Q(Major__FieldID__ID=pk) | Q(Major__ID=pk))
    context = {'uni_majors': uni_majors, 'comb_majors': comb_majors, 'major': major, 'url': reverse(url, args=[pk])}
    return render(request,'Demo/major.html' , context)

def filter(request):
    unis = University.objects.all()
    majors = Major.objects.all()
    uni_majors = UniMajor.objects.all()

    #Filtering by region
    selected_regions = request.GET.getlist('region')
    if selected_regions:
        campuses = Campus.objects.filter(Region__ID__in=selected_regions).values_list('Uni', flat=True)
        unis = unis.filter(ID__in=campuses)
    #Filtering by type
    selected_types = request.GET.getlist('type')
    if selected_types:
        unis = unis.filter(Type__in=selected_types)
    #Filtering by fee
    selected_fees = request.GET.getlist('fee')
    if selected_fees:
        fees = [tuple(map(float, fee.split('-'))) for fee in selected_fees]
        queries = [Q(Max_Tuition_Fee__gt=fee[0], Min_Tuition_Fee__lte=fee[1]) for fee in fees]
        query = queries.pop()
        for q in queries:
            query |= q
        unis = unis.filter(query)
    #Filtering by score
    selected_scores = request.GET.getlist('score')
    if selected_scores:
        scores = [tuple(map(float, score.split('-'))) for score in selected_scores]
        queries = [Q(Min_Score__gt=score[0], Max_Score__lte=score[1]) for score in scores]    
        query = queries.pop()
        for q in queries:
            query |= q
        unis = unis.filter(query)
        
    uni_majors = uni_majors.filter(UniID__in=unis)
    majors = majors.filter(ID__in=uni_majors.values_list('MajorID', flat=True))
    query_params = request.GET.copy().urlencode()
    
    # Reconstruct query parameters for the URL
    

    # Determine the referring page and redirect back to it
    if 'university' in request.path:
         url = 'Demo/uni.html'
         uni_majors = None
    elif 'major' in request.path:
        url = 'Demo/major.html'  
    else:
        url = 'Demo/home.html'
    context = {'unis': unis, 
               'uni_majors': uni_majors, 
               'majors': majors, 
               'query_params': query_params}
    return render(request, url, context)



def filterInOneMajor(request, pk):
    major = Major.objects.get(ID=pk)
    uni_majors = UniMajor.objects.filter(MajorID__ID=pk)
    comb_majors = CombMajor.objects.filter(Major__ID=pk)
    selected_regions = request.GET.getlist('region')
    if selected_regions:
        campus = Campus.objects.filter(Region__ID__in=selected_regions)
        uni_ids = campus.values_list('Uni', flat=True)
        uni_majors = uni_majors.filter(UniID__ID__in=uni_ids)
    selected_types = request.GET.getlist('type')
    if selected_types:
        uni = University.objects.filter(Type__in=selected_types)
        uni_majors = uni_majors.filter(UniID__in=uni)
    selected_fees = request.GET.getlist('fee')
    if selected_fees:
        fees = [tuple(map(float, fee.split('-'))) for fee in selected_fees]
        queries = [Q(Tuition_Fee__gte=fee[0], Tuition_Fee__lte=fee[1]) for fee in fees]
        query = queries.pop()
        for q in queries:
            query |= q
        uni_majors = uni_majors.filter(query)
    selected_scores = request.GET.getlist('score')
    if selected_scores:
        scores = [tuple(map(float, score.split('-'))) for score in selected_scores]
        queries = [Q(Score__gte=score[0], Score__lte=score[1]) for score in scores]    
        query = queries.pop()
        for q in queries:
            query |= q
        comb_majors = comb_majors.filter(query)
        uni_ids = comb_majors.values_list('Uni', flat=True).distinct()
        uni_majors = uni_majors.filter(UniID__in=uni_ids)
    context ={'major': major,
              'uni_majors': uni_majors,
              'comb_majors': comb_majors}
    return render(request, 'Demo/major.html', context)


def filterInOneUniversity(request, pk):
    uni = University.objects.get(ID=pk)
    uni_majors = UniMajor.objects.filter(UniID__ID=pk)
    comb_majors = CombMajor.objects.filter(Uni__ID=pk)
    selected_regions = request.GET.getlist('region')
    if selected_regions:
        campus = Campus.objects.filter(Region__ID__in=selected_regions)
        uni_ids = campus.values_list('Uni', flat=True)
        uni_majors = uni_majors.filter(UniID__ID__in=uni_ids)
    selected_types = request.GET.getlist('type')
    if selected_types:
        uni = University.objects.filter(Type__in=selected_types)
        uni_majors = uni_majors.filter(UniID__in=uni)
    selected_fees = request.GET.getlist('fee')
    if selected_fees:
        fees = [tuple(map(float, fee.split('-'))) for fee in selected_fees]
        queries = [Q(Tuition_Fee__gte=fee[0], Tuition_Fee__lte=fee[1]) for fee in fees]
        query = queries.pop()
        for q in queries:
            query |= q
        uni_majors = uni_majors.filter(query)
    selected_scores = request.GET.getlist('score')
    if selected_scores:
        scores = [tuple(map(float, score.split('-'))) for score in selected_scores]
        queries = [Q(Score__gte=score[0], Score__lte=score[1]) for score in scores]    
        query = queries.pop()
        for q in queries:
            query |= q
        comb_majors = comb_majors.filter(query)
        uni_ids = comb_majors.values_list('Uni', flat=True).distinct()
        uni_majors = uni_majors.filter(UniID__in=uni_ids)
    context ={'uni': uni,
              'uni_majors': uni_majors,
              'comb_majors': comb_majors}
    return render(request, 'Demo/major.html', context)
