import heapq


class Node:
                               #pathCost = g(n)   heuristicCost = h(n) 
    def __init__(self, value, parent, pathCost, heuristicCost):
        self.value = value
        self.parent = parent
        self.pathCost = pathCost
        self.heuristicCost = heuristicCost
        self.totalCost = pathCost + heuristicCost       # totalCost = f(n)

    def getValue(self):
        return self.value

    def setParent(self, parent):
        self.parent = parent

    def getParent(self):
        return self.parent
    
    def getTotalCost(self):
      return self.totalCost
     
    def getPathCost(self):
        return self.pathCost

    def __lt__(self, other):
      return self.totalCost < other.totalCost
      


def heuristicCost(start,goal):
  return (abs(start[0] - goal[0]) + abs(start[1] - goal[1]))
  # manhattan cost


def getNeighbors(location, grid):
    returnArray = []
    # check up
    if (location[1] - 1 >= 0 and location[1] - 1 <= len(grid[0])-1) and (grid[location[0]][location[1] + -1] > 0):
        returnArray.append([location[0], location[1] - 1])
    # check right
    if ((location[0] + 1 >= 0) and (location[0] + 1 <= len(grid)-1) and (grid[location[0] + 1][location[1]] > 0)):
        returnArray.append([location[0] + 1, location[1]])
    # check down
    if ((location[1] + 1 >= 0) and (location[1] + 1 <= len(grid[0])-1) and (grid[location[0]][location[1] + 1] > 0)):
        returnArray.append([location[0], location[1] + 1])
    # Check left
    if (location[0] - 1 >= 0) and (location[0] - 1 <= len(grid)-1) and (grid[location[0] - 1][location[1]] > 0):
        returnArray.append([location[0] - 1, location[1]])

    return returnArray


def expandNode(CurNode, grid, openList, copyOfOpenList, closedList, endNode):
    neighbors = getNeighbors(CurNode.getValue(), grid)
    notInClosedList = []
    match = False
    currentX = 0
    currentY = 0
    for x in neighbors:                                                     #compares neighbors with closed list, using currentY and currentX to count each side
        currentY = 0
        for y in closedList:
            if (neighbors[currentX] == closedList[currentY].getValue()):
                match = True
        currentY += 1
        if (match == False):
            notInClosedList.append(neighbors[currentX])
        match = False
        currentX += 1

    currentB = 0
    currentA = 0
    
    for a in notInClosedList:                                               #compares the items notInClosedList with the copyOfOpenList using currentA and currentB as iterators, after duplicates are found nodes are added to openList and copyOfOpenList
        currentB = 0
        for b in copyOfOpenList:
            if (a ==  b.getValue()):
                match = True
        currentB += 1
        if (match == False):
            newPath = CurNode.getPathCost() + grid[notInClosedList[currentA][0]][notInClosedList[currentA][1]]
            new = Node(notInClosedList[currentA], CurNode, newPath, heuristicCost(CurNode.getValue(), endNode))
            copyOfOpenList.append(new)
            heapq.heappush(openList, new)
        match = False
        currentA += 1

def checkOpenGreedy(CurNode, grid, openList, endNode):
    currentB = 0
    currentA = 0
    match = False
    neighbors = getNeighbors(CurNode.getValue(), grid)
    
    for a in neighbors:                                               #compares the items notInClosedList with the copyOfOpenList using currentA and currentB as iterators, after duplicates are found nodes are added to openList and copyOfOpenList
        currentB = 0
        for b in openList:
            if (a ==  b.getValue()):
                match = True
        currentB += 1
        if (match == False):
            
            new = Node(neighbors[currentA], CurNode, 0, heuristicCost(CurNode.getValue(), endNode))
            heapq.heappush(openList, new)
        match = False
        currentA += 1
        
