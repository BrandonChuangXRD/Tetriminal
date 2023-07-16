import curses

#the layout here is just text on the left side of the board and a queue on the right side, maximum 6 piece in visible queue
#for temp just do the board for now

#TODO terminal must be big enough to display at least the grid
MINOCHAR =  "▊"
BACKUPS = "▊ █" 

#pieces spawn at a minimum height of 21 (two above the end)
#2 extra rows are displayed above "height"
class game_display():
    #use a pads for the grid and queue
    def __init__(self, length = 10, height = 20+4):
        self.disp = None #curses display class
        self.grid = None #maybe needed later for larger resolutions
        self.grid_height = height
        self.grid_length = length
        self.info_char_count = 10 #how many characters of text are allowed
        #for detecting changes in the terminal dimensions
        self.display_length = -1
        self.display_height = -1

    def kill(self):
        self.disp.clear()
        curses.nocbreak()
        self.disp.keypad(False)
        curses.echo()
        curses.endwin()
        return 0    

    #blanks out the screen, centers text saying the terminal is too small
    def pause_display():
        return 0

    #make sure the terminal doesn't get changed to be too small.
    #in the future, this could just pause the game.
    #returns false if terminal size is too small.
    def terminal_change(self):
        return True
    
    def start(self, grid = [], leftinfo = [], queue = []):
        self.disp = curses.initscr()
        curses.noecho()
        curses.cbreak()
        curses.curs_set(0)
        self.disp.keypad(True)
        curses.start_color()
        if curses.has_colors() == False:
            print("TERMINAL DOES NOT HAVE COLORS: not implemented.")
            return 1
        #Each square needs to be its own pad
        #determine the minimum terminal size and confirm sizing
        self.display_height, self.display_length = self.disp.getmaxyx()
        #! Temporary fix, not tested
        if self.terminal_change() == 1:
            self.kill()
            print("Terminal size is too small")
            return 1
        
        self.update_info()
        self.update_board()
        self.update_hold()
        self.update_queue()

    #just rerender the entire thing for now
    def update_info(self):
        return 0
    
    #at start, needs to be empty
    def update_hold(self):
        return 0

    #just rerender the entire thing for now
    def update_board(self):
        return 0
    
    #entire thing needs to be updated anyways
    def update_queue(self):
        return 0


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


# def game_display(length=10, height=20, grid = None, leftinfo = [], queue = []):


