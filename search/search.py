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
from multiprocessing import Queue
from inspect import stack
from game import Directions

import util
"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

#from util import Queue

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
    """

    x = problem.getStartState()
   # print "start state is " + str(problem)
    visitedSet = [x]
    internalSuccessors = []
    path = []
    parent = {}
    stacked_list = []
    result = []
    start_state = ''
   
    setOfSuccessors = problem.getSuccessors(x)
    start_State = (x, Directions.STOP, 0)
    
    parent[start_State]= None
    
    
    for i in setOfSuccessors:
        parent[i] = start_State
    while setOfSuccessors:
        anothervar =  setOfSuccessors.pop()
        current = anothervar[0]
        currentPath  = anothervar[1]
        
        if current in visitedSet:
            continue
        if problem.isGoalState(current):
           stacked_list = pushOnStack(start_State, anothervar, parent, [])
           for i in reversed(stacked_list):
               result.append(i[1])
           return result
        visitedSet.append(current)
        path.append(currentPath)
        internalSuccessors = problem.getSuccessors(current)
        for i in internalSuccessors:
            parent[i] = anothervar
            setOfSuccessors.append(i)
            #print str(i) + "parent is : " + str(anothervar)
        
    


    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()
    
def pushOnStack(start, goal, parent, some_list):
           if parent[goal]!=None :
             #print "abhishek " + str(goal)
             some_list.append(goal)
             pushOnStack(start, parent[goal], parent, some_list)
           return some_list;
       
def pushOnStackUCS(start, goal, parent, some_list):
    if parent[goal]!=None :
             #print "abhishek " + str(goal)
             some_list.append(goal)
             pushOnStack(start, parent[goal], parent, some_list)
    return some_list;
        

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    x = problem.getStartState()
    internalSuccessors = []
    path = []
    parent = {}
    stacked_list = []
    result = []
    start_state = ''
    queue= util.Queue()
    visitedSet =[x]
    initial_successors = problem.getSuccessors(x)
    for i in initial_successors :
        queue.push(i)
    start_State = (x, Directions.STOP, 0)
    
    parent[start_State]= None
    for i in initial_successors:
        #print i
        parent[i] = start_State
    while queue:
        anothervar =  queue.pop()
        current = anothervar[0]
        currentPath  = anothervar[1]
        
        if current in visitedSet:
            continue
        if problem.isGoalState(current):
           stacked_list = pushOnStack(start_State, anothervar, parent, [])
           for i in reversed(stacked_list):
               result.append(i[1])
           return result
        visitedSet.append(current)
        path.append(currentPath)
        internalSuccessors = problem.getSuccessors(current)
        for i in internalSuccessors:
            if i[0] in visitedSet:
                continue;
            parent[i] = anothervar
            queue.push(i)
    
    util.raiseNotDefined()

def uniformCostSearch(problem):
    x = problem.getStartState()
   # print "start state is " + str(problem)
   
    internalSuccessors = []
    path = []
    parent_list = []
    initial_successors = []
    parent = {}
    stacked_list = []
    result = []
    prior_dict = {}
    visitedSet = [x]
    queue= util.PriorityQueue()
    oneLevel = []
    start_State = (x, Directions.STOP, 0)
    prior_dict[start_State] = start_State[2]
    parent[start_State] = None
    
    for i in problem.getSuccessors(x) :
        prior_dict[i] = i[2]
        queue.push(i, prior_dict[i])
        parent[i] = start_State
    while queue:
        anothervar =  queue.pop()
        current = anothervar[0]
        currentPath  = anothervar[1]
        if current in visitedSet:
            continue
        if problem.isGoalState(current):
            stacked_list = pushOnStackUCS(start_State, anothervar, parent, [])
            for i in reversed(stacked_list):
               result.append(i[1])
            return result
        visitedSet.append(current)
        internalSuccessors = problem.getSuccessors(current)
        for i in internalSuccessors:
            if i[0] in visitedSet:
                continue
            parent[i] = anothervar
            prior_dict[i] = i[2] + prior_dict[anothervar]
            queue.push(i, prior_dict[i])
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
    x = problem.getStartState()
   # print "start state is " + str(problem)
   
    internalSuccessors = []
    path = []
    parent_list = []
    initial_successors = []
    parent = {}
    stacked_list = []
    result = []
    prior_dict = {}
    visitedSet = [x]
    queue= util.PriorityQueue()
    oneLevel = []
    start_State = (x, Directions.STOP, 0)
    prior_dict[start_State] = start_State[2] 
    parent[start_State] = None
    
    for i in problem.getSuccessors(x) :
        prior_dict[i] = i[2] 
        queue.push(i, prior_dict[i] + heuristic(i[0], problem))
        parent[i] = start_State
    while queue:
        anothervar =  queue.pop()
        current = anothervar[0]
        currentPath  = anothervar[1]
        if current in visitedSet:
            continue
        if problem.isGoalState(current):
            stacked_list = pushOnStackUCS(start_State, anothervar, parent, [])
            for i in reversed(stacked_list):
               result.append(i[1])
            return result
        visitedSet.append(current)
        internalSuccessors = problem.getSuccessors(current)
        for i in internalSuccessors:
            if i[0] in visitedSet:
                continue
            parent[i] = anothervar
            prior_dict[i] = i[2] + prior_dict[anothervar]
            queue.push(i, prior_dict[i] + heuristic(i[0], problem))
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
