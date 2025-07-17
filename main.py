import random
DEAD = 0
ALIVE = 1

def dead_state(width, height):
    return [[DEAD for _ in range(width)] for _ in range(height)]

def random_state(width, height):
    state = dead_state(height, width)
    for x in range(width):
        for y in range(height):
            if random.random() > 0.7:
                state[x][y] = ALIVE
    return state

def render(state):
    display = {
        DEAD: ' ',
        ALIVE: u"\u2588",
    }
    height = len(state)
    width = len(state[0])
    lines = []
    for x in range(width):
        line = ''
        for y in range(height):
            line += display[state[x][y]] * 3
        lines.append(line)
    print("\n".join(lines))
