# Tetriminal
An infinite tetris game using SRS and 7 bag, running entirely in the terminal using curses. Tries to mimic the Zen gamemode in [TETR.IO](https://tetr.io/)

## Default Controls and Handling
| Control | Default Key |
| ------- | ----------- |
| 

| Handling | Default Value |
| -------- | ------------- |

ARR: 2F
DAS: 10F
DCD: 0F
SDF: 6x
DAS Direction Cancel: on
Prevent accidental Hard Drops: on
a

## Installation and Execution
the `pynput` library is required to run this program. This can be done using the following command:

```pip install pynput```

this can be run with the command `python3 main.py` as of now. the `-d` flag runs the debug mode, which currently only tests the screen and a few inputs.

## Problems, Contradictions, and Possible Future Developments
- This program does not run properly in WSL (Windows Subsystem for Linux).

## Credits and Method Reasonings
- Thank you to the developers behind the [pynput](https://github.com/moses-palmer/pynput) on github for the pynput library. The curses library was insufficent for this project due to the lack of "release events" for keys.
- The curses library was used because it interested me; it was used in a class assignment for class I took, but for a different quarter.
- The SRS (Super Rotation System) implementation is based on its [wikipedia page](https://tetris.wiki/Super_Rotation_System).
- The NRS (Nintendo Rotation System) implementation is based on its [fandom page](https://tetris.fandom.com/wiki/Nintendo_Rotation_System).
- The layout, information, and gamemodes are based off of [TETR.IO](https://tetr.io/). Fun game 10/10.