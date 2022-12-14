
from queue import PriorityQueue
import time
from car import Car
from gameboard import Gameboard
import re
import heapq
from heuristics import Heuristics

#============UCS

totalTime = 0

class UCS: 

# The shortestPath function is a dikjstra model search algorithm which will 
# try to find the shortest path possible given a root node to a goal node 
# The function returns the path solution to the path as well as the heursitics of each node
    
    def shortestPath(root):
        h = []

        heapq.heappush(h, (0, root))
        ucs_path = []
        ucs_values = []
  
        t0 = time.perf_counter()

        ucs_path.append(root)
        while len(h) !=0:
            current_cost, current_node = heapq.heappop(h)
            ucs_path.append(current_node)
            ucs_values.append((current_cost, current_cost, 0))
            if current_node.state[2][5] == "A" and current_node.state[2][4] == "A":
                t1 = time.perf_counter()
                totalTime = str(t1-t0)
                return ucs_path, ucs_values 
            else:
                    for children in current_node.children:
                        heapq.heappush(h, (current_cost+children.cost, children.board))

        t1 = time.perf_counter()
        totalTime = str(t1-t0)
        
        return ValueError("There is no solution")
        


# ============GREEDY

class Greedy: 

    # The greedy algorithm is an algorithm that will find a search path
    # depending on the heuristic of each node in the following layer
    # it chooses the lowest value heuristic through a priority queue
    # f(n) = h(n)
    # the algorithm takes in the root node and a heuristic string input
    # if no heurisitic choice is given, it will by default run h1

    def greedy(root, heur="h1"):
        # track of visited nodes
        visited = set()  
        # GBFS traversal result
        greedy_traversal = list()
        # queue
        queue = PriorityQueue()
        # heuristics for traversal path 
        greedy_values = list()
        global totalTime

        # push the root node to the queue and mark it as visited 
        queue.put((0,root))
        visited.add(root)
        t0 = time.perf_counter()

        if ( heur == "h1"):
            # loop until queue empty 
            while not queue.empty(): 
                # take the first board from the queue and add it to the traversal list
                current_cost, current_node = queue.get()
                greedy_traversal.append(current_node)
                greedy_values.append((current_cost, 0, current_cost))

                # update cost with heuristics 
                # current_cost = Heuristics.h1(current_node.state)

                # if the current board is in a winning state, then return the bfs traversale
                if current_node.state[2][5] == "A" and current_node.state[2][4] == "A" :
                    t1 = time.perf_counter()
                    totalTime = str(t1-t0)
                    return greedy_traversal, greedy_values
                # else, check the children of that node 
                else: 
                    for children in current_node.children:
                        # if the children node havent been visited yet
                        # push them onto the queue and mark them as visited 
                        if children.board not in visited:
                            visited.add(children.board)
                            # children.setCost(Heuristics.h1(children.board.state))
                            queue.put((Heuristics.h1(children.board.state),children.board))
        elif (heur == "h2"):
            # loop until queue empty 
            while not queue.empty(): 
                # take the first board from the queue and add it to the traversal list
                current_cost, current_node = queue.get()
                greedy_traversal.append(current_node)
                greedy_values.append((current_cost, 0, current_cost))

                # update cost with heuristics 
                # current_cost = Heuristics.h2(current_node.state)

                # if the current board is in a winning state, then return the bfs traversale
                if current_node.state[2][5] == "A" and current_node.state[2][4] == "A" :
                    t1 = time.perf_counter()
                    totalTime = str(t1-t0)
                    return greedy_traversal, greedy_values
                # else, check the children of that node 
                else: 
                    for children in current_node.children:
                        # if the children node havent been visited yet
                        # push them onto the queue and mark them as visited 
                        if children.board not in visited:
                            visited.add(children.board)
                            # children.setCost(Heuristics.h2(children.board.state))
                            queue.put((Heuristics.h2(children.board.state),children.board))
        elif (heur == "h3"):
            # loop until queue empty 
            while not queue.empty(): 
                # take the first board from the queue and add it to the traversal list
                current_cost, current_node = queue.get()
                greedy_traversal.append(current_node)
                greedy_values.append((current_cost, 0, current_cost))


                # update cost with heuristics 
                # current_cost = Heuristics.h3(current_node.state)

                # if the current board is in a winning state, then return the bfs traversale
                if current_node.state[2][5] == "A" and current_node.state[2][4] == "A" :
                    t1 = time.perf_counter()
                    totalTime = str(t1-t0)
                    return greedy_traversal, greedy_values
                # else, check the children of that node 
                else: 
                    for children in current_node.children:
                        # if the children node havent been visited yet
                        # push them onto the queue and mark them as visited 
                        if children.board not in visited:
                            visited.add(children.board)
                            # children.setCost(Heuristics.h3(children.board.state,5))
                            queue.put((Heuristics.h3(children.board.state,5),children.board))
        elif (heur == "h4"):
            # loop until queue empty 
            while not queue.empty(): 
                # take the first board from the queue and add it to the traversal list
                current_cost, current_node = queue.get()
                greedy_traversal.append(current_node)
                greedy_values.append((current_cost, 0, current_cost))

                # update cost with heuristics 
                # current_cost = Heuristics.h4(current_node.state)

                # if the current board is in a winning state, then return the bfs traversale
                if current_node.state[2][5] == "A" and current_node.state[2][4] == "A" :
                    t1 = time.perf_counter()
                    totalTime = str(t1-t0)
                    return greedy_traversal, greedy_values
                # else, check the children of that node 
                else: 
                    for children in current_node.children:
                        # if the children node havent been visited yet
                        # push them onto the queue and mark them as visited 
                        if children.board not in visited:
                            visited.add(children.board)
                            # children.setCost(Heuristics.h4(children.board.state))
                            queue.put((Heuristics.h4(children.board.state),children.board))
        
        t1 = time.perf_counter()
        totalTime = str(t1-t0)
        return ValueError("There is no solution")


