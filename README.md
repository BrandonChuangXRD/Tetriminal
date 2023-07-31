# Tetriminal
An X Application of an infinite tetris game using SRS and 7 bag, using curses for the display and pynput for the inputs. Tries to mimic the Zen gamemode in [TETR.IO](https://tetr.io/)

## Controls and Handling
| Control | Default Key |
| ------- | ----------- |
| up | up arrow |
| soft drop | down arrow |
| left | left arrow |
| right | right arrow |
| hard drop | space |
| counter-clockwise | z |
| clockwise | x |
| 180-spin | a |
| hold | c |

| Handling | Default Value |
| -------- | ------------- |
| ARR (Auto-Repeat Rate) | 2 F(rames) |
| DAS (Delayed Auto-Shift) | 10 F(rames) |
| DCD (DAS Cut Delay) | 0 F(rames) |
| DAS Direction Cancel | on |
| Prevent accidental hard drops | off |

## Installation and Execution
As an X application, this requires an X11 terminal or similar (ex: xterm). Otherwise, the inputs will not register at all.
This was done because X11 seems to be the only way for inputs to be registered as actions (key down, key up). The curses library
only records inputs like it is being typed, were it registers one press, then waits, then spams the key. Its possible to get it to work on other
terminals (such as wayland) with root access, but I did not really understand these issues until later. In the future maybe I will make it
compatible.

the `pynput` library is required to run this program. This can be done using the following command:

```pip install pynput```

this can be run with the command `python3 main.py` as of now. the `-d` flag runs the debug mode, which currently only tests the screen and a few inputs.

## Problems, Contradictions, and Possible Future Developments
- Due to the modularization, it is possible in the future this gets expanded to include 40 line, blitz, and custom room creations (just like TETR.IO).
- the SRS kick table is implemented instead of SRS+, so the I kicks are not the same as TETR.IO.
- need to implement preventing accidental hard drops

## Credits and Method Reasonings
- Thank you to the developers behind the [pynput](https://github.com/moses-palmer/pynput) on github for the pynput library. The curses library was insufficent for this project due to the lack of "release events" for keys.
- The curses library was used because it interested me; it was used in a class assignment for class I took, but during a different quarter.
- I tried to modularize as best as possible, which explains the excess files.
- The SRS (Super Rotation System) implementation is based on its [wikipedia page](https://tetris.wiki/Super_Rotation_System).
- The NRS (Nintendo Rotation System) implementation is based on its [fandom page](https://tetris.fandom.com/wiki/Nintendo_Rotation_System).
- The layout, information, and gamemodes are based off of [TETR.IO](https://tetr.io/). Fun game 10/10.
- I've seperated the spawn point for pieces from the rotation system (unlike the wiki) since it should be modifiable by the user.