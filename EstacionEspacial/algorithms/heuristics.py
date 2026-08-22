from typing import Tuple
from algorithms import utils
from algorithms.problems import SystemRepairProblem
import math

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def manhattanHeuristic(state, problem):
    """
    The Manhattan distance heuristic.

    Baseline rule for this workshop: estimate the direct distance to the next
    mandatory target:
    - K if the robot does not have the kit yet.
    - the nearest pending T if the robot has the kit and systems remain.
    - C if all systems have been repaired.
    """
    hasKit = state[2]
    if not hasKit:
        posKit = problem.kitPosition
        x_cordinate = posKit[0]
        y_cordinate = posKit[1]
    
    elif  len(problem.systemPositions) == 0:
        control_pos = problem.controlPosition
        x_cordinate = control_pos[0]
        y_cordinate = control_pos[1]
    else:
        smallest_manhattan = math.inf
        for cord in state[2]:
            x_cordinate = cord[0]
            y_cordinate = cord[1]
            
            new_manhattan = abs(state[0][0] - x_cordinate) + abs(state[0][1] - y_cordinate)
            if (new_manhattan<smallest_manhattan):
                smallest_manhattan = new_manhattan
        return smallest_manhattan
            
    



    return abs(state[0][0] - x_cordinate) + abs(state[0][1] - y_cordinate)
    #utils.raiseNotDefined()


def euclideanHeuristic(state, problem):
    """
    The Euclidean distance heuristic.

    Baseline rule for this workshop: estimate the direct distance to the next
    mandatory target:
    - K if the robot does not have the kit yet.
    - the nearest pending T if the robot has the kit and systems remain.
    - C if all systems have been repaired.
    """
    # TODO: Add your code here
    utils.raiseNotDefined()


def systemRepairHeuristic(
    state: Tuple[Tuple, bool, Tuple], problem: SystemRepairProblem
):
    """
    Your heuristic for the SystemRepairProblem.

    state: (position, hasKit, pendingSystems)
    problem: SystemRepairProblem instance

    This must be admissible and preferably consistent.

    Hints:
    - Use problem.heuristicInfo to cache expensive computations
    - Go with some simple heuristics first, then build up to more complex ones
    - Consider the kit, pending systems, and the final return to control center
    - Balance heuristic strength vs. computation time (do experiments!)
    """
    # TODO: Add your code here
    utils.raiseNotDefined()
