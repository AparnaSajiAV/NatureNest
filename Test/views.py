from django.shortcuts import render,redirect
from Test.models import *

# Create your views here.

#team
def teamInsertSelect(request):
    data=tbl_team.objects.all()
    if request.method=="POST":
        TeamName=request.POST.get('txtteam')
        tbl_team.objects.create(team_name=TeamName)
        return render(request,"Test/Team.html",{'data':data})
    else:
        return render(request,"Test/Team.html",{'data':data})

#player
def playerInsertSelect(request):
    data=tbl_player.objects.all()
    team=tbl_team.objects.all()
    position=tbl_position.objects.all()
    if request.method=="POST":
        PlayerName=request.POST.get('txtplayer')
        TeamName=tbl_team.objects.get(id=request.POST.get('sel_team'))
        PositionName=tbl_position.objects.get(id=request.POST.get('sel_position'))
        PlayerPhoto=request.FILES.get("fileimg")
        tbl_player.objects.create(team=TeamName,player_name=PlayerName,player_image=PlayerPhoto,position=PositionName)
        return render(request,"Test/Players.html",{'data':data})
    else:
        return render(request,"Test/Players.html",{'data':data,"team":team,"position":position})

#positionInsertSelect
def positionInsertSelect(request):
    data=tbl_position.objects.all()
    if request.method=="POST":
        PositionName=request.POST.get('txtpos')
        tbl_position.objects.create(position_name=PositionName)
        return render(request,"Test/Positions.html",{'data':data})
    else:
        return render(request,"Test/Positions.html",{'data':data})

#schedule
def scheduleInsertSelect(request):
    data=tbl_schedule.objects.all()
    if request.method=="POST":
        ScheduleName=request.POST.get('txtname')
        ScheduleFrom=request.POST.get('txtfrom')
        ScheduleDue=request.POST.get('txtdue')
        ScheduleVenue=request.POST.get('txtvenue')
        tbl_schedule.objects.create(schedule_name=ScheduleName,schedule_fromdate=ScheduleFrom,schedule_duedate=ScheduleDue,schedule_venue=ScheduleVenue)
        return render(request,"Test/MatchSchedule.html",{'data':data})
    else:
        return render(request,"Test/MatchSchedule.html",{'data':data})

#playereleven
def playerelevenInsertSelect(request):
    schedule=tbl_schedule.objects.all()
    data=tbl_playereleven.objects.all()
    team=tbl_team.objects.all()
    if request.method=="POST":
        ScheduleName = tbl_schedule.objects.get(id=request.POST.get('sel_schedule'))
        PlayerName=tbl_player.objects.get(id=request.POST.get('sel_player'))
        tbl_playereleven.objects.create(schedule=ScheduleName,player=PlayerName)
        return render(request,"Test/PlayerEleven.html",{'data':data})
    else:
        return render(request,"Test/PlayerEleven.html",{'data':data,"schedule":schedule,"team":team})

#ajaxplayer
def ajaxplayer(request):
    team=tbl_team.objects.get(id=request.GET.get("did"))
    player=tbl_player.objects.filter(team=team)
    return render(request,"Test/AjaxPlayer.html",{"player":player})

#view playereleven schedule
def playerelevenschedulelevenSelect(request):
    data=tbl_schedule.objects.all()
    return render(request,"Test/ViewPlayerEleven.html",{'data':data})

#view playereleven team
def playereleventeamSelect(request,did):
    #data=tbl_playereleven.objects.all()
    #data=tbl_player.objects.all()
    schedule=tbl_schedule.objects.get(id=did)
    data=tbl_playereleven.objects.filter(schedule=schedule)
    return render(request,"Test/ViewPlayerElevenTeam.html",{'data':data})

