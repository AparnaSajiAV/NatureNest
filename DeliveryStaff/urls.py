from django.contrib import admin
from django.urls import path,include
from DeliveryStaff import views

app_name="DeliveryStaff"
urlpatterns = [
    path('admin/', admin.site.urls),

    #homepage
    path('HomePage/',views.homepage,name="homepage"),

    #Profile
    path('MyProfile/',views.myprofile,name="myprofile"),
    
    #edit profile
    path('EditProfile/',views.editprofile,name="editprofile"),

    #change password
    path('ChangePassword/',views.changepassword,name="changepassword"),

    #pot
    #ShippedOrders
    path('ShippedPotOrdersView/',views.shippedpotsorderSelect,name="shippedpotsorderSelect"), 
    #DeliveredOrdersView
    path('DeliveredPotOrdersView/',views.deliveredpotsorderSelect,name="deliveredpotsorderSelect"), 

    #plant
    #ShippedOrders
    path('ShippedPlantsOrdersView/',views.shippedplantsorderSelect,name="shippedplantsorderSelect"), 
    #DeliveredOrders
    path('DeliveredPlantsOrdersView/',views.deliveredplantsorderSelect,name="deliveredplantsorderSelect"),
    path('UpdateStatus/<int:bid>',views.updateproductbooking,name="updateproductbooking"), 

]

