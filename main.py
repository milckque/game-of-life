import random
import time

DEAD = 0
ALIVE = 1

def dead_state(width, height):
    return [[DEAD for _ in range(height)] for _ in range(width)]

def random_state(width, height):
    state = dead_state(width, height)
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

    width = len(state)
    height = len(state[0])
    lines = []
    lines.append('-' * width * 3)
    for x in range(width):
        line = ''
        for y in range(height):
            line += display[state[x][y]] * 3
        lines.append(line)
    lines.append('-' * width * 3)

    print("\n".join(lines))

def next_cell_state(cell_coords, state, height, width):
    x = cell_coords[0]
    y = cell_coords[1]
    live_neighbours = 0

    # checking the 8 neighbours
    for x1 in range(x-1, x+2):
        # edge of board check
        if x1 < 0 or x1 >= width: continue

        for y1 in range(y-1, y+2):
            # edge of board check
            if y1 < 0 or y1 >= height: continue
            # not the same cell check
            if x1 == x and y1 == y: continue

            if state[x1][y1] == ALIVE: live_neighbours += 1

    if state[x][y] == ALIVE:
        if live_neighbours <= 1:
            return DEAD
        elif live_neighbours <=3:
            return ALIVE
        else:
            return DEAD
    else:
        if live_neighbours == 3:
            return ALIVE
        else:
            return DEAD

def next_state(original_state):
    width = len(original_state)
    height = len(original_state[0])

    new_state = dead_state(width, height)
    for x in range(width):
        for y in range(height):
            new_state[x][y] = next_cell_state((x, y), original_state, height, width)

    return new_state

def run_forever(state):
    new_state = state
    while True:
        render(new_state)
        new_state = next_state(new_state)
        time.sleep(0.5)

if __name__ == "__main__":
    state = random_state(20, 20)
    run_forever(state)