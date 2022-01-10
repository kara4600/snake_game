from turtle import Turtle
SNAKE_PIXEL_SIZE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake(Turtle):

    def __init__(self):
        super().__init__()
        self.snake_body = []
        self.colors = ["white", "dodger blue", "tan", "violet"]
        self.new_snake()
        self.snake_head = self.snake_body[0]

    def new_snake(self):
        """Creates the initial snake body"""
        # Snake will always be placed in center of screen at start of game
        for num in range(0, 3):
            new_square = Turtle(shape="square")
            new_square.penup()
            new_square.color(self.colors[num])
            new_square.goto(x=int(num * -SNAKE_PIXEL_SIZE), y=0)
            self.snake_body.append(new_square)

    def eaten_food(self):
        """Makes the snake grow larger"""
        new_square = Turtle(shape="square")
        new_square.penup()
        new_square.color("white")
        new_square.goto(x=self.snake_body[-1].xcor(), y=self.snake_body[-1].ycor())
        self.snake_body.append(new_square)

    '''
        VISUAL
        |4||3||2||1|
         ^ during first iteration (part = 3/block 4)
         snake_body[part - 1] looks at part = 2/block 3
         then moves block 4 to where block 3 was
    '''

    def move(self):
        """Makes the snake move continuously"""
        # Makes the rest of the tail chase after the head
        for part in range(len(self.snake_body) - 1, 0, -1):
            x_coord = self.snake_body[part - 1].xcor()
            y_coord = self.snake_body[part - 1].ycor()
            self.snake_body[part].goto(x=x_coord, y=y_coord)

        self.snake_head.forward(SNAKE_PIXEL_SIZE)

    def over_bounds(self):
        """Detects when the snake has collided with a wall"""
        window_width = self.getscreen().window_width() / 2
        window_height = self.getscreen().window_height() / 2

        return (abs(self.snake_head.xcor()) >= window_width) | (abs(self.snake_head.ycor()) >= window_height)

    def collision(self):
        collided = False

        # Flags if snake head collides with any part of its body
        for part in self.snake_body[1:]:
            if self.snake_head.distance(part.position()) <= 10:
                collided = True

        return collided

    def turn_up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def turn_down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def turn_left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def turn_right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)
