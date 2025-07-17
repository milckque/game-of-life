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


print(random_state(5, 5))