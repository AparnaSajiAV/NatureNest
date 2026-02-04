from django.contrib import admin
from django.urls import path,include
from Basics import views

app_name="WebBasics"
urlpatterns = [
    path('admin/', admin.site.urls),

    path('Calculator/',views.calculation,name="calculation"),
    path('LargestSmallest/',views.largestsmallest,name="largestsmallest"),
    path('Marklist/',views.marklist,name="marklist"),
    path('SalarySlip/',views.salaryslip,name="salaryslip"),

    #Department
    path('Department/',views.deptInsertSelect,name="deptInsertSelect"),
    path('DepartmentDelete/<int:did>',views.deptDelete,name="deptDelete"),
    path('DepartmentUpdate/<int:eid>',views.deptUpdate,name="deptUpdate"),

    #Designation
    path('Designation/',views.desiInsertSelect,name="desiInsertSelect"),
    path('DesignationDelete/<int:did>',views.desiDelete,name="desiDelete"),
    path('Designation/<int:eid>',views.desiUpdate,name="desiUpdate"),

    #Employee
    path('Employee/',views.empInsertSelect,name="empInsertSelect"),
    path('EmployeeDelete/<int:did>',views.empDelete,name="empDelete"),
    path('EmployeeUpdate/<int:eid>',views.empUpdate,name="empUpdate"),

    #Course
    path('Course/',views.courseInsertSelect,name="courseInsertSelect"),
    path('CourseDelete/<int:did>',views.courseDelete,name="courseDelete"),
    path('CourseUpdate/<int:eid>',views.courseUpdate,name="courseUpdate"),

    #Subject
    path('Subject/',views.subjectInsertSelect,name="subjectInsertSelect"),
    path('SubjectDelete/<int:did>',views.subjectDelete,name="subjectDelete"),
    path('SubjectUpdate/<int:eid>',views.subjectUpdate,name="subjectUpdate"),

    #Semester
    path('Semester/',views.semesterInsertSelect,name="semesterInsertSelect"),
    path('SemesterDelete/<int:did>',views.semesterDelete,name="semesterDelete"),
    path('SemesterUpdate/<int:eid>',views.semesterUpdate,name="semesterUpdate"),

    #Syllabus
    path('Syllabus/',views.syllabusInsertSelect,name="syllabusInsertSelect"),
    path('SyllabusDelete/<int:did>',views.syllabusDelete,name="syllabusDelete"),
    path('SyllabusUpdate/<int:eid>',views.syllabusUpdate,name="syllabusUpdate"),
]