from django.shortcuts import render,get_object_or_404
from admin_master.models import *
from django.http import JsonResponse
from admin_employee.models import *
from io import BytesIO
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile



def empl_mng(request):
    msg = ''
    if request.POST:
        empcat = request.POST['select_catarea'].strip()
        empcat_id = empcat.split("_")[0].strip()
        empcat_instance = get_object_or_404(masterempcat, id=empcat_id)
        emp_name = request.POST['select_name'].strip()
        empgender = request.POST['select_gen'].strip()
        empdob = request.POST['select_dob'].strip()
        empmob = request.POST['select_numb'].strip()
        empemail = request.POST['select_email'].strip()
        empads = request.POST['select_addrss'].strip()
        empqual_id = request.POST['select_qual'].strip()
        empqual_instance = get_object_or_404(masterqualif, id=empqual_id)
        empdes_id = request.POST['select_des'].strip()
        empdes_instance = get_object_or_404(masterdesig, id=empdes_id)
        empdep_id = request.POST['select_dep'].strip()
        empdep_instance = get_object_or_404(masterdpt, id=empdep_id)
        empsalary = request.POST['select_sal'].strip()
        emp_jdate = request.POST['select_jdate'].strip()
        emp_photo = request.FILES['select_photo']

        # Create Employee instance and save to the database
        employee_instance, created = EmployeeRegistration.objects.get_or_create(empcatid=empcat_instance,
            empname=emp_name,
            gender=empgender,
            dob=empdob,
            mob=empmob,
            email=empemail,
            address=empads,
            deptid=empdep_instance,
            desid=empdes_instance,
            qualid=empqual_instance,
            salary=empsalary,
            jdate=emp_jdate,
            photo=emp_photo)
        
        # insert employee dept table
        deptobj=Department_employee(deptid=empdep_instance,empid=employee_instance,fromdate=emp_jdate)
        deptobj.save()

        # insert employee designation table
        desobj=EmployeeDesignation(designationid=empdes_instance,empid=employee_instance,fromdate=emp_jdate)
        desobj.save()

        # insert employee salary table
        salaryobj=EmpSalary(empid=employee_instance,salary=empsalary,fromdate=emp_jdate)
        salaryobj.save()

        # insert employee scd table
        classlist=request.POST.getlist("selcls")
        divlist=request.POST.getlist("seldiv")
        sublist=request.POST.getlist("selsub")
        if classlist:
            for class_id,div_id,sub_id in zip(classlist,divlist,sublist):
                scdobj=sub_cls_div(empid=employee_instance,classid=get_object_or_404(masterclass, id=class_id),divid=get_object_or_404(masterdivision,id=div_id),subid=get_object_or_404(subject,id=sub_id))
                scdobj.save()
        



        msg = 'Employee details saved successfully.'

    qual = masterqualif.objects.filter(status=1).order_by("qualifname")
    des = masterdesig.objects.filter(status=1).order_by("designame")
    dep = masterdpt.objects.filter(status=1).order_by("dptname")
    empcat = masterempcat.objects.filter(status=1).order_by("empcatarea")
    cls = masterclass.objects.filter(status=1).order_by("classname")
    div = masterdivision.objects.filter(status=1).order_by("divisionname")


    data = {'qlist': qual, 'deslist': des, 'deplist': dep, 'catlist': empcat, 'clslist': cls, 'divlist': div, 'msg': msg}
    return render(request, 'emp_mng.html', data)

def empl_sub_list(request):
    
    return render(request, 'emp_mng.html')



def sub_listss(request):
    class_id = request.GET['classId']
    academic_class = get_object_or_404(masterclass, id=class_id, status=1)
    subjects = list(subject.objects.filter(classes=academic_class, status=1).values('id', 'sub_name'))
    print(subjects)
    response_data={"subjects":subjects}
    return JsonResponse(response_data)
