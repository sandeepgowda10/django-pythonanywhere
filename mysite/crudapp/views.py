from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def home(request):
    context = {}
    context['data'] = Person.objects.all()
    return render(request, 'crud1.html', context)

@csrf_exempt
def addEmployee(request):
    context = {}
    context['data'] = Person.objects.all()

    if request.method == "POST":
        emp_edit_name = request.POST.get('emp_edit_name')
        emp_delete_name = request.POST.get('emp_delete_name') 
        if emp_edit_name:
            editemp_addr = Address.objects.get(id=request.POST.get('address_edit_name'))
            editemp_addr.address = request.POST.get('address')
            editemp_addr.save()

            editemp_contact = Contact.objects.get(id=request.POST.get('phone_edit_name'))
            editemp_contact.phone = request.POST.get('phone')
            if request.POST.get('emergency_contact_edit'):
                editemp_contact.emergency_contact = request.POST.get('emergency_contact_edit')
            else:
                editemp_contact.emergency_contact = None

            editemp_contact.save()


            addemp = Person.objects.get(id=emp_edit_name)
            addemp.name = request.POST.get('name')
            addemp.email = request.POST.get('email')
            addemp.address = editemp_addr
            addemp.phone = editemp_contact
            addemp.save()

                    
        elif emp_delete_name:
            Person.objects.get(id=emp_delete_name).delete()
            print('deleted')


        else:
            emp_address = Address.objects.create(address=request.POST.get('address'))
            emp_phone_no = Contact()
            emp_phone_no.phone = request.POST.get('phone')
            if request.POST.get('emergency_contact_add'):
                emp_phone_no.emergency_contact = request.POST.get('emergency_contact_add')
            emp_phone_no.save()

            addemp = Person()
            addemp.name = request.POST.get('name')
            addemp.email = request.POST.get('email')
            addemp.address = emp_address
            addemp.phone = emp_phone_no
            addemp.save()
        
    
    return render(request, 'table1.html', context)
    

    # return JsonResponse({'data':request.POST})