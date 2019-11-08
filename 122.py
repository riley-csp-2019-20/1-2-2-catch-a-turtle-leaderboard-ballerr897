# a121_catch_a_turtle.py

#-----import statements-----
import turtle as trtl
import random
import leaderboard as lb

#-----game configuration----
trtlshape = "arrow"   
trtlsize = 4
trtlcolor = "green"
#scoreboard variables

leaderboard_file_name = "a122_leaderboard.txt"
leader_names_list = []
leader_scores_list = []
player_name = input("Please enter your name")

score = 0

scorewriter = trtl.Turtle()
scorewriter.penup()
scorewriter.goto(-350,300)

timer = 5
counter_interval = 1000   #1000 represents 1 second
timer_up = False

font_setup = ("Times new roman", 30, "bold")
scorewriter.write(score, font= font_setup)

#-----initialize turtle-----
Keagan = trtl.Turtle(shape=trtlshape)
Keagan.color(trtlcolor)
Keagan.speed(3)
Keagan.shapesize(trtlsize)
scorewriter.ht()

counter =  trtl.Turtle()
counter.speed(0)
counter.ht()
counter.penup()
counter.goto(275,275)

#-----game functions--------
def turtle_clicked(x,y):
    print("keagan got clicked")
    change_posistion()
    update_score()
   
def change_posistion():
    Keagan.penup()
    Keagan.ht()
    if not timer_up:
      Keaganx = random.randint(-400,400)
      Keagany = random.randint(-300,300)
      Keagan.goto(Keaganx,Keagany)
      Keagan.st()

def update_score():
    global score
    score += 1
    print(score)
    scorewriter.clear()
    scorewriter.write(score, font= font_setup)

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    manage_leaderboard()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 

# manages the leaderboard for top 5 scorers
def manage_leaderboard():
  
  global leaderboard_file_name
  global leader_scores_list
  global leader_names_list
  global score
  global Keagan

  # load all the leaderboard records into the lists
  lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)

  # TODO
  if (len(leader_scores_list) < 5 or score > leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(leader_names_list, leader_scores_list, True, Keagan, score)

  else:
    lb.draw_leaderboard(leader_names_list, leader_scores_list, False, Keagan, score)

#-----events----------------

wn = trtl.Screen()
wn.ontimer(countdown, counter_interval) 
Keagan.onclick(turtle_clicked)
wn.mainloop()
