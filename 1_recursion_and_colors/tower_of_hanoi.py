def validate_disks(disks):
    """Validate the position of the disks"""
    for i in range(len(disks) - 1):
        # Make sure disks are sorted by size in descending order
        if disks[i][0] <= disks[i + 1][0]:
            return False
    return True

def move_disk(disk, source, target, rod_state):
    """Move the disks from one rod to another taking into account the restrictions"""
    if rod_state[target] and rod_state[target][-1][0] < disk[0]:
        # Restriction 1: A large disk cannot be placed on a small disk
        return False
    if rod_state[target] and rod_state[target][-1][1] == disk[1]:
        # Restriction 2: Discs of the same color cannot be stacked
        return False
    rod_state[target].append(disk)
    rod_state[source].pop()
    return True

def hanoi_with_constraints(n, disks, source, target, auxiliary, rod_state, moves, idx):
    """We apply recursion with restrictions"""
    if n == 0:
        return True  # Base case: no disks to move

    # Move n-1 discs to the auxiliary rod
    if not hanoi_with_constraints(n - 1, disks, source, auxiliary, target, rod_state, moves, idx + 1):
        return False

    # Move disk n to the target rod
    if not move_disk(disks[idx], source, target, rod_state):
        return False  # If the movement fails due to restrictions

    moves.append((disks[idx], source, target))

    # Move n-1 discs from the auxiliary rod to the target rod
    if not hanoi_with_constraints(n - 1, disks, auxiliary, target, source, rod_state, moves, idx + 1):
        return False

    return True

def solve_tower_of_hanoi(n, disks):
    if not validate_disks(disks):
        return -1  # Invalid input configuration

    # Initial state of the rods
    rod_state = {
        "A": disks[:],  # Source rod with all the discs
        "B": [],        # Auxiliar rod
        "C": []         # Target rod
    }
    moves = []

    if not hanoi_with_constraints(n, disks, "A", "C", "B", rod_state, moves, 0):
        return -1  # Impossible to resolve due to restrictions

    return moves

# Example of use

n = 3
disks = [(3, "red"), (2, "blue"), (1, "red")]

result = solve_tower_of_hanoi(n, disks)
print(result)
