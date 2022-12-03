
from queue import PriorityQueue
from car import Car
from gameboard import Gameboard
import re
import heapq
from heuristics import Heuristics

class UCS: 
    def shortestPath(root):
        h = []

        heapq.heappush(h, (0, root))
        path = []
        path.append(root)
        while len(h) !=0:
            current_cost, current_node = heapq.heappop(h)
            path.append(current_node)
            if current_node.state[2][5] == "A" and current_node.state[2][4] == "A":
                return path
            else:
                    for children in current_node.children:
                        heapq.heappush(h, (current_cost+children.cost, children.board))
        return path

class Greedy: 
    # algorithm for greedy search, takes in be default heuristics 1
    def greedy(root, heur="h1"):
        # track of visited nodes
        visited = set()  
        # GBFS traversal result
        greedy_traversal = list()
        # queue
        queue = PriorityQueue()

        # push the root node to the queue and mark it as visited 
        queue.put((0,root))
        visited.add(root)

        if ( heur == "h1"):
            # loop until queue empty 
            while not queue.empty(): 
                # take the first board from the queue and add it to the traversal list
                current_cost, current_node = queue.get()
                greedy_traversal.append(current_node)

                # update cost with heuristics 
                current_cost = Heuristics.h1(current_node.state)

                # if the current board is in a winning state, then return the bfs traversale
                if current_node.state[2][5] == "A" and current_node.state[2][4] == "A" :
                    return greedy_traversal
                # else, check the children of that node 
                else: 
                    for children in current_node.children:
                        # if the children node havent been visited yet
                        # push them onto the queue and mark them as visited 
                        if children.board not in visited:
                            visited.add(children.board)
                            children.setCost(Heuristics.h1(children.board.state))
                            queue.put((children.cost,children.board))
        elif (heur == "h2"):
            # loop until queue empty 
            while not queue.empty(): 
                # take the first board from the queue and add it to the traversal list
                current_cost, current_node = queue.get()
                greedy_traversal.append(current_node)

                # update cost with heuristics 
                current_cost = Heuristics.h2(current_node.state)

                # if the current board is in a winning state, then return the bfs traversale
                if current_node.state[2][5] == "A" and current_node.state[2][4] == "A" :
                    return greedy_traversal
                # else, check the children of that node 
                else: 
                    for children in current_node.children:
                        # if the children node havent been visited yet
                        # push them onto the queue and mark them as visited 
                        if children.board not in visited:
                            visited.add(children.board)
                            children.setCost(Heuristics.h2(children.board.state))
                            queue.put((children.cost,children.board))
        elif (heur == "h3"):
            # loop until queue empty 
            while not queue.empty(): 
                # take the first board from the queue and add it to the traversal list
                current_cost, current_node = queue.get()
                greedy_traversal.append(current_node)

                # update cost with heuristics 
                current_cost = Heuristics.h3(current_node.state)

                # if the current board is in a winning state, then return the bfs traversale
                if current_node.state[2][5] == "A" and current_node.state[2][4] == "A" :
                    return greedy_traversal
                # else, check the children of that node 
                else: 
                    for children in current_node.children:
                        # if the children node havent been visited yet
                        # push them onto the queue and mark them as visited 
                        if children.board not in visited:
                            visited.add(children.board)
                            children.setCost(Heuristics.h3(children.board.state,5))
                            queue.put((children.cost,children.board))
        
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
                print("queue size"+str(open.qsize()))
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
            
        return ValueError("There is no solution")