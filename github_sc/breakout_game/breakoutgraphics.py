"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
from campy.gui.events.timer import pause
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 5      # Maximum initial horizontal speed for the ball.
NUM_LIVES = 3


class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):
        self.ball_radius = ball_radius
        self.over = GLabel('GAME OVER')
        self.over.color = 'red'

        # Create a graphical window, with some extra space.
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # Create a paddle.
        self.pad = GRect(paddle_width, paddle_height)
        self.pad.filled = True
        self.pad.fill_color = 'black'
        self.window.add(self.pad, x=(self.window_width-paddle_width)/2, y=self.window_height-paddle_offset)

        # Default initial velocity for the ball.
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners.
        onmousemoved(self.move_pad)
        onmouseclicked(self.start_check)

        # the checker to decide whether the game can start,if 1, start, if 0, pending
        self.chk = 0

        # Draw bricks.
        for y in range(brick_offset, brick_rows*(brick_height+brick_spacing)+brick_offset, brick_height+brick_spacing):
            for x in range(0, self.window_width-brick_width+1, brick_width+brick_spacing):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                self.brick.fill_color = 'yellow'
                self.brick.color = 'green'
                self.window.add(self.brick, x=x, y=y)
        self.num_bricks = brick_cols * brick_rows

        # Center a filled ball in the graphical window.
        self.ball = GOval(ball_radius * 2, ball_radius * 2)
        self.ball.filled = True
        self.ball.fill_color = 'navy'
        self.ball.color = 'blue'
        self.window.add(self.ball, x=self.window_width / 2 - ball_radius, y=self.window_height / 2 - ball_radius)

    def move_pad(self, event):
        """
        To make the paddle moves following the mouse
        :param event: int, the coordinate(x,y) of the mouse
        """
        if event.x < self.pad.width/2:
            self.pad.x = 0
        elif event.x > self.window.width - self.pad.width/2:
            self.pad.x = self.window.width - self.pad.width
        else:
            self.pad.x = event.x - self.pad.width/2

    def get_dx(self):
        """
        To return the hidden object dx
        :return: int, the distance to move on x-coordinate per movement
        """
        return self.__dx

    def get_dy(self):
        """
        To return the hidden object dy
        :return: int, the distance to move on y-coordinate per movement
        """
        return self.__dy

    def reset_ball(self):
        """
        To set the ball at initial position and resetting chk to 0
        """
        self.window.add(self.ball, x=self.window_width / 2 - self.ball_radius, y=self.window_height / 2 - self.
                        ball_radius)
        self.chk = 0

    def start_check(self, m):
        """
        Check if the ball is at the center, if yes, start bouncing; if no, the click is ignored
        """
        if self.ball.x == self.window_width / 2 - self.ball_radius and self.ball.y == self.window_height / 2 - \
                self.ball_radius and self.num_bricks > 0:
            self.__dx = random.randint(1, MAX_X_SPEED)
            self.__dy = INITIAL_Y_SPEED
            if (random.random()) > 0.5:
                self.__dx = -self.__dx
            self.chk = 1

    def get_chk(self):
        """
        To return chk
        :return: int, the checker to detect whether the game should starts
        """
        return self.chk

    def check_collision(self):
        """
        Check if the 4 vertex touch paddle or brick
        :return: str or object, to indicate if the ball touches anything
        """
        for i in range(0, self.ball_radius * 2 + 1, self.ball_radius * 2):
            for j in range(0, self.ball_radius * 2 + 1, self.ball_radius * 2):
                is_obj = self.window.get_object_at(self.ball.x + j, self.ball.y + i)
                if is_obj is not None:
                    if is_obj is self.pad:
                        self.ball.move(0, -self.pad.height)
                        print('touch pad')
                        return 'pad'
                    else:
                        self.window.remove(is_obj)
                        self.num_bricks -= 1
                        print('touch brick')
                        return 'brick'
                return 'not collide'






