import curses
import time

def main(stdscr):
    # Set up the screen
    curses.curs_set(0)
    stdscr.timeout(100)  # Set a timeout for non-blocking input
    sh, sw = stdscr.getmaxyx()
    w = curses.newwin(sh, sw, 0, 0)
    
    # Initial positions and velocities
    ball_y, ball_x = sh // 2, sw // 2
    ball_vy, ball_vx = 1, 1
    paddle_y, paddle_x = sh - 2, sw // 2
    
    # Main game loop
    while True:
        w.clear()
        
        # Draw ball
        w.addch(int(ball_y), int(ball_x), curses.ASTERISK)
        
        # Draw paddle
        w.addch(paddle_y, paddle_x - 1, curses.HLINE)
        w.addch(paddle_y, paddle_x, curses.HLINE)
        w.addch(paddle_y, paddle_x + 1, curses.HLINE)
        
        # Move ball
        ball_y += ball_vy
        ball_x += ball_vx
        
        # Move paddle based on user input
        try:
            key = w.getch()
            if key == ord('a') and paddle_x > 1:
                paddle_x -= 1
            elif key == ord('d') and paddle_x < sw - 2:
                paddle_x += 1
        except curses.error:
            pass  # Ignore errors when reading from the keyboard
        
        # Ball bouncing off walls
        if ball_y == 0 or ball_y == sh - 1:
            ball_vy = -ball_vy
        if ball_x == 0 or ball_x == sw - 1:
            ball_vx = -ball_vx
        
        # Ball bouncing off paddle
        if ball_y == paddle_y - 1 and paddle_x - 1 <= ball_x <= paddle_x + 1:
            ball_vy = -ball_vy
        
        # Check for game over
        if ball_y == sh - 1:
            w.addstr(sh // 2, sw // 2 - 5, "Game Over!")
            w.refresh()
            time.sleep(2)
            break
        
        w.refresh()

if __name__ == "__main__":
    curses.wrapper(main)