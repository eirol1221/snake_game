from turtle import Turtle, Screen

# constants
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STEP = 20

screen = Screen()
screen.colormode(255)


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    # def refresh(self):
    #     self.snake = []
    #     self.create_snake()

    # create 3 20x20 segments to form a snake
    def create_snake(self):
        for x_pos in range(0, -60, -20):
            self.add_segment((x_pos, 0), "white")

    # add new segment to the snake
    def add_segment(self, position, new_color):
        new_segment = Turtle("circle")
        new_segment.color(new_color)
        new_segment.up()
        new_segment.goto(position)
        self.snake.append(new_segment)

    # add new segment when the snake collides with the food (the snake eats the food)
    def extend(self, new_color):
        self.add_segment(position=self.snake[-1].position(), new_color=new_color)

    # move the snake's segments, starting from the last segment, to move the snake
    def move(self):
        for index in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[index - 1].xcor()
            new_y = self.snake[index - 1].ycor()
            self.snake[index].goto(new_x, new_y)
        self.head.forward(STEP)

    # restrict down movement when snake is going up
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    # restrict up movement when snake is going down
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    # restrict right movement when snake is going left
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    # restrict left movement when snake is going right
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def collided_with_wall(self, wall):
        return (self.head.xcor() > wall or
                self.head.xcor() < -wall or
                self.head.ycor() > wall or
                self.head.ycor() < -wall)
