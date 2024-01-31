from django.shortcuts import render,get_object_or_404,redirect
from admin_master.models import *
from django.http import JsonResponse
from admin_employee.models import *
from io import BytesIO
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
import qrcode
import json
from django.views.decorators.csrf import csrf_exempt



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
        
        deptname=masterdpt.objects.get(id=empdep_id)
        qr_data = f"Name: {emp_name} \nDOB: {empdob}\nDepartment: {deptname.dptname}\nJoin Date: {emp_jdate}"

        # Generate QR code image
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(qr_data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        # Save the QR code image to a BytesIO object
        qr_image_io = BytesIO()
        img.save(qr_image_io, format='PNG')
        qr_image_io.seek(0)

        # Create an InMemoryUploadedFile from BytesIO
        qr_image = InMemoryUploadedFile(
            file=qr_image_io,
            field_name=None,
            name=f'qr_code_{emp_name}.png',
            content_type='image/png',
            size=qr_image_io.tell(),
            charset=None,
        )
        

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
            photo=emp_photo,
            barcode=qr_image)
        
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
        classlist = request.POST.getlist("selcls")
        divlist = request.POST.getlist("seldiv")
        sublist = request.POST.getlist("selsub")
        
        for class_id, div_id, sub_id in zip(classlist, divlist, sublist):
            if class_id and div_id and sub_id:
                scdobj = sub_cls_div(empid=employee_instance, classid=get_object_or_404(masterclass, id=class_id),
                                 divid=get_object_or_404(masterdivision, id=div_id),
                                 subid=get_object_or_404(subject, id=sub_id))
                scdobj.save()
        



        msg = 'Employee details saved successfully.'

    qual = masterqualif.objects.filter(status=1).order_by("qualifname")
    des = masterdesig.objects.filter(status=1).order_by("designame")
    dep = masterdpt.objects.filter(status=1).order_by("dptname")
    empcat = masterempcat.objects.filter(status=1).order_by("empcatarea")
    cls = masterclass.objects.filter(status=1).order_by("classname")
    div = masterdivision.objects.filter(status=1).order_by("divisionname")


    data = {'qlist': qual,
            'deslist': des,
            'deplist': dep,
            'catlist': empcat,
            'clslist': cls,
            'divlist': div,
            'msg': msg}
    return render(request, 'emp_mng.html', data)

def empl_sub_list(request):
    
    return render(request, 'emp_mng.html')


def sub_listss(request):
    class_id = request.GET.get('classId')
    academic_class = get_object_or_404(masterclass, id=class_id, status=1)
    subjects = list(subject.objects.filter(classes=academic_class, status=1).values('id', 'sub_name'))
    for subj in subjects:
        if not subj['id']:
            subj['id'] = 0 
    response_data = {"subjects": subjects}
    return JsonResponse(response_data)



def get_employee_details(request):
    employee_data=EmployeeRegistration.objects.all()
    return render(request,'Employee_Details.html',{'employee_data':employee_data})

@csrf_exempt
def fetch_employee(request,item_id):
    if request.POST:
        var_name=request.POST['edit_name']
        var_dob=request.POST['edit_dob']
        var_gender=request.POST['edit_gen']
        var_mobile=request.POST['edit_numb']
        var_email=request.POST['edit_email']
        var_address=request.POST['edit_addrss']
        var_qualification=request.POST['edit_qual']
        var_joiningdate=request.POST['edit_jdate']
        var_status=request.POST['edit_status']
        obj=EmployeeRegistration.objects.get(id=item_id)
        obj.empname=var_name
        obj.dob=var_dob
        obj.gender=var_gender
        obj.mob=var_mobile
        obj.email=var_email
        obj.address=var_address
        obj.qualid.qualifname=var_qualification
        obj.jdate=var_joiningdate
        obj.status=var_status
        if 'edit_photo' in  request.FILES:
            objphoto=request.FILES['edit_photo']
            obj.photo=objphoto
        obj.save()
        return redirect('get_employee_details')
    objjjj=EmployeeRegistration.objects.get(id=item_id)
    cat=EmployeeRegistration.objects.filter(id=item_id).select_related('empcatid')
    objj=masterqualif.objects.all()
    cladiv=list(sub_cls_div.objects.filter(empid=item_id).prefetch_related('classid','divid','subid'))
    return JsonResponse({'list':cladiv})
    cla=masterclass.objects.filter(status=1).order_by("classname")  
    divi=masterdivision.objects.filter(status=1).order_by("divisionname")
    sub=subject.objects.filter(status=1).order_by("sub_name")
    return render(request,'Employee_edit.html',{'data':objjjj,
                                                'list':objj,
                                                'cla':cla,
                                                "divi":divi,
                                                "sub":sub,
                                                'cladiv':cladiv,
                                                'datta':cat})


def delete_empl(request):
    if request.GET:
        ids=request.GET['id']
        obj=EmployeeRegistration.objects.get(id=ids)
        obj.delete()
        return JsonResponse()
    

