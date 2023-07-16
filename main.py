import os
import options.options as options
import order
import argparse
import screen
import gamemodes.zen as zen
import gamemodes.debug as debug

CONTROLS_SOURCE = "options/controls.json"
HANDLING_SOURCE = "options/handling.json"

0

def main():
    #create control/handling scheme if it doesn't exist, using default values
    if not os.path.isfile(HANDLING_SOURCE):
        default = options.HandlingScheme()
        default = default.serialize()
        with open(HANDLING_SOURCE, "w") as outfile:
            outfile.write(default)

    if not os.path.isfile(CONTROLS_SOURCE):
        default = options.ControlScheme()
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
    
    ctrl = options.ControlScheme()
    ctrl = ctrl.deserialize(CONTROLS_SOURCE)

    handle = options.HandlingScheme()
    handle = handle.deserialize(HANDLING_SOURCE)
    if args.debug:
        debug.start()
    if args.zen:
        zen.start()
    else:
        screen.game_display("zen")
    return 1


if __name__  == "__main__":
    main()