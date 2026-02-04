from django.contrib import admin
from django.urls import path,include
from Admin import views

app_name="WebAdmin"
urlpatterns = [
    path('admin/', admin.site.urls),

    #Homepage
    path('HomePage/',views.homepageLoarding,name="homepageLoarding"),

    #Profile
    path('MyProfile/',views.myprofile,name="myprofile"),
    
    #edit profile
    path('EditProfile/',views.editprofile,name="editprofile"),

    #change password
    path('ChangePassword/',views.changepassword,name="changepassword"),

    #userlist
    path('UserList/',views.userlist,name="userlist"),

    #Admin Reg
    path('AdminReg/',views.adminInsert,name="adminInsert"),
    path('AdminRegList/',views.adminSelect,name="adminSelect"),
    path('AdminDelete/<int:did>',views.adminDelete,name="adminDelete"),
    path('AdminUpdate/<int:eid>',views.adminUpdate,name="adminUpdate"),

    #Nursery Staff
    path('NurseryStaffReg/',views.nurserystaffInsert,name="nurserystaffInsert"),
    path('NurseryStaffList/',views.nurserystaffSelect,name="nurserystaffSelect"),
    path('NurseryStaffDelete/<int:did>',views.nurserystaffDelete,name="nurserystaffDelete"),
    path('NurseryStaffUpdate/<int:eid>',views.nurserystaffUpdate,name="nurserystaffUpdate"),

    #Delivery Staff
    path('DeliveryStaffReg/',views.deliverystaffInsert,name="deliverystaffInsert"),
    path('DeliveryStaffList/',views.deliverystaffSelect,name="deliverystaffSelect"),
    path('DeliveryStaffDelete/<int:did>',views.deliverystaffDelete,name="deliverystaffDelete"),
    path('DeliveryStaffUpdate/<int:eid>',views.deliverystaffUpdate,name="deliverystaffUpdate"),

    #District
    path('District/',views.districtInsertSelect,name="districtInsertSelect"),
    path('DistrictDelete/<int:did>', views.districtDelete,name="districtDelete"),
    path('DistrictUpdate/<int:eid>',views.districtUpdate,name="districtUpdate"),

    #Place
    path('Place/', views.placeInsertSelect,name="placeInsertSelect"),
    path('PlaceDelete/<int:did>', views.placeDelete,name="placeDelete"),
    path('PlaceUpdate/<int:eid>',views.placeUpdate,name="placeUpdate"),

    #category(plant)
    path('Category/',views.categoryInsertSelect,name="categoryInsertSelect"),
    path('CategoryDelete/<int:did>',views.categoryDelete,name="categoryDelete"),
    path('CategoryUpdate/<int:eid>',views.categoryUpdate,name="categoryUpdate"),

    #subcategory
    path('Subategory/',views.subcategoryInsertSelect,name="subcategoryInsertSelect"),
    path('SubcategoryDelete/<int:did>',views.subcategoryDelete,name="subcategoryDelete"),
    path('SubcategoryUpdate/<int:eid>',views.subcategoryUpdate,name="subcategoryUpdate"),

    #pot type
    path('TypePot/',views.typepotInsertSelect,name="typepotInsertSelect"),
    path('TypePotDelete/<int:did>',views.typepotDelete,name="typepotDelete"),
    path('TypePotUpdate/<int:eid>',views.typepotUpdate,name="typepotUpdate"),

    #pot shape
    path('ShapePot/',views.shapepotInsertSelect,name="shapepotInsertSelect"),
    path('ShapePotDelete/<int:did>',views.shapepotDelete,name="shapepotDelete"),
    path('ShapePotUpdate/<int:eid>',views.shapepotUpdate,name="shapepotUpdate"),

    #pot color
    path('ColorPot/',views.colorpotInsertSelect,name="colorpotInsertSelect"),
    path('ColorPotDelete/<int:did>',views.colorpotDelete,name="colorpotDelete"),
    path('ColorPotUpdate/<int:eid>',views.colorpotUpdate,name="colorpotUpdate"),

    #pot material
    path('MaterialPot/',views.materialpotInsertSelect,name="materialpotInsertSelect"),
    path('MaterialPotDelete/<int:did>',views.materialpotDelete,name="materialpotDelete"),
    path('MaterialUpdate/<int:eid>',views.materialpotUpdate,name="materialpotUpdate"),

    #pot size
    path('SizePot/',views.sizepotInsertSelect,name="sizepotInsertSelect"),
    path('SizePotDelete/<int:did>',views.sizepotDelete,name="sizepotDelete"),
    path('SizeUpdate/<int:eid>',views.sizepotUpdate,name="sizepotUpdate"),

    #Complaint
    path('ComplaintView/',views.complaintSelect,name="complaintSelect"),
    path('ComplaintReply/<int:cid>',views.complaintreplayInsert,name="complaintreplayInsert"),
    path('ComplaintSolvedView/',views.complaintsolvedSelect,name="complaintsolvedSelect"),

    #Review
    path('ReviewSelect/',views.ReviewSelect,name="ReviewSelect"),

    #sales report
    path('PlantsReport/',views.plantsReportSelect,name="plantsReportSelect"),
    path('PlantsDetails/<int:cid>',views.plantsdetails,name="plantsdetails"),
    path('PlantersReport/',views.plantersReportSelect,name="plantersReportSelect"),
    path('PlantersDetails/<int:pid>',views.plantersdetails,name="plantersdetails"),

    #logout
    path('Logout/',views.logoutview,name="logoutview"),
]
