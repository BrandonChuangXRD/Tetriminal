import curses
import json

#convert to JSON objects.
class HandlingScheme():
    def __init__(self, ARR = 2, DAS = 10, DCD = 0, SDF = 6, DAS_DC = False, HDL = True):
        self.ARR = ARR
        self.DAS = DAS
        self.DCD = DCD
        self.SDF = SDF
        self.DAS_DC = DAS_DC #Cancel DAS upon changing direction
        self.HDL = HDL #Hard Drop Lockout
    
    def serialize(self):
        jsobj = {"ARR": self.ARR, "DAS": self.DAS, "DCD": self.DCD, "SDF": self.SDF, "DAS_DC": self.DAS_DC, "HDL": self.HDL}
        return json.dumps(jsobj, indent = 4)
    
    def deserialize(self, jsfile):
        jsdict = None
        with open(jsfile, "r") as infile:
            jsdict = infile.read()
        jsdict = json.loads(jsdict)
        self.ARR = jsdict["ARR"]
        self.DAS = jsdict["DAS"]
        self.DCD = jsdict["DCD"]
        self.SDF = jsdict["SDF"]
        self.DAS_DC = jsdict["DAS_DC"]
        self.HDL = jsdict["HDL"]

#change this to take in strings instead of ints.
class ControlScheme():
    def __init__(self, left = curses.KEY_LEFT,
                 right = curses.KEY_RIGHT,
                 soft_drop = curses.KEY_DOWN,
                 hard_drop = ord(' '),
                 clockwise = ord('z'),
                 counterclockwise = ord('x'),
                 one_eighty = ord('a'),
                 hold = ord('c')):
        self.left = left
        self.right = right
        self.soft_drop = soft_drop
        self.hard_drop = hard_drop
        self.clockwise = clockwise
        self.counterclockwise = counterclockwise
        self.one_eighty = one_eighty
        self.hold = hold

    def serialize(self):
        jsobj = {"left": self.left,
                "right": self.right,
                "soft_drop": self.soft_drop,
                "clockwise": self.clockwise,
                "counterclockwise": self.counterclockwise,
                "one_eighty": self.one_eighty,
                "hold": self.hold}
        return json.dumps(jsobj, indent = 4)
    
    def deserialize(self, jsfile):
        jsdict = None
        with open(jsfile, "r") as infile:
            jsdict = infile.read()
        jsdict = json.loads(jsdict)
        self.left = jsdict["left"]
        self.right = jsdict["right"]
        self.soft_drop = jsdict["soft_drop"]
        self.clockwise = jsdict["clockwise"]
        self.counterclockwise = jsdict["counterclockwise"]
        self.one_eighty = jsdict["one_eighty"]
        self.hold = jsdict["hold"]
    
    
