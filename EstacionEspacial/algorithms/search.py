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
    """
    IDEA PROPIA:
    Lo que se hace es inicializar las estructuras de control. Particularmente la frontera se inicializa con el primer estado y su camino vacio.
    Note que decidimos que cada elemento de la frontera tenga la forma (estado,lista_camino->[accion1,accion2,accion3]) de esta forma se hace sencillo trazar el camino,
    añadir nuevas acciones, y retornarlo en caso de que estemos en el estado meta.
    El resto del algoritmo es bastante fiel a las implementaciones clasicas como las aprendidas en EDA.
    
    alcanzados = utils.Counter()
    frontera = utils.Stack()
    inicial = (problem.getStartState(),[]) 
    frontera.push(inicial)
    while frontera.isEmpty() != True:
        v,camino = frontera.pop()
        alcanzados[v] = 1
        if problem.isGoalState(v):
            return camino
        for elemento_vecino in problem.getSuccessors(v):
            vecino = elemento_vecino[0]
            accion = elemento_vecino[1]
            if alcanzados[vecino] == 0:
                frontera.push((vecino,camino + [accion]))
    return []
    
    
    
    """
    alcanzados = utils.Counter()
    frontera = utils.Stack()
    inicial = (problem.getStartState(),[]) 
    frontera.push(inicial)
    while frontera.isEmpty() != True:
        v,camino = frontera.pop()
        if alcanzados[v] == 1: #Con ayuda de la IA introducimos esta verificación para evitar expandir
            continue           #un estado en la frontera multiples veces desde diferentes estados.
        alcanzados[v] = 1
        if problem.isGoalState(v):
            return camino
        for elemento_vecino in problem.getSuccessors(v):
            vecino = elemento_vecino[0]
            accion = elemento_vecino[1]
            if alcanzados[vecino] == 0:
                frontera.push((vecino,camino + [accion]))
    return []


