import os
import options.options as options
import order
import argparse

CONTROLS_SOURCE = "options/controls.json"
HANDLING_SOURCE = "options/handling.json"



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



    ctrl = options.ControlScheme()
    ctrl = ctrl.deserialize(CONTROLS_SOURCE)

    handle = options.HandlingScheme()
    handle = handle.deserialize(HANDLING_SOURCE)

    parser = argparse.ArgumentParser()
    parser.add_argument("--options", "-o", action="store_true", help="options the options menu")
    parser.add_argument("")

    return 0


if __name__  == "__main__":
    main()