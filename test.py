from main import next_state

if __name__ == "__main__":
    # dead cells with no live neighbours should stay dead.
    init_state1 = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    expected_next_state1 = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    actual_next_state1 = next_state(init_state1)

    if expected_next_state1 == actual_next_state1:
        print("PASSED 1")
    else:
        print("FAILED 1!")

#-----------------------------------------------------------------------------------------------------------------------

    # dead cells with exactly 3 neighbours should come alive.
    init_state2 = [
        [0,0,1],
        [0,1,1],
        [0,0,0]
    ]
    expected_next_state2 = [
        [0,1,1],
        [0,1,1],
        [0,0,0]
    ]
    actual_next_state2 = next_state(init_state2)

    if expected_next_state2 == actual_next_state2:
        print("PASSED 2")
    else:
        print("FAILED 2!")

# -----------------------------------------------------------------------------------------------------------------------

    # alive cells with 0 or 1 neighbours should become dead.
    init_state3 = [
        [0, 0, 1],
        [0, 1, 0],
        [0, 0, 0]
    ]
    expected_next_state3 = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    actual_next_state3 = next_state(init_state3)

    if expected_next_state3 == actual_next_state3:
        print("PASSED 3")
    else:
        print("FAILED 3!")

# -----------------------------------------------------------------------------------------------------------------------

    # alive cells with 2 or 3 neighbours should stay alive.
    init_state4 = [
        [0, 1, 1],
        [0, 1, 0],
        [0, 0, 0]
    ]
    expected_next_state4 = [
        [0, 1, 1],
        [0, 1, 0],
        [0, 0, 0]
    ]
    actual_next_state4 = next_state(init_state4)

    if expected_next_state4 == actual_next_state4:
        print("PASSED 4")
    else:
        print("FAILED 4!")

# -----------------------------------------------------------------------------------------------------------------------

    # alive cells with more than 3 neighbours should become dead.
    init_state5 = [
        [0, 1, 1],
        [1, 1, 1],
        [0, 1, 0]
    ]
    expected_next_state5 = [
        [0, 0, 1],
        [1, 0, 0],
        [0, 1, 0]
    ]
    actual_next_state5 = next_state(init_state5)

    if expected_next_state5 == actual_next_state5:
        print("PASSED 3")
    else:
        print("FAILED 3!")