def breadthFirstSearch(problem: SearchProblem):
    """
    Search the shallowest nodes in the search tree first.
    """
    # TODO: Add your code here
    
    """
    1. Versión inicial propia
    
    nodoInicial = problem.getStartState()
    if problem.isGoalState(nodoInicial):
        return nodoInicial
    
    frontera = utils.Queue()
    utils.Queue.push(frontera, (nodoInicial, '', 0))
    alcanzados = utils.Counter() 
    alcanzados[nodoInicial] = 1
    
    while utils.Queue.isEmpty(frontera) is False:
        nodo, acciones, costo = utils.Queue.pop(frontera)
        for hijo in problem.getSuccessors(nodo):
            estadoHijo = hijo[0]
            accionesHijo = hijo[1]
            costoHijo = hijo[2]
            
            if problem.isGoalState(hijo):
                return accionesHijo
            if alcanzados[estadoHijo] == 0:
                alcanzados[estadoHijo] += 1
                utils.Queue.push(frontera, (estadoHijo, accionesHijo, costoHijo))
    return None
    
    Al ejecutar la función de manera visual, el robot no se desplazaba y en una ejecución de terminal inmediata
    realizaba la expansión de todos los nodos pero retornando un camino de coste 0 (es decir, sin alguna acción).
    Esto debido a que no había guardado las acciones de alguna manera tal que al final el retorno sea el camino mediante
    las acciones. 
    Para ello, utilicé el siguiente prompt en Claude más mi versión inicial y la definición de algunas funciones:
    
    "Tengo esta función de BFS implementada para un espacio de estados. 
    Se trata sobre un robot que se desplaza en las cuatro direcciones y busca en un laberinto de obstaculos. 
    Tengo un problema en el que el robot permanece inmovil al ejecutar el programa y por ende no se puede encontrar el camino. 
    Cuál podría ser la causa de dicho problema?"
    
    Me realizó las siguientes correciones:
    - Bug en if problem.isGoalState(hijo): -> if problem.isGoalState(estadoHijo):
    - Bug en utils.Queue.push(frontera, (estadoHijo, accionesHijo, costoHijo)) -> utils.Queue.push(frontera, (estadoHijo, acciones + [accionesHijo], costoHijo)):
    - utils.Queue.push(frontera, (nodoInicial, ' ', 0)) -> utils.Queue.push(frontera, (nodoInicial, [], 0))
    
    Con estos cambios la función se ejecutaba correctamente y retornaba el camino esperado. Aprendí con esto que
    es necesario guardar las acciones de manera acumulada en alguna estructura de datos tal que al final este sea
    el resultado y podamos obtener el camino desde dicha estructura. 
    
    
    """
    #Version final
    nodoInicial = problem.getStartState()
    if problem.isGoalState(nodoInicial):
        return nodoInicial
    
    frontera = utils.Queue()
    utils.Queue.push(frontera, (nodoInicial, [], 0))
    alcanzados = utils.Counter() 
    alcanzados[nodoInicial] = 1
    
    while utils.Queue.isEmpty(frontera) is False:
        nodo, acciones, costo = utils.Queue.pop(frontera)
        for hijo in problem.getSuccessors(nodo):
            estadoHijo = hijo[0]
            accionHijo = hijo[1]
            costoHijo = hijo[2]
            
            if problem.isGoalState(estadoHijo):
                return acciones + [accionHijo]
            if alcanzados[estadoHijo] == 0:
                alcanzados[estadoHijo] += 1
                utils.Queue.push(frontera, (estadoHijo, acciones + [accionHijo], costoHijo))
    return None



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
    
    2. Version corregida
    
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
    
    Al probar esta nueva implementación el algoritmo de búsqueda corría completamente. Sin embargo, revisando
    nuevamente se descubrió un error que hacía que el costo del camino encontrado no fuera el más óptimo y que
    se expandieran más nodos de los necesarios, debido a que la variable costo se actualizaba en cada sucesor 
    con el mismo estado y que un nodo alcanzado se guardaba nuevamente si tenía un costo diferente.
    
    """
    #Versión final
    nodoInicial = problem.getStartState()
    frontera = utils.PriorityQueue()
    frontera.push((nodoInicial, [], 0), 0)
    alcanzados = utils.Counter()
    alcanzados[nodoInicial] = 0
    
    while frontera.isEmpty() is False:
        nodo, acciones, costo = frontera.pop()
        
        if problem.isGoalState(nodo):
            return acciones
        
        for hijo in problem.getSuccessors(nodo):
            estadoHijo = hijo[0]
            accionHijo = hijo[1]
            costoHijo = hijo[2] + costo
            if alcanzados[estadoHijo] == 0 or costoHijo < alcanzados[estadoHijo]:
                alcanzados[estadoHijo] = costoHijo
                utils.PriorityQueue.update(frontera, (estadoHijo, acciones+[accionHijo] , costoHijo), costoHijo)
    
    return None


def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """
    Search the node that has the lowest combined cost and heuristic first.
    """
    """
    Version incial:
    start_state = problem.getStartState()
    frontera = utils.PriorityQueue()
    alcanzados = {}
    frontera.push(nodo_inicio, 0)
    padre_nodo_actual = None
    
    while not (frontera.isEmpty()):
        nodo_actual, acciones, g_actual = frontera.pop()
        #nodo_actual = frontera.pop()
        g_nodo_actual = calcular_g(alcanzados, nodo_actual)
        alcanzados[nodo_actual] = {"padre":padre_nodo_actual, "f(n)":heuristic(nodo_actual, problem) + g_nodo_actual }
        if problem.isGoalState(nodo_actual):
            return calcular_camino_optimo(alcanzados, nodo_actual)
            
        sucesores_nodo_actual = problem.getSuccessors(nodo_actual)
        for sucesor in sucesores_nodo_actual:
            nodo_sucesor = sucesor[0]
            
            if nodo_sucesor not in alcanzados:
                costo_fn_nodo_actual = calcular_g() + heuristic(nodo_actual, problem)
                frontera.update(nodo_actual, costo_fn_nodo_actual)
                
    def calcular_camino_optimo(alcanzados, nodo_meta):
    #Reconstruye una lista con el camino desde el nodo meta hasta el origen
    camino = [nodo_meta]
    padre = alcanzados[nodo_meta]["padre"]
    while padre is not None:
        camino.append(padre)
    return camino
                
    1. El principal error que la IA encontro en este codigo es que estaba
    retornando una lista de estados en lugar de una lista de acciones.
    
    2. Ademas, la IA me ayudo a comprender mejor la estrucutra del problem
    
    3. Por ultimo, guardar una lista indicando el camino en cada nodo
    resulto ser una solucion mas limpia para retornar el resultado
                         
    """
    #print("Start:", problem.getStartState())
    #print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    #print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    start_state = problem.getStartState()
    
    frontera = utils.PriorityQueue()
    
    frontera.push((start_state, [], 0), heuristic(start_state, problem))
    
    alcanzados = {}
    
    while not frontera.isEmpty():
        nodo_actual, acciones, g_actual = frontera.pop()
        
        if problem.isGoalState(nodo_actual):
            return acciones
        
        
        if nodo_actual in alcanzados and alcanzados[nodo_actual] <= g_actual:
            continue
            
        alcanzados[nodo_actual] = g_actual
        
        for sucesor, accion, costo_paso in problem.getSuccessors(nodo_actual):
            nuevo_g = g_actual + costo_paso
            nuevo_f = nuevo_g + heuristic(sucesor, problem)
            
            if sucesor not in alcanzados or alcanzados[sucesor] > nuevo_g:
                frontera.push((sucesor, acciones + [accion], nuevo_g), nuevo_f)
                
    return []
    
def calcular_g(alcanzados, nodo_padre):
    #No estoy seguro del tipo del segundo parametro...
    g = 0
    while nodo_padre is not None:
        g+=1
        nodo_padre = alcanzados[nodo_padre]["padre"]
        
    return g+1


    



# Abbreviations (you can use them for the -f option in main.py)
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