# The grid values must be separated by spaces, e.g.
# 1 1 1 1 1 
# 1 0 0 0 1
# 1 0 0 0 1
# 1 1 1 1 1
# Returns a 2D list of 1s and 0s
def readGrid(filename):
    # print('In readGrid')
    grid = []
    with open(filename) as f:
        for l in f.readlines():
            grid.append([int(x) for x in l.split()])

    f.close()
    # print 'Exiting readGrid'
    return grid


# Writes a 2D list of 1s and 0s with spaces in between each character
# 1 1 1 1 1 
# 1 0 0 0 1
# 1 0 0 0 1
# 1 1 1 1 1
def outputGrid(grid, start, goal, path):
    # print('In outputGrid')
    filenameStr = 'path.txt'

    # Open filename
    f = open(filenameStr, 'w')

    # Mark the start and goal points
    grid[start[0]][start[1]] = 'S'
    grid[goal[0]][goal[1]] = 'G'

    # Mark intermediate points with *
    for i, p in enumerate(path):
        if i > 0 and i < len(path) - 1:
            grid[p[0]][p[1]] = '*'

    # Write the grid to a file
    for r, row in enumerate(grid):
        for c, col in enumerate(row):

            # Don't add a ' ' at the end of a line
            if c < len(row) - 1:
                f.write(str(col) + ' ')
            else:
                f.write(str(col))

        # Don't add a '\n' after the last line
        if r < len(grid) - 1:
            f.write("\n")

    # Close file
    f.close()


# print('Exiting outputGrid')


def InformedSearch(grid, start, goal, inp):
    if inp == "1":
        current = Node(start, None, 0, heuristicCost(start, goal))
        openlist = []
        heapq.heappush(openlist, current)
        copyOfOpenList = []
        copyOfOpenList.append(current)
        closedlist = []
        expandNode(current, grid, openlist, copyOfOpenList, closedlist, goal)

        while len(openlist) != 0:
            current =  heapq.heappop(openlist)            #gets current node from front of queue
            if current.getValue() == goal:
                print("Path found!")
                break                           #breaks loop if found
            else:
                closedlist.append(current)      #adds current to closed list and expands
                expandNode(current, grid, openlist, copyOfOpenList, closedlist, goal)

        return current
    
    if inp == "2":
        current = Node(start, None, 0, heuristicCost(start, goal))
        openlist = []
        heapq.heappush(openlist, current)
        copyOfOpenList = []
        copyOfOpenList.append(current)
        closedlist = []
        checkOpenGreedy(current, grid, openlist, goal)

        while len(openlist) != 0:
            current =  heapq.heappop(openlist)            #gets current node from front of queue
            if current.getValue() == goal:
                print("Path found!")
                break                           #breaks loop if found
            else:   #adds current to closed list and expands
                checkOpenGreedy(current, grid, openlist, goal)

        return current
    
    else:
        print("Invalid Entry")


def setPath(current, path):
    i = 0
    while current.getParent():
        i += 1                                  #counter
        path.append(current.getValue())         #adds parent value to path
        current = current.getParent()
        path.append(current.getValue())
    print(str(i) + ' steps to the goal.' )

def Main():
    grid = readGrid("file.txt")                                 #reads grid
    print("Start:")
    for i in grid:
        for r in i:
            print(r,end = " ")
        print()
    startingX = input("Please enter your starting X: ")
    startingY = input("Please enter your starting Y: ")
    goalX = input("Please enter your goal X: ")
    goalY = input("Please enter your goal Y: ")
    val = input("Please enter 1 for A* or 2 for Greedy: ")
    current = InformedSearch(grid, [int(startingX), int(startingY)], [int(goalX), int(goalY)], val)         #sets current to the node goal node returned by search
    path = []                                                   #sets path to blank
    setPath(current, path)                                      #uses set path to findt he path
    outputGrid(grid, [int(startingX), int(startingY)], [int(goalX), int(goalY)], path)                      #outputs grid
    print("Final:")
    for i in grid:
        for r in i:
            print(r,end = " ")
        print()

        

if __name__ == '__main__':
    Main()