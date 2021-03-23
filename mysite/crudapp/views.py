from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import *

# Create your views here.

def home(request):
    context = {}
    context['data'] = Person.objects.all()
    return render(request, 'crud1.html', context)

def addEmployee(request):
    if request.method == "POST":
        emp_edit_name = request.POST.get('emp_edit_name')
        emp_delete_name = request.POST.get('emp_delete_name') 
        if emp_edit_name:
            #wirte edit logic here
            addemp = Person.objects.get(id=emp_edit_name)
            addemp.name = request.POST.get('name')
            addemp.email = request.POST.get('email')
            addemp.address = request.POST.get('address')
            addemp.phone = request.POST.get('phone')
            addemp.save()

                    
        elif emp_delete_name:
            Person.objects.get(id=emp_delete_name).delete()
            print('deleted')


        else:
            addemp = Person()
            addemp.name = request.POST.get('name')
            addemp.email = request.POST.get('email')
            addemp.address = request.POST.get('address')
            addemp.phone = request.POST.get('phone')
            addemp.save()
        
    context = {}
    context['data'] = Person.objects.all()
    return render(request, 'table1.html', context)
    

    # return JsonResponse({'data':request.POST})