from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from admin_master.models import masterdpt,masterdesig,masterclass,masterdivision,masterempcat,masterqualif

# Create your views here.


@csrf_exempt
def admin_master_dpt_mng(request):
    message=''
    if request.POST:
        amdptname=request.POST['dpt_name'].strip()
        amdptcode=request.POST['dpt_code'].strip()
        if not amdptname or not amdptcode:
            message = "Both Name and code are required."
        elif masterdpt.objects.filter(dptname=amdptname).exists():
            message = "Department name already exists."
        elif masterdpt.objects.filter(dptcode=amdptcode).exists():
            message = "Department code already exists."
        else:
            dept = masterdpt(dptname=amdptname, dptcode=amdptcode)
            dept.save()
            message = "Submitted successfully."
    departments = masterdpt.objects.all()
    return render(request, 'department_manage.html', {'mess': message, 'departments': departments})


@csrf_exempt
def admin_master_desig_mng(request):
    message=''
    if request.POST:
        desiname=request.POST['desig_name'].strip()
        desicode=request.POST['desig_code'].strip()
        if not desiname or not desicode:
            message = "Both Name and code are required."
        elif masterdesig.objects.filter(designame=desiname).exists():
            message = "Designation name already exists."
        elif masterdesig.objects.filter(desigcode=desicode).exists():
            message = "Designation code already exists."
        else:
            designation = masterdesig(designame=desiname, desigcode=desicode)
            designation.save()
            message = "Submitted successfully."
    designations = masterdesig.objects.all()
    return render(request, 'designation_manage.html', {'mess': message, 'designations': designations})



@csrf_exempt
def admin_master_qual_mng(request):
    message=''
    if request.POST:
        qualname=request.POST['qua_name'].strip()
        
        if not qualname:
            message = "Name is required."
        elif masterqualif.objects.filter(qualifname=qualname).exists():
            message = "Qualification name already exists."
        else:
            qualification = masterqualif(qualifname=qualname)
            qualification.save()
            message = "Submitted successfully."
    qualifications = masterqualif.objects.all()
    return render(request, 'qualification_manage.html', {'mess': message, 'qualifications': qualifications})

@csrf_exempt
def cls_mng(request):
    message=''
    if request.POST:
        name=request.POST['cls_name'].strip()
        
        if not name:
            message = "Name is required."
        elif masterclass.objects.filter(classname=name).exists():
            message = "Class name already exists."
        else:
            classes = masterclass(classname=name)
            classes.save()
            message = "Submitted successfully."
    cls = masterclass.objects.all()
    return render(request, 'Class_manage.html', {'mess': message, 'cls': cls})

@csrf_exempt
def division_mng(request):
    message=''
    if request.POST:
        name=request.POST['div_name'].strip()
        
        if not name:
            message = "Name is required."
        elif masterdivision.objects.filter(divisionname=name).exists():
            message = "Division name already exists."
        else:
            classes = masterdivision(divisionname=name)
            classes.save()
            message = "Submitted successfully."
    divisions = masterdivision.objects.all()
    return render(request, 'Division_manage.html', {'mess': message, 'divisions': divisions})

@csrf_exempt
def employee_category(request):
    message=''
    if request.POST:
        emp_name=request.POST['empl_ctgry'].strip()
        areas=request.POST['area'].strip()
        if not emp_name:
            message = "Category must be filled."
        elif not areas:
            message = "Area is required."
        else:
            if masterempcat.objects.filter(empcatname=emp_name).exists():
                message = "Name already exists."
            elif masterempcat.objects.filter(empcatarea=areas).exclude(empcatarea=settings.EMPL_CTGRY_OTHER).exists():
                message = "Area already exists."
            else:
                category = masterempcat(empcatname=emp_name, empcatarea=areas)
                category.save()
                message = "Submitted successfully."
    categories = masterempcat.objects.all()
    return render(request, 'employee_manage.html', {'mess': message, 'categories': categories, 'settings':settings})


def division_mng_edt(request):
    if request.GET:
        ids=request.GET['id']
        obj=masterdivision.objects.get(id=ids)
        res={
            'name':obj.divisionname,'status':obj.status
        }
        return JsonResponse(res)
    
def division_mng_updt(request):
    if request.GET:
        ids=request.GET['id']
        diviname=request.GET['diviname']
        divistatus=request.GET['divistatus']
        if not diviname:
            message = "This must be filled."
        else:
            if masterdivision.objects.filter(divisionname=diviname).exclude(id=ids).exists():
                message = "Name already exists."
            else:
                add = masterdivision.objects.get(id=ids)
                add.divisionname=diviname
                if divistatus.isdigit():
                    add.status = int(divistatus)
                else:
   
                    print("Invalid status:", divistatus)
    
                add.save()
                message = "Submitted successfully."
        respond={
            'message':message
        }
    return JsonResponse(respond)