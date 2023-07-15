import curses

#the layout here is just text on the left side of the board and a queue on the right side, maximum 6 piece in visible queue
#for temp just do the board for now

#TODO terminal must be big enough to display at least the grid

def get_dimensions():
    return curses.COLS, curses.LINES

def options_display():
    disp = curses.initscr()
    curses.curs_set(0)
    curses.noecho()
    curses.cbreak() #must be turned off when option is selected
    return disp

def options_kill(disp):
    disp.clear()
    curses.nocbreak()
    disp.keypad(False)
    curses.echo()
    curses.endwin()
    return 0

def game_display():
    disp = curses.initscr()
    curses.noecho()
    curses.cbreak()
    curses.curs_set(0)
    disp.keypad(True)
    curses.start_color
    return disp

def game_kill(disp):
    disp.clear()
    curses.nocbreak()
    disp.keypad(False)
    curses.echo()
    curses.endwin()
    return 0



