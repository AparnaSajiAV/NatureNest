from django.shortcuts import render,redirect
from Basics.models import *

# Create your views here.

#calculator
def calculation(request):
    result=""
    if request.method=="POST":
        no1=int(request.POST.get("txtnumone"))
        no2=int(request.POST.get("txtnumtwo"))
        btn=request.POST.get("btnsubmit")
        if btn=="+":
            result=no1+no2
        elif btn=="-":
            result=no1-no2
        elif btn=="*":
            result=no1*no2
        elif btn=="/":
            result=no1/no2
        return render(request,"Basics/Calculator.html",{'res':result})
    else:
        return render(request,"Basics/Calculator.html",{'res':result})
        
#largestsmallest
def largestsmallest(request):
    l=""
    s=""
    if request.method=="POST":
        no1=int(request.POST.get("txtnumone"))
        no2=int(request.POST.get("txtnumtwo"))
        no3=int(request.POST.get("txtnumthree"))
        l=no1
        if l<no2:
            l=no2
        elif l<no3:
            l=no3
        s=no1
        if s>no2:
            s=no2
        elif s>no3:
            s=no3
        return render(request,"Basics/LargestSmallest.html",{'res1':l,'res2':s})
    else:
        return render(request,"Basics/LargestSmallest.html",{'res1':l,'res2':s})

#marklist
def marklist(request):
    name=""
    gender=""
    dept=""
    m1=""
    m2=""
    m3=""
    total=""
    percent=""
    grade=""
    if request.method=="POST":
        fname=request.POST.get("txtfirstname")
        lname=request.POST.get("txtlastname")
        gender=request.POST.get("rdogender")
        dept=request.POST.get("ddndept")
        m1=int(request.POST.get("txtm1"))
        m2=int(request.POST.get("txtm2"))
        m3=int(request.POST.get("txtm3"))
        total=m1+m2+m3
        percent=total/3
        name=fname+' '+lname
        if(percent>=90):
            grade="A"
        elif(percent>=80):
            grade="B"
        elif(percent>=70):
            grade="C"
        elif(percent>=60):
            grade="D"
        else:
            grade="E"
        return render(request,"Basics/Marklist.html",{'name':name,'gender':gender,'dept':dept,'m1':m1,'m2':m2,'m3':m3,'res1':total,'res2':percent,'res3':grade})
    else:
        return render(request,"Basics/Marklist.html",{'name':name,'gender':gender,'dept':dept,'m1':m1,'m2':m2,'m3':m3,'res1':total,'res2':percent,'res3':grade})

#salaryslip
def salaryslip(request):
    name=""
    gender=""
    dept=""
    #dob=""
    #doj=""
    bs=""
    ta=""
    da=""
    hra=""
    lic=""
    pf=""
    netsal=""
    if request.method=="POST":
        fname=request.POST.get("txtfirstname")
        lname=request.POST.get("txtlastname")
        name=fname+' '+lname
        gender=request.POST.get("rdogender")
        dept=request.POST.get("ddndept")
        #dob=request.POST.get("txtdob")
        #doj=request.POST.get("txtdoj")
        bs=int(request.POST.get("txtbs"))
        if bs>=25000:
            ta=bs*40/100
            da=bs*35/100
            hra=bs*30/100
            lic=bs*25/100
            pf=bs*20/100
        elif bs>=15000:
            ta=bs*35/100
            da=bs*30/100
            hra=bs*25/100
            lic=bs*20/100
            pf=bs*15/100
        else:
            ta=bs*30/100
            da=bs*25/100
            hra=bs*20/100
            lic=bs*15/100 
            pf=bs*10/100
        netsal=bs+ta+da+hra-pf-lic
        return render(request,'Basics/SalaryCalculation.html',{'name':name,'gender':gender,'dept':dept,'ta':ta,'da':da,'hra':hra,'lic':lic,'pf':pf,'netsal':netsal})
    else:
        return render(request,'Basics/SalaryCalculation.html',{'name':name,'gender':gender,'dept':dept,'ta':ta,'da':da,'hra':hra,'lic':lic,'pf':pf,'netsal':netsal})

