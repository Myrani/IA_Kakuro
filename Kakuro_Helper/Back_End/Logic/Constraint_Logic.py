# Add Constraint
def propagate_add_constraint_up(self, kakuro, x, y, constraint):
    print(kakuro)
    if kakuro[x][y][0] == " | ":
        kakuro[x][y][4].append(constraint)
        propagate_add_constraint_up(kakuro, x-1, y, constraint)
    else:
        return kakuro


def propagate_add_constraint_down(self, kakuro, x, y, constraint):
    if kakuro[x][y][0] == " | ":
        kakuro[x][y][4].append(constraint)
        propagate_add_constraint_down(kakuro, x+1, y, constraint)
    else:
        return kakuro


def propagate_add_constraint_rigth(self, kakuro, x, y, constraint):
    if kakuro[x][y][0] == " | ":
        kakuro[x][y][4].append(constraint)
        propagate_add_constraint_rigth(kakuro, x, y+1, constraint)
    else:
        return kakuro


def propagate_add_constraint_left(self, kakuro, x, y, constraint):
    if kakuro[x][y][0] == " | ":
        kakuro[x][y][4].append(constraint)
        propagate_add_constraint_left(kakuro, x, y-1, constraint)
    else:
        return kakuro


def start_add_constraint_propagation(self, kakuro, x, y, constraint):
    kakuro = propagate_add_constraint_down(kakuro, x+1, y, constraint)
    kakuro = propagate_add_constraint_up(kakuro, x-1, y, constraint)
    kakuro = propagate_add_constraint_rigth(kakuro, x, y+1, constraint)
    kakuro = propagate_add_constraint_left(kakuro, x, y-1, constraint)

    return kakuro

# Remove Constraint


def propagate_remove_constraint_up(self, kakuro, x, y, constraint):
    if kakuro[x][y][0] == " | ":
        kakuro[x][y][4].remove(constraint)
        self.propagate_remove_constraint_up(kakuro, x-1, y, constraint)
    else:
        return kakuro


def propagate_remove_constraint_down(self, kakuro, x, y, constraint):
    if kakuro[x][y][0] == " | ":
        kakuro[x][y][4].remove(constraint)
        propagate_remove_constraint_down(kakuro, x+1, y, constraint)
    else:
        return kakuro


def propagate_remove_constraint_rigth(self, kakuro, x, y, constraint):
    if kakuro[x][y][0] == " | ":
        kakuro[x][y][4].remove(constraint)
        propagate_remove_constraint_rigth(kakuro, x, y+1, constraint)
    else:
        return kakuro


def propagate_remove_constraint_left(self, kakuro, x, y, constraint):
    if kakuro[x][y][0] == " | ":
        kakuro[x][y][4].remove(constraint)
        propagate_remove_constraint_left(kakuro, x, y-1, constraint)
    else:
        return kakuro


def start_remove_constraint_propagation(self, kakuro, x, y, constraint):
    kakuro = propagate_remove_constraint_down(kakuro, x+1, y, constraint)
    kakuro = propagate_remove_constraint_up(kakuro, x-1, y, constraint)
    kakuro = propagate_remove_constraint_rigth(kakuro, x, y+1, constraint)
    kakuro = propagate_remove_constraint_left(kakuro, x, y-1, constraint)

    return kakuro
