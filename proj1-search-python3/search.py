# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):

    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"


    # print("Start:", problem.getStartState())
    # print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    # print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    stack = util.Stack()
    checkedSpots = []
    checkedSpots.append(problem.getStartState())
    currentState = problem.getStartState()
    tuple = (currentState, [])
    stack.push(tuple)
    while not stack.isEmpty() and not problem.isGoalState(currentState):
        nextState, directions = stack.pop()
        checkedSpots.append(nextState)
        successor = problem.getSuccessors(nextState)
        for i in successor:
            if i[0] not in checkedSpots:
                currentState = i[0]
                direction = i[1]
                stack.push((i[0], directions + [i[1]]))


    return directions + [direction]
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""

    # print("Start:", problem.getStartState())
    # print("Start's successors:", problem.getSuccessors(problem.getStartState()))

    queue = util.Queue()
    path = []
    checkedSpots = []
    currentState = problem.getStartState()

    queue.push([])
    end = False

    while not queue.isEmpty()and not problem.isGoalState(currentState):
        currentPath = queue.pop()
        if len(currentPath) != 0:
            currentState = currentPath[-1][0]

        new_path = []
        # print (currentState)
        if currentState not in checkedSpots:
            successors = problem.getSuccessors(currentState)

            for i in successors:
                #print (i)


                new_path = list(currentPath)
                if i[0] not in checkedSpots:
                    # print(i[0])
                    new_path.append(i)
                queue.push(new_path)
                if problem.isGoalState(i[0]):

                    #print ("GOAL!!!!!!!")
                    end = True
                    break
            checkedSpots.append(currentState)
        if end:
            break


    while not queue.isEmpty():
        currentState = queue.pop()[-1][0]
        if not problem.isGoalState(currentState) and currentState not in checkedSpots:
            problem.getSuccessors(currentState)

    for i in new_path:
        path.append(i[1])

    return path
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


def uniformCostSearch(problem):
    start = problem.getStartState()
    checkedSpots = []
    queue = util.PriorityQueue()
    queue.push((start, []), 0)
    while not queue.isEmpty():
        currentState, actions = queue.pop()
        if problem.isGoalState(currentState):
            break
        if currentState not in checkedSpots:
            successors = problem.getSuccessors(currentState)
            for i in successors:
                if i[0] not in checkedSpots:
                    directions = i[1]
                    newCost = actions + [directions]
                    queue.update((i[0], actions + [directions]), problem.getCostOfActions(newCost))
        checkedSpots.append(currentState)
    return actions
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    checkedSpots = []
    nQueue = util.PriorityQueue()
    nQueue.push((problem.getStartState(), []), 0)

    while not nQueue.isEmpty():
        currentState, actions = nQueue.pop()
        if problem.isGoalState(currentState):
            break
        if currentState not in checkedSpots:
            successors = problem.getSuccessors(currentState)
            for i in successors:
                if i[0] not in checkedSpots:
                    directions = i[1]
                    cost = actions + [directions]
                    nQueue.update((i[0], actions + [directions]), problem.getCostOfActions(cost) + heuristic(i[0], problem))
        checkedSpots.append(currentState)

    return actions
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