#Department
def deptInsertSelect(request):
    data=tbl_dept.objects.all()
    if request.method=="POST":
        deptName=request.POST.get("txtdept")
        tbl_dept.objects.create(dept_name=deptName)
        return render(request,"Basics/Department.html",{"data":data})
    else:
        return render(request,"Basics/Department.html",{"data":data})
    
def deptDelete(request,did):
    tbl_dept.objects.get(id=did).delete()
    return redirect("WebBasics:deptInsertSelect")

def deptUpdate(request,eid):
    editdata=tbl_dept.objects.get(id=eid)
    if request.method=="POST":
        editdata.dept_name=request.POST.get("txtdept")
        editdata.save()
        return redirect("WebBasics:deptInsertSelect")
    else:
        return render(request,"Basics/Department.html",{"editdata":editdata})

#Designation
def desiInsertSelect(request):
    data=tbl_desi.objects.all()
    if request.method=="POST":
        desiName=request.POST.get("txtdesi")
        tbl_desi.objects.create(desi_name=desiName)
        return render(request,"Basics/Designation.html",{"data":data})
    else:
        return render(request,"Basics/Designation.html",{"data":data})

def desiDelete(request,did):
    tbl_desi.objects.get(id=did).delete()
    return redirect("WebBasics:desiInsertSelect")

def desiUpdate(request,eid):
    editdata=tbl_desi.objects.get(id=eid)
    if request.method=="POST":
        editdata.desi_name=request.POST.get("txtdesi")
        editdata.save()
        return redirect("WebBasics:desiInsertSelect")
    else:
        return render(request,"Basics/Designation.html",{"editdata":editdata})

#Employee
def empInsertSelect(request):
    data=tbl_emp.objects.all()
    dept=tbl_dept.objects.all()
    desi=tbl_desi.objects.all()
    if request.method=="POST":
        empName=request.POST.get("txtname")
        empContact=request.POST.get("txtcont")
        empEmail=request.POST.get("txtemail")
        empBasal=request.POST.get("txtbs")
        depnt = tbl_dept.objects.get(id=request.POST.get('sel_dept'))
        desin = tbl_desi.objects.get(id=request.POST.get('sel_desi'))
        tbl_emp.objects.create(emp_name=empName,emp_contact=empContact,emp_email=empEmail,dept=depnt,desi=desin,emp_basal=empBasal)
        return render(request,"Basics/Employee.html",{"data":data})
    else:
        return render(request,"Basics/Employee.html",{"data":data,"desidata":desi,"deptdata":dept})

def empDelete(request,did):
    tbl_emp.objects.get(id=did).delete()
    return redirect("WebBasics:empInsertSelect")

def empUpdate(request,eid):
    dept=tbl_dept.objects.all()
    desi=tbl_desi.objects.all()
    editdata=tbl_emp.objects.get(id=eid)
    if request.method=="POST":
        editdata.emp_name=request.POST.get("txtname")
        editdata.emp_contact=request.POST.get("txtcont")
        editdata.emp_email=request.POST.get("txtemail")
        editdata.emp_basal=empBasal=request.POST.get("txtbs")
        depnt = tbl_dept.objects.get(id=request.POST.get('sel_dept'))
        desin = tbl_desi.objects.get(id=request.POST.get('sel_desi'))
        editdata.dept=depnt
        editdata.desi=desin
        editdata.save()
        return redirect("WebBasics:empInsertSelect")
    else:
        return render(request,"Basics/Employee.html",{"editdata":editdata,"desidata":desi,"deptdata":dept})

#Course
def courseInsertSelect(request):
    dept=tbl_dept.objects.all()
    data=tbl_course.objects.all()
    if request.method=="POST":
        courseName=request.POST.get("txtcourse")
        courseDue=request.POST.get("txtdue")
        courseSemno=request.POST.get("txtsemno")
        depnt = tbl_dept.objects.get(id=request.POST.get('sel_dept'))
        tbl_course.objects.create(course_name=courseName,course_duration=courseDue,course_semno=courseSemno,dept=depnt)
        return render(request,"Basics/Course.html",{"data":data})
    else:
        return render(request,"Basics/Course.html",{"data":data,"deptdata":dept})

def courseDelete(request,did):
    tbl_course.objects.get(id=did).delete()
    return redirect("WebBasics:courseInsertSelect")

