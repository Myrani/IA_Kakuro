def gridSmartFiller(grid):
    for line in grid:
        state = False
        for case in line:
            if case[0] != "#/#":

                state = not state

            elif case[0] == "#/#":
                if state:
                    case[0] = "***"
                else:
                    continue
    return grid

def gridMaker(x,y):
    grid = []
    for x in range(0,x):
        grid.append([["#/#"] for y in range(0,y)])


    grid[0][2][0] = "11/#"
    grid[0][3][0] = "4/#"
    grid[1][1][0] = "14/5"
    grid[1][4][0] = "10/#"
    grid[2][0][0] = "#/17"
    grid[2][5][0] = "3/#"
    grid[3][0][0] = "#/6"
    grid[3][3][0] = "3/4"
    grid[4][1][0] = "#/10"
    grid[5][2][0] = "#/3"
    
    return gridSmartFiller(grid)


def terminalPrint(kakuro):
    for line in kakuro:
        for case in line:
            print("|"+str(case[0:len(case)]).replace("[","").replace("]",""),end="")
        print("")


kakuro_projet = gridMaker(6,6)

terminalPrint(kakuro_projet)