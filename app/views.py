from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import *

def django_forms(request):
    formobject=Studentsform()
    d={'forms':formobject}

    if request.method=='POST':
        FD=Studentsform(request.POST)
        if FD.is_valid():
            n=FD.cleaned_data['name']
            a=FD.cleaned_data['age']
            e=FD.cleaned_data['email']
            ad=FD.cleaned_data['address']
            g=FD.cleaned_data['gender']
            c=FD.cleaned_data['course']
            d1={'n':n,'a':a,'e':e,'ad':ad,'g':g,'c':c}
            return render(request,'form_data.html',d1)
    return render(request,'student_form.html',d)