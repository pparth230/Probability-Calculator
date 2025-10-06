import curses
import time
import random

def main(stdscr):
    curses.curs_set(0) # setting the cursror to invisible
    stdscr.keypad(True) # enabling the keypad mode
    stdscr.nodelay(True) # keeps the game running even if no key is pressed
    stdscr.timeout(100) # setting a delay for the getch() function

    snake = [(5, 10), (5, 9), (5, 8)]
    direction = curses.KEY_RIGHT
    score = 0

    food = (random.randint(1, 20), random.randint(1, 40)) # Random food position, this creates the memory of the food

    height, width = stdscr.getmaxyx()



    
    while True:
        key = stdscr.getch()
        if key != -1:
            direction = key

         # Calculate new head position
        head = snake[0]
        if direction == curses.KEY_RIGHT:
            new_head = (head[0], head[1] + 1)
        elif direction == curses.KEY_LEFT:
            new_head = (head[0], head[1] - 1)
        elif direction == curses.KEY_UP:
            new_head = (head[0] - 1, head[1])
        elif direction == curses.KEY_DOWN:
            new_head = (head[0] + 1, head[1])

        snake.insert(0, new_head)
        if new_head == food:
            food = (random.randint(1, 20), random.randint(1, 40))
            score += 1
        else:
            snake.pop()

        #Check for wall collisiopm
        if new_head[0] < 0 or new_head[0] >= height or new_head[1] < 0 or new_head[1] >= width:
            break # Game over

        #Check for self collision
        if new_head in snake[1:]:
            break # Game over

        stdscr.clear()

        #Draw the snake
        for segment in snake:
            stdscr.addch(segment[0], segment[1], '#')
        
        #Draw the food

        stdscr.addch(food[0], food[1], '^')
        stdscr.addstr(0, 0, f"Score: {score} ")
    
        
        stdscr.refresh()

    stdscr.nodelay(False)
    stdscr.timeout(-1)
    stdscr.clear()

    stdscr.addstr(height//2, width//2 - 10, f"Game Over! Score: {score}")
    stdscr.addstr(height//2 + 1, width//2 - 15, "Press any key to exit")
    stdscr.refresh()
    time.sleep(0.5)
    stdscr.getch()





if __name__ == "__main__":
    curses.wrapper(main)


