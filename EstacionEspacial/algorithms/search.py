from algorithms.problems import SearchProblem
import algorithms.utils as utils
from world.game import Directions
from algorithms.heuristics import nullHeuristic


def tinyDiagnosticSearch(problem: SearchProblem):
    """
    Returns a hard-coded sequence of moves for the tinyDiagnostic layout.
    For any other station layout, the sequence of moves will be incorrect.
    """
    s = Directions.SOUTH
    e = Directions.EAST
    return [s, e, s, e, e, e, e, s, e, e, s, s, e, s, s, e, s, e, e, e, e, e, e, e]


def depthFirstSearch(problem: SearchProblem):
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
    # TODO: Add your code here
    utils.raiseNotDefined()


def breadthFirstSearch(problem: SearchProblem):
    """
    Search the shallowest nodes in the search tree first.
    """
    # TODO: Add your code here
    utils.raiseNotDefined()


def uniformCostSearch(problem: SearchProblem):
    """
    Search the node of least total cost first.
    """

    # TODO: Add your code here
    """
    1. Versión inicial propia.
    
    nodoInicial = problem.getStartState()
    frontera = utils.PriorityQueue()
    utils.PriorityQueue.push(frontera, (nodoInicial, 0), 0)
    alcanzados = utils.Counter()
    
    while utils.PriorityQueue.isEmpty(frontera) is False:
        nodo = utils.PriorityQueue.pop(frontera)
        if problem.isGoalState(nodo[0]):
            return nodo[0]
        alcanzados[nodo[0]] += 1
        for hijo in problem.getSuccessors(nodo[0]):
            estadoHijo = hijo[0]
            costo = hijo[2] + nodo[1]
            if alcanzados[estadoHijo] == 0:
                utils.PriorityQueue.update(frontera, (estadoHijo, costo), costo)
    return None
    
    Al probarlo se obtenía un error en el método directionToVector de la clase Actions (archivo game).
    Tras revisar la implementación con ayuda de la IA con el propmt "Por qué con esta implementación 
    de UCS falla en el método directions de otra clase? (...)" Y se llegó a la conclusión de que era porque
    no se almacenaba una lista de acciones que llevaban a un nuevo estado.
    """
    #Versión final
    nodoInicial = problem.getStartState()
    frontera = utils.PriorityQueue()
    utils.PriorityQueue.push(frontera, (nodoInicial, [], 0), 0)
    alcanzados = utils.Counter()
    
    while utils.PriorityQueue.isEmpty(frontera) is False:
        nodo, acciones, costo = utils.PriorityQueue.pop(frontera)
        if problem.isGoalState(nodo):
            return acciones
        alcanzados[nodo] += 1
        for hijo in problem.getSuccessors(nodo):
            estadoHijo = hijo[0]
            accionHijo = hijo[1]
            costo = hijo[2] + costo
            if alcanzados[estadoHijo] == 0:
                utils.PriorityQueue.update(frontera, (estadoHijo, acciones+[accionHijo] , costo), costo)
    
    return None


def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """
    Search the node that has the lowest combined cost and heuristic first.
    """
    # TODO: Add your code here
    utils.raiseNotDefined()


# Abbreviations (you can use them for the -f option in main.py)
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
