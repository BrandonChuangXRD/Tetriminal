import os
import options.opt as opt
import argparse
import screen
import gamemodes.zen as zen
import gamemodes.debugscreen as debugscreen
import curses
import sys

CONTROLS_SOURCE = "options/controls.json"
HANDLING_SOURCE = "options/handling.json"

#! this doesn't work, you need to find a way to pass in stdscr.
# def handle_exception(exc_type, exc_value, exc_traceback):
#     # Cleanup and restore the terminal state
#     curses.nocbreak()
#     stdscr.keypad(False)
#     curses.echo()
#     curses.endwin()

#     # Print the exception information
#     print("An error occurred:")
#     print("Type:", exc_type)
#     print("Value:", exc_value)
#     print("Traceback:")
#     traceback.print_tb(exc_traceback)

#     # Terminate the program
#     sys.exit(1)


def main():
    # sys.excepthook = handle_exception
    #create control/handling scheme if it doesn't exist, using default values
    if not os.path.isfile(HANDLING_SOURCE):
        default = opt.HandlingScheme()
        default = default.serialize()
        with open(HANDLING_SOURCE, "w") as outfile:
            outfile.write(default)

    if not os.path.isfile(CONTROLS_SOURCE):
        default = opt.ControlScheme()
        default = default.serialize()
        with open(CONTROLS_SOURCE, "w") as outfile:
            outfile.write(default)





    parser = argparse.ArgumentParser()
    parser.add_argument("--options", "-o", action="store_true", help="options the options menu")
    parser.add_argument("--zen", "-z", action="store_true", help="starts the zen gamemode (default)")
    parser.add_argument("--debug", "-d", action="store_true", help="activate debug mode")
    args = parser.parse_args()
    if args.options:
        screen.options_display()
        return 0
    
    ctrl = opt.ControlScheme()
    ctrl = ctrl.deserialize(CONTROLS_SOURCE)

    handle = opt.HandlingScheme()
    handle = handle.deserialize(HANDLING_SOURCE)
    if args.debug:
        debugscreen.start()
        return 0
    if args.zen:
        zen.start()
    else:
        screen.game_display("zen")
    return 1


if __name__  == "__main__":
    main()