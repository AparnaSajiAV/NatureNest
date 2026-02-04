from django.db import models

# Create your models here.

#team
class tbl_team(models.Model):
    team_name=models.CharField(max_length=50)

#positions
class tbl_position(models.Model):
    position_name=models.CharField(max_length=50)

#Player
class tbl_player(models.Model):
    player_name=models.CharField(max_length=50)
    team=models.ForeignKey(tbl_team,on_delete=models.CASCADE)
    position=models.ForeignKey(tbl_position,on_delete=models.CASCADE)
    player_image=models.FileField(upload_to='Assets/TestPhoto/')

#Schedule
class tbl_schedule(models.Model):
    schedule_name=models.CharField(max_length=50)
    schedule_fromdate=models.CharField(max_length=50)
    schedule_duedate=models.CharField(max_length=50)
    schedule_venue=models.CharField(max_length=50)

#player eleven
class tbl_playereleven(models.Model):
    schedule=models.ForeignKey(tbl_schedule,on_delete=models.CASCADE)
    player=models.ForeignKey(tbl_player,on_delete=models.CASCADE)