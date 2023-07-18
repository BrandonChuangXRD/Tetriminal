import curses

#the layout here is just text on the left side of the board and a queue on the right side, maximum 6 piece in visible queue
#for temp just do the board for now

#TODO terminal must be big enough to display at least the grid
#TODO minimum for now: length 30 height 25
#TODO a grid border could be cool.
#! it would be very nice to have a double wide version, blocks being 2x3 to make it more square
MINOCHAR =  "█"
BACKUPS = "▊ █" 



#use the splat operator for this: https://www.geeksforgeeks.org/python-passing-dictionary-as-arguments-to-function/#
# ch: _ChType, attr: int = ...

COLOR_CODES = {}

#pieces spawn at a minimum height of 21 (two above the end)
#2 extra rows are displayed above "height"
class game_display():
    #use a pads for the grid and queue
    def __init__(self, length = 10, height = 20+4):
        self.disp = None #curses display class
        self.grid_pad = None #curses pad class
        self.hold_pad = None
        self.queue_pad = None
        
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

    #! Do this later.
    #blanks out the screen, centers text saying the terminal is too small
    def pause_display():
        return 0

    #! Do this later.
    #make sure the terminal doesn't get changed to be too small.
    #in the future, this could just pause the game.
    #returns false if terminal size is too small.
    def terminal_change(self):
        return True
    
    # TODO
    def color_init(self):
        #need three routes for no color, color, fancy custom colors
        if not curses.can_change_color():
            return False
        global COLOR_CODES
        curses.start_color()
        curses.use_default_colors()
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_WHITE)
        curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_WHITE)
        curses.init_pair(4, curses.COLOR_MAGENTA, curses.COLOR_WHITE)
        curses.init_pair(5, curses.COLOR_RED, curses.COLOR_WHITE)
        curses.init_pair(6, curses.COLOR_BLUE, curses.COLOR_WHITE)
        curses.init_pair(7, curses.COLOR_CYAN, curses.COLOR_WHITE)
        curses.init_pair(8, curses.COLOR_YELLOW, curses.COLOR_WHITE)
        curses.init_pair(9, curses.COLOR_BLACK, curses.COLOR_WHITE)
        curses.init_pair(10, curses.COLOR_WHITE, curses.COLOR_BLACK)
        curses.init_pair(11, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(52, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(53, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(54, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
        curses.init_pair(55, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(56, curses.COLOR_BLUE, curses.COLOR_BLACK)
        curses.init_pair(57, curses.COLOR_CYAN, curses.COLOR_BLACK)
        curses.init_pair(58, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        COLOR_CODES =     {"z": (MINOCHAR, curses.color_pair(2)),
                           "s": (MINOCHAR, curses.color_pair(3)),
                           "t": (MINOCHAR, curses.color_pair(4)),
                           "l": (MINOCHAR, curses.color_pair(5) | curses.A_HORIZONTAL), # TODO no good color for orange. quick-ish workaround.
                           "j": (MINOCHAR, curses.color_pair(6)),
                           "i": (MINOCHAR, curses.color_pair(7)),
                           "o": (MINOCHAR, curses.color_pair(8)),
                           "e": (MINOCHAR, curses.color_pair(9)),
                           "g": (MINOCHAR, curses.color_pair(10)),
                           "x": ("X", curses.color_pair(11))} # TODO this one should probably be "><" instead of two x's next to each other.

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
        if self.terminal_change() == False:
            self.kill()
            print("Terminal size is too small")
            return 1
        self.color_init()
        self.update_info()
        self.update_board(grid)
        self.update_hold()
        self.update_queue()

    # TODO
    #just rerender the entire thing for now
    #start with information going bottom up
    #the hold spot should only be 4 characters tall.
    def update_info(self):
        return 0
    
    # TODO
    #at start, needs to be empty
    #right justified
    def update_hold(self, piece = None):
        text = "HOLD"
        #"HOLD" text at the top
        textpos_y = (self.display_height//2)-(self.grid_height//2)+4
        textpos_x = (self.display_length//2)-self.grid_length-6 #-1 for the border, -4 for the text length
        textwin = curses.newwin(2, 5, textpos_y, textpos_x)
        textwin.addstr("HOLD")
        textwin.refresh()
        #next piece, make it just T for now
        if piece is not None:
            piecewin = curses.newwin(3, 8, textpos_y+2, textpos_x-4)
            if piece == "t":
                piecewin.addstr(("    ██    ██████"), curses.color_pair(54))
            elif piece == "j":
                piecewin.addstr(("  ██      ██████"), curses.color_pair(56))
            elif piece == "l":
                piecewin.addstr(("      ██  ██████"), curses.color_pair(55))
            elif piece == "s":
                piecewin.addstr(("    ████  ████  "), curses.color_pair(53))
            elif piece == "z":
                piecewin.addstr(("  ████      ████"), curses.color_pair(52))
            elif piece == "o":
                piecewin.addstr(("  ████    ████  "), curses.color_pair(58))
            elif piece == "i":
                piecewin.addstr(("        ████████"), curses.color_pair(57))
            piecewin.refresh()
        return 0
    
    #! You might want to just make this a window.
    #just rerender the entire thing for now, its possible to make a system where it only updates required pixels.
    def update_board(self, grid):
        #print("grid:")
        #print(grid)
        center_height = self.display_height//2
        center_length = self.display_length//2
        #adding one is the only way I can get it not to crash. I don't know why,
        #but python doc shows this
        self.grid_pad = curses.newpad(self.display_height+1, self.display_length+1)
        # TODO Fill in the pad, one pixel at a time (will need to be replaced to make the board larger)
        #make sure to account for the hidden rows.
        for y in range(self.grid_height-1, -1, -1):
            for x in range(self.grid_length):
                #grid will be in reversed order
                g_y = self.grid_height-y
                self.grid_pad.addch(y, x*2, *COLOR_CODES[grid[g_y][x]])
                self.grid_pad.addch(y, x*2+1, *COLOR_CODES[grid[g_y][x]])
        #refresh at the correct place
        self.grid_pad.refresh(0, 0, #start of pad
                              center_height-(self.grid_height//2), center_length-self.grid_length, #top left corner of window
                              center_height+((self.grid_height+1)//2), center_length+self.grid_length+1) #bottom right corner of window
        return 0
    
    # TODO
    #entire thing needs to be updated anyways
    def update_queue(self):
        return 0


def get_dimensions(self):
    return self.disp.getmaxyx()

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


