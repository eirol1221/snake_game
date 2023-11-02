from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from prompt import Prompt
import time


def game_over():
    global game_is_on, play_again
    global scoreboard, screen, prompt
    scoreboard.game_over()
    game_is_on = False
    if (prompt.play_again()).lower() == 'y':
        screen.reset()
        scoreboard.reset_format()
    else:
        play_again = False


# constants
WALL = 290

scoreboard = Scoreboard()
prompt = Prompt()
turtle_game = Turtle()
# turtle_game.color("white")
turtle_game.hideturtle()

# get player's name
player = (prompt.get_player_name()).title()

play_again = True
while play_again:
    # screen setup
    screen = Screen()
    screen.setup(600, 600)
    screen.bgcolor("black")
    screen.title("Colored Worm Game: A Snake Game variant")

    # turn off animation
    screen.tracer(0)

    # objects
    snake = Snake()
    food = Food()

    # re-render the screen
    screen.update()

    # listen to key presses on the keyboard
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    # continue the game until the snake collides with the wall or itself
    game_is_on = True
    while game_is_on:
        scoreboard.show_score(player)
        screen.update()
        time.sleep(0.1)
        snake.move()

        # check if snake collides with the food
        if snake.head.distance(food) < 15:
            new_color = ()
            for color in food.pencolor():
                new_color += (int(color),)
            scoreboard.score += 1
            snake.extend(new_color)
            food.refresh()

        # check if snake collided with the wall or with itself
        if snake.collided_with_wall(WALL):
            game_over()
        else:
            for segment in snake.snake[1:]:
                if snake.head.distance(segment) < 10:
                    game_over()
                    break

