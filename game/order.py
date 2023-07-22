import random

pieces = ['s','z','l','j','o','t','i']

def sevenbag():
    while True:
        bag = pieces.copy()
        random.shuffle(bag)
        while len(bag) != 0:
            yield bag.pop()

def fourteenbag():
    while True:
        bag = pieces.copy() + pieces.copy()
        random.shuffle(bag)
        while len(bag) != 0:
            yield bag.pop()

def insanity():
    while True:
        yield random.choice(pieces)