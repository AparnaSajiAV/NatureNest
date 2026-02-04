from django.contrib import admin
from django.urls import path,include
from Test import views

app_name="WebTest"
urlpatterns = [
    path('admin/', admin.site.urls),

    #team
    path('Team/',views.teamInsertSelect,name="teamInsertSelect"),

    #player
    path('Player/',views.playerInsertSelect,name="playerInsertSelect"),
    
    #position
    path('Position/',views.positionInsertSelect,name="positionInsertSelect"),

    #schedule
    path('Schedule/',views.scheduleInsertSelect,name="scheduleInsertSelect"),

    #playereleven
    path('PlayerEleven/',views.playerelevenInsertSelect,name="playerelevenInsertSelect"),

    #ajaxplayer
    path('AjaxPlayer/',views.ajaxplayer,name="ajaxplayer"),

    #view playereleven
    path('ViewPlayerEleven/',views.playerelevenschedulelevenSelect,name="playerelevenschedulelevenSelect"),

    #view playereleven team
    path('ViewPlayerElevenTeam/<int:did>',views.playereleventeamSelect,name="playereleventeamSelect"),
]
