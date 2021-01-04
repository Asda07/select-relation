from django.shortcuts import render
from django.http import HttpResponse
from.models import Student
# Create your views here.

def select(request):
    st=Student.objects.all().select_related('dept','house')
    for s in st:
        print(s.name,s.dept,s.house,s.house.head)
    # return render(request,'index.html')

def prefetch(request):
    st=Student.objects.all().prefetch_related('contest_set')
    for s in st:
        print(s.name,s.contest_set.all())