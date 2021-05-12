"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
from campy.gui.events.mouse import onmouseclicked, onmousemoved

FRAME_RATE = 1000 / 60 # 120 frames per second.
NUM_LIVES = 3

graphics = BreakoutGraphics()


def main():
    """
    Breakout game, users can move paddle to make the ball rebound and break bricks, when all bricks are cleared,
    users win the game
    """
    # use chk to trigger the game, if chk = 1, game starts
    while True:
        chk = graphics.get_chk()
        if chk == 1:
            bouncing()
        pause(FRAME_RATE)


def bouncing():
    """
    The ball bouncing animation, counting number of lives as well
    """
    global NUM_LIVES
    # getting velocity of bounce
    dy = graphics.get_dy()
    dx = graphics.get_dx()
    # checking whether the game can resume or not
    if NUM_LIVES > 0 and graphics.num_bricks > 0:
        # when ball is above the ground, keep bouncing
        while graphics.ball.y + graphics.ball.height < graphics.window.height:
            graphics.ball.move(dx, dy)
            # when ball touches the frame, changes to the opposite direction
            if graphics.ball.x < 0 or graphics.ball.x + graphics.ball.width > graphics.window.width:
                dx = -dx
            elif graphics.ball.y < 0:
                dy = -dy
            # when the ball is in the frame, check if the ball touches objects
            else:
                result = graphics.check_collision()
                # if the ball touches the pad or brick, rebound
                if result == 'pad' or result == 'brick':
                    dy = -dy
                # if the ball does not collide with object, do nothing
                else:
                    pass
            pause(FRAME_RATE)
        # when ball falls to the ground, NUM_LIVE minus 1 and start the next round
        NUM_LIVES -= 1
        print('Remaining Lives:'+str(NUM_LIVES))
        graphics.window.remove(graphics.ball)
        pause(500)
        # place ball at the center, starting next round
        graphics.reset_ball()


if __name__ == '__main__':
    main()
