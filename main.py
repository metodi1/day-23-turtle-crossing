import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
tim = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.onkey(tim.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car_manager.create_car()
    car_manager.move_cars()


    #detect finis line
    if tim.is_at_finish_line():
        tim.go_back_to_start()
        car_manager.level_up()
        scoreboard.increase_level()



    #detect collisian with car
    for car in car_manager.all_cars:
        if car.distance(tim)<20:
            game_is_on = False
            scoreboard.game_over()
            screen.exitonclick()


    screen.update()
