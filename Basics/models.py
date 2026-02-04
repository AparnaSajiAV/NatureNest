from django.db import models

# Create your models here.

#Department
class tbl_dept(models.Model):
    dept_name=models.CharField(max_length=50)

#Designation
class tbl_desi(models.Model):
    desi_name=models.CharField(max_length=50)

#Employee
class tbl_emp(models.Model):
    emp_name=models.CharField(max_length=50)
    emp_contact=models.CharField(max_length=50)
    emp_email=models.CharField(max_length=50)
    emp_basal=models.CharField(max_length=50)
    dept=models.ForeignKey(tbl_dept,on_delete=models.CASCADE)
    desi=models.ForeignKey(tbl_desi,on_delete=models.CASCADE)

#Course
class tbl_course(models.Model):
    course_name=models.CharField(max_length=50)
    course_duration=models.CharField(max_length=50)
    course_semno=models.CharField(max_length=50)
    dept=models.ForeignKey(tbl_dept,on_delete=models.CASCADE)

#Subject
class tbl_subject(models.Model):
    subject_name=models.CharField(max_length=50)

#Semester
class tbl_semester(models.Model):
    semester_no=models.CharField(max_length=50)

#Syllabus
class tbl_syllabus(models.Model):
    course=models.ForeignKey(tbl_course,on_delete=models.CASCADE)
    subject=models.ForeignKey(tbl_subject,on_delete=models.CASCADE)
    semester=models.ForeignKey(tbl_semester,on_delete=models.CASCADE)
