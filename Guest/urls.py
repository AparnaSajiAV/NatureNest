from django.contrib import admin
from django.urls import path,include
from Guest import views

app_name="WebGuest"
urlpatterns = [
    path('admin/', admin.site.urls),

    #NewUser
    path('NewUserReg/',views.userInsert,name="userInsert"),

    #Ajax place
    path('AjaxPlace/',views.ajaxplace,name="ajaxplace"),

    #Login
    path('Login/',views.Login,name="Login"),

    #HomePage
    path('Index/',views.index,name="index"),
    path('About/',views.about,name="about"),
    path('Portfolio/',views.portfolio,name="portfolio"),
    path('Contact/',views.contact,name="contact"),
    path('Blog/',views.blog,name="blog"),
    path('ForgotPassword/', views.ForgotPass,name="ForgotPass"),
    path('ValidateOTP/', views.ValidateOTP,name="ValidateOTP"),
    path('CreatePassword/', views.CreatePass,name="CreatePass"),

]
