from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View,TemplateView
from app.forms import *
# Create your views here.

#class based view
class Data_render(View):
    def get(self,request):
        d={'name':'mahesh'}
        return render(request,'Data_render.html',d)
    

#fuction based view
def Student(request):
    SFO=StudentForm()
    d={'SFO':SFO}
    if request.method=='POST':
        SFD=StudentForm(request.POST)
        if SFD.is_valid():
            SFD.save()
            return HttpResponse('data is inserted')
    return render(request,'Student.html',d)


#class based view 
class Insert_student(View):
    def get(self,request):
        SFO=StudentForm()
        d={'SFO':SFO}
        return render(request,'Insert_student.html',d)
    def post(self,request):
        SFD=StudentForm(request.POST)
        if SFD.is_valid():
            SFD.save()
            return HttpResponse('DATA IS INSERTED')

class template(TemplateView):
    template_name='template.html'