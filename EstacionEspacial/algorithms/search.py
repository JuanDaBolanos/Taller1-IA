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
    utils.raiseNotDefined()


def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """
    Search the node that has the lowest combined cost and heuristic first.
    """
    nodo_inicio = problem.getStartState()
    frontera = utils.PriorityQueue()
    alcanzados = {}
    frontera.push(nodo_inicio, 0)
    padre_nodo_actual = None
    while not (frontera.isEmpty):
        nodo_actual = frontera.pop()
        g_nodo_actual = calcular_g(alcanzados, nodo_actual)
        alcanzados[nodo_actual] = {"padre":padre_nodo_actual, "f(n)":heuristic(nodo_actual, problem) + g_nodo_actual }
        if problem.isGoalState(nodo_actual):
            return calcular_camino_optimo(alcanzados, nodo_actual)
        
        
        sucesores_nodo_actual = SearchProblem.getSuccessors(nodo_actual)
        for sucesor in sucesores_nodo_actual:
            nodo_sucesor = sucesor[0]
            
            if nodo_sucesor not in alcanzados:
                costo_fn_nodo_actual = calcular_g() + heuristic(nodo_actual, problem)
                frontera.update(nodo_actual, costo_fn_nodo_actual)
                
            
            
        
        
        
        
    
    
    
    # TODO: Add your code here
    utils.raiseNotDefined()
    
def calcular_g(alcanzados, nodo_padre):
    #No estoy seguro del tipo del segundo parametro...
    g = 0
    while nodo_padre is not None:
        g+=1
        nodo_padre = alcanzados[nodo_padre]["padre"]
        
    return g+1

def alcular_camino_optimo(alcanzados, nodo_meta):
    #Reconstruye una lista con el camino desde el nodo meta hasta el origen
    camino = [nodo_meta]
    padre = alcanzados[nodo_meta]["padre"]
    while padre is not None:
        camino.append(padre)
    return camino
    



# Abbreviations (you can use them for the -f option in main.py)
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
