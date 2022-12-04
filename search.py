
from queue import PriorityQueue
from car import Car
from gameboard import Gameboard
import re
import heapq
from heuristics import Heuristics

#============UCS

class UCS: 

# The shortestPath function is a dikjstra model search algorithm which will 
# try to find the shortest path possible given a root node to a goal node 
# The function returns the path solution to the path as well as the heursitics of each node
    
    def shortestPath(root):
        h = []

        heapq.heappush(h, (0, root))
        ucs_path = []
        ucs_values = []

        ucs_path.append(root)
        while len(h) !=0:
            current_cost, current_node = heapq.heappop(h)
            ucs_path.append(current_node)
            ucs_values.append((current_cost, current_cost, 0))
            if current_node.state[2][5] == "A" and current_node.state[2][4] == "A":
                return ucs_path, ucs_values 
            else:
                    for children in current_node.children:
                        heapq.heappush(h, (current_cost+children.cost, children.board))
        return ucs_path, ucs_values

# ============GREEDY

class Greedy: 

    # The greedy algorithm is an algorithm that will find a search path
    # depending on the heuristic of each node in the following layer
    # it chooses the lowest value heuristic through a priority queue
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

        # push the root node to the queue and mark it as visited 
        queue.put((0,root))
        visited.add(root)

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
                    greedy_traversal, greedy_values
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
        
        return ValueError("There is no solution")


class ASTAR:
    # algorithm for astar, takes h1 as default heuristics 
    def astar(root, heur="h1"):
        open = PriorityQueue()
        closedset = set()
        path = []
        current = root

        open.put((current, 0))

        if (heur=="h1"):
            while not open.empty(): 
                # current_node, current_cost = min(openset, key=lambda o:o[0])
                current_node, current_cost = open.get()
                path.append(current_node)
                
                if current_node.state[2][5] == 'A' and current_node.state[2][4] == 'A':
                    return path 
                
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
                path.append(current_node)
                
                if current_node.state[2][5] == 'A' and current_node.state[2][4] == 'A':
                    path.append(current_node)
                    return path 
                
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
                path.append(current_node)
                
                if current_node.state[2][5] == 'A' and current_node.state[2][4] == 'A':
                    path.append(current_node)
                    return path 
                
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
                path.append(current_node)
                
                if current_node.state[2][5] == 'A' and current_node.state[2][4] == 'A':
                    path.append(current_node)
                    return path 
                
                # openset.remove((current_node, current_cost))
                closedset.add(current_node)

                for children in current_node.children:
                    if children.board not in closedset:
                        g_cost = (current_cost-Heuristics.h4(children.parent.state)) + children.cost
                        closedset.add(children.board)
                        f_cost = g_cost + Heuristics.h4(children.board.state)
                        open.put((children.board, f_cost))
            
        return ValueError("There is no solution")