
# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
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
     Returns the start state for the search problem 
     """
     util.raiseNotDefined()
    
  def isGoalState(self, state):
     """
       state: Search state
    
     Returns True if and only if the state is a valid goal state
     """
     util.raiseNotDefined()

  def getSuccessors(self, state):
     """
       state: Search state
     
     For a given state, this should return a list of triples, 
     (successor, action, stepCost), where 'successor' is a 
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental 
     cost of expanding to that successor
     """
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
     """
      actions: A list of actions to take
 
     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
     """
     util.raiseNotDefined()
           

def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]


class Node:
    def __init__(self, state, parent, move , movecost):
        self.state  = state
        self.parent = parent
        self.move = move
        if parent==None:
            self.cost = movecost
        else:
            self.cost = parent.cost + movecost

    def __str__(self):
        return "State: " + str(self.state) + "\n" + \
               "Parent: " + str(self.parent.state) + "\n" + \
               "Move: " + str(self.move) + "\n" + \
               "Cost: " + str(self.cost)

    def getState(self):
        return self.state

    def getParent(self):
        return self.parent

    def getMove(self):
        return self.move

    def getCost(self):
        return self.cost

    def pathFromStart(self):
        stateList = []
        moveList = []
        current = self
        while current.getMove() is not None:
            #print stateList
            print moveList
            stateList.append(current.getState())
            moveList.append(current.getMove())
            current = current.parent
        moveList.reverse()
        return moveList




def depthFirstSearch(problem):
  """
  Search the deepest nodes in the search tree first
  [2nd Edition: p 75, 3rd Edition: p 87]
  
  Your search algorithm needs to return a list of actions that reaches
  the goal.  Make sure to implement a graph search algorithm 
  [2nd Edition: Fig. 3.18, 3rd Edition: Fig 3.7].
  
  To get started, you might want to try some of these simple commands to
  understand the search problem that is being passed in:
  
  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  """

  stack = util.Stack()
  explored = []
  start = Node(problem.getStartState(), None, None, 0)
  stack.push(start)
  moves = []

  while (not stack.isEmpty()):
      
      current = stack.pop()
      explored.append(current.getState())
      if problem.isGoalState(current.getState()):
          print "done"
          return current.pathFromStart()
      else:
          successors = problem.getSuccessors(current.getState())
          for item in successors:
              state = item[0]
              action = item[1]
              stepcost = item[2]
              if state not in explored:
                  stack.push( Node(state, current, action, stepcost) )
  util.raiseNotDefined()

def breadthFirstSearch(problem):

  stack = util.Queue()
  explored = []
  start = Node(problem.getStartState(), None, None, 0)
  stack.push(start)
  moves = []

  while (not stack.isEmpty()):
  #for i in range(3):
      current = stack.pop()
      #explored[current.getState()] = 1
      temp = current.getState()  
      explored.append(temp)
      #print "current", current.getState()
      if problem.isGoalState(current.getState()):
          print "done"
          return current.pathFromStart()
      else:
          successors = problem.getSuccessors(current.getState())
          for item in successors:
              state = item[0]
              action = item[1]
              stepcost = item[2]
              if state not in explored:
                  stack.push( Node(state, current, action, stepcost) )
  util.raiseNotDefined()
      


def uniformCostSearch(problem):

    util.raiseNotDefined()


def aStarSearch(problem, heuristic):
    util.raiseNotDefined()
  

    
  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