# =============A/A*

class ASTAR:

    # astar algorithm takes in the root node of a graph and a heuristic input value 
    # if no heuristic string is given, it will by default run on heuristic of h1
    # the algorithm uses a priosity queue to choose the best node to traverse depending on the fn cost 
    # f(n) = g(n) + h(n)
    
    def astar(root, heur="h1"):
        open = PriorityQueue()
        closedset = set()
        astar_path = list()
        astar_values = list()
        current = root
        global totalTime

        open.put((current, 0))
        t0 = time.perf_counter()    

        if (heur=="h1"):
            while not open.empty(): 
                # current_node, current_cost = min(openset, key=lambda o:o[0])
                current_node, current_cost = open.get()
                astar_path.append(current_node)
                fn = current_cost
                hn = Heuristics.h1(current_node.state)
                gn = fn-hn 
                if(gn<0):
                    astar_values.append((fn, 0, hn))
                else:
                    astar_values.append((fn, gn, hn))
                
                if current_node.state[2][5] == 'A' and current_node.state[2][4] == 'A':
                    t1 = time.perf_counter()
                    totalTime = str(t1-t0)
                    return astar_path, astar_values
                
                # openset.remove((current_node, current_cost))
                closedset.add(current_node)

                for children in current_node.children:
                    if children.board not in closedset:
                        g_cost = (current_cost-Heuristics.h1(children.parent.state)) + children.cost
                        closedset.add(children.board)
                        f_cost = g_cost + Heuristics.h1(children.board.state)
                        open.put((children.board, f_cost))
        elif(heur == "h2"):
            while not open.empty(): 
                # current_node, current_cost = min(openset, key=lambda o:o[0])
                current_node, current_cost = open.get()
                astar_path.append(current_node)
                fn = current_cost
                hn = Heuristics.h2(current_node.state)
                gn = fn-hn 
                if(gn<0):
                    astar_values.append((fn, 0, hn))
                else:
                    astar_values.append((fn, gn, hn))
                
                if current_node.state[2][5] == 'A' and current_node.state[2][4] == 'A':
                    # astar_path.append(current_node)
                    t1 = time.perf_counter()
                    totalTime = str(t1-t0)
                    return astar_path, astar_values 
                
                # openset.remove((current_node, current_cost))
                closedset.add(current_node)

                for children in current_node.children:
                    if children.board not in closedset:
                        g_cost = (current_cost-Heuristics.h2(children.parent.state)) + children.cost
                        closedset.add(children.board)
                        f_cost = g_cost + Heuristics.h2(children.board.state)
                        open.put((children.board, f_cost))
        
        elif(heur == "h3"):
            while not open.empty(): 
                # current_node, current_cost = min(openset, key=lambda o:o[0])
                current_node, current_cost = open.get()
                astar_path.append(current_node)
                fn = current_cost
                hn = Heuristics.h3(current_node.state)
                gn = fn-hn 
                if(gn<0):
                    astar_values.append((fn, 0, hn))
                else:
                    astar_values.append((fn, gn, hn))
                
                if current_node.state[2][5] == 'A' and current_node.state[2][4] == 'A':
                    # astar_path.append(current_node)
                    t1 = time.perf_counter()
                    totalTime = str(t1-t0)
                    return astar_path, astar_values
                
                # openset.remove((current_node, current_cost))
                closedset.add(current_node)

                for children in current_node.children:
                    if children.board not in closedset:
                        g_cost = (current_cost-Heuristics.h3(children.parent.state,5)) + children.cost
                        closedset.add(children.board)
                        f_cost = g_cost + Heuristics.h3(children.board.state,5)
                        open.put((children.board, f_cost))
        elif(heur == "h4"):
            while not open.empty(): 
                # current_node, current_cost = min(openset, key=lambda o:o[0])
                current_node, current_cost = open.get()
                astar_path.append(current_node)
                fn = current_cost
                hn = Heuristics.h4(current_node.state)
                gn = fn-hn 
                if(gn<0):
                    astar_values.append((fn, 0, hn))
                else:
                    astar_values.append((fn, gn, hn))
                
                if current_node.state[2][5] == 'A' and current_node.state[2][4] == 'A':
                    # astar_path.append(current_node)
                    t1 = time.perf_counter()
                    totalTime = str(t1-t0)
                    return astar_path, astar_values
                
                # openset.remove((current_node, current_cost))
                closedset.add(current_node)

                for children in current_node.children:
                    if children.board not in closedset:
                        g_cost = (current_cost-Heuristics.h4(children.parent.state)) + children.cost
                        closedset.add(children.board)
                        f_cost = g_cost + Heuristics.h4(children.board.state)
                        open.put((children.board, f_cost))
        
        t1 = time.perf_counter()
        totalTime = str(t1-t0)    
        return ValueError("There is no solution")