def courseUpdate(request,eid):
    dept=tbl_dept.objects.all()
    editdata=tbl_course.objects.get(id=eid)
    if request.method=="POST":
        editdata.course_name=request.POST.get("txtcourse")
        editdata.course_duration=request.POST.get("txtdue")
        editdata.course_semno=request.POST.get("txtsemno")
        depnt = tbl_dept.objects.get(id=request.POST.get('sel_dept'))
        editdata.dept=depnt
        editdata.save()
        return redirect("WebBasics:courseInsertSelect")
    else:
        return render(request,"Basics/Course.html",{"editdata":editdata,"deptdata":dept})

#Subject
def subjectInsertSelect(request):
    data=tbl_subject.objects.all()
    if request.method=="POST":
        subjectName=request.POST.get("txtsubject")
        tbl_subject.objects.create(subject_name=subjectName)
        return render(request,"Basics/Subject.html",{"data":data})
    else:
        return render(request,"Basics/Subject.html",{"data":data})

def subjectDelete(request,did):
    tbl_subject.objects.get(id=did).delete()
    return redirect("WebBasics:subjectInsertSelect")

def subjectUpdate(request,eid):
    editdata=tbl_subject.objects.get(id=eid)
    if request.method=="POST":
        editdata.subject_name=request.POST.get("txtsubject")
        editdata.save()
        return redirect("WebBasics:subjectInsertSelect")
    else:
        return render(request,"Basics/Subject.html",{"editdata":editdata})

#Semester
def semesterInsertSelect(request):
    data=tbl_semester.objects.all()
    if request.method=="POST":
        semesterNo=request.POST.get("txtsemno")
        tbl_semester.objects.create(semester_no=semesterNo)
        return render(request,"Basics/Semester.html",{"data":data})
    else:
        return render(request,"Basics/Semester.html",{"data":data})

def semesterDelete(request,did):
    tbl_semester.objects.get(id=did).delete()
    return redirect("WebBasics:semesterInsertSelect")

def semesterUpdate(request,eid):
    editdata=tbl_semester.objects.get(id=eid)
    if request.method=="POST":
        editdata.semester_no=request.POST.get("txtsemno")
        editdata.save()
        return redirect("WebBasics:semesterInsertSelect")
    else:
        return render(request,"Basics/Semester.html",{"editdata":editdata})

#Syllabus
def syllabusInsertSelect(request):
    data=tbl_syllabus.objects.all()
    course=tbl_course.objects.all()
    subject=tbl_subject.objects.all()
    semester=tbl_semester.objects.all()
    if request.method=="POST":
        courseName=tbl_course.objects.get(id=request.POST.get('sel_course'))
        subjectName=tbl_subject.objects.get(id=request.POST.get('sel_subject'))
        semesterNo=tbl_semester.objects.get(id=request.POST.get('sel_semester'))
        tbl_syllabus.objects.create(semester=semesterNo,course=courseName,subject=subjectName)
        return render(request,"Basics/Syllabus.html",{"data":data})
    else:
        return render(request,"Basics/Syllabus.html",{"data":data,"coursedata":course,"subjectdata":subject,"semesterdata":semester})

def syllabusDelete(request,did):
    tbl_syllabus.objects.get(id=did).delete()
    return redirect("WebBasics:syllabusInsertSelect")

def syllabusUpdate(request,eid):
    editdata=tbl_syllabus.objects.get(id=eid)
    course=tbl_course.objects.all()
    subject=tbl_subject.objects.all()
    semester=tbl_semester.objects.all()
    if request.method=="POST":
        courseName = tbl_course.objects.get(id=request.POST.get('sel_course'))
        editdata.course = courseName
        subjectName= tbl_subject.objects.get(id=request.POST.get('sel_subject'))
        editdata.subject = subjectName
        semesterNo= tbl_semester.objects.get(id=request.POST.get('sel_semester'))
        editdata.semester =semesterNo
        editdata.save()
        return redirect("WebBasics:syllabusInsertSelect")
    else:
        return render(request,"Basics/Syllabus.html",{"editdata":editdata,"coursedata":course,"subjectdata":subject,"semesterdata":semester})