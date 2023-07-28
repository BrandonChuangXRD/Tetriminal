import game.rotation.rotate as rotate

#!untested
KICKS_CW_I = [[(0, 0), (0, -1), (0, 2), (2, -1), (-1, 2)],
               [(0, 0), (0, 2), (0, -1), (1, 2), (-2, -1)],
               [(0, 0), (0, 1), (0, -2), (-2, 1), (1, -2)],
               [(0, 0), (0, -2), (0, 1), (-1, -2), (2, 1)]
]

KICKS_CW_O = [[(0, 0)],
               [(0, 0)],
               [(0, 0)],
               [(0, 0)]
]

KICKS_CW_OTHER = [[(0,0), (0, 1), (1, 1), (-2, 0), (-2, 1)],
         [(0,0), (0, 1), (-1, 1), (2, 0), (2, 1)],
         [(0,0), (0, -1), (1, -1), (-2, 0), (-2, -1)],
         [(0,0), (0, -1), (-1, -1), (2, 0), (2, -1)]
         ]

KICKS_CCW_I = [[(0, 0), (0, -2), (0, 1), (-1, -2), (2, 1)],
              [(0, 0), (0, -1), (0, 2), (2, -1), (-1, 2)],
              [(0, 0), (0, 2), (0, -1), (1, 2), (-2, -1)],
              [(0, 0), (0, 1), (0, -2), (-2, 1), (1, -2)]
]

KICKS_CCW_O = [[(0, 0)],
              [(0, 0)],
              [(0, 0)],
              [(0, 0)]
]

KICKS_CCW_OTHER = [[(0,0), (0, -1), (1, -1), (-2, 0), (-2, -1)],
         [(0,0), (0, 1), (-1, 1), (2, 0), (2, 1)],
         [(0,0), (0, 1), (1, 1), (-2, 0), (-2, 1)],
         [(0,0), (0, -1), (-1, -1), (2, 0), (2, -1)]
         ]

KICKS_OE = [[(0,0)],
         [(0,0)],
         [(0,0)],
         [(0,0)]
]


#converts above lists into the 3d arrays
def _set_kicks(d: dict, key: str):
    ccw = None
    cw = None
    oe = KICKS_OE
    if key == "i":
        ccw = KICKS_CCW_I
        cw = KICKS_CW_I
    if key == "o":
        ccw = KICKS_CCW_O
        cw = KICKS_CW_O
    else:
        ccw = KICKS_CCW_OTHER
        cw = KICKS_CW_OTHER

    d[key] = []
    for y in range(4):
        d[key].append([])
        for x in range(4):
            if y == x:
                d[key][y].append(None)
            elif y == (x-1)%4: #counter clockwise
                d[key][y].append(ccw[y])
            elif y == (x+1)%4: #clockwise
                d[key][y].append(cw[y])
            else: #180
                d[key][y].append(oe[y])
    return 0

#returns true if rotate was successful, false otherwise.
class SRS(rotate.Rotate):
    def __init__(self):
        self.held_keys = []
        self.kick_dict = {}
        for i in "iotszjl":
            _set_kicks(self.kick_dict, i)