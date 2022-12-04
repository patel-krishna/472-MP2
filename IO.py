from search import *
from queue import PriorityQueue
from car import Car
from gameboard import Gameboard
import re
import heapq
from heuristics import Heuristics
from search import *
from IO import *

class IO:

    def writeSolSearch(input_array ,board, puzzlenum, carFuel, output_directory):
        #CREATING TEXT FILE TO OUTPUT INFO FROM SEARCH ALGOS
        answerUCS, heuristicsUCS = UCS.shortestPath(board)
        fileSOL = "ucs-sol-" + str(1) + ".txt"
        with open(fileSOL,"w") as f:
            print("opened file")
            f.write("Inital Board configuration: ")
            for i in input_array:
                f.write(str(i))
            f.write('\n\n')
            f.write("Car Fuel available: " + str(carFuel) + "\n\n")
            f.write("Runtime: " + str(totalTime) + "\n")
            f.write("Solution Path length: " + str(len(board.children)) + "\n")
            f.write("Search Path length: " + str(len(answerUCS)) + "\n")
            f.write("Solution Path: " + str(board.path) + "\n")
        f.close()
        fileSEARCH = "ucs-search.txt"
        with open(fileSEARCH,"w") as f:
            temp = 0
            for i in heuristicsUCS:
                f.write(str(i) + " ")
                f.write(str(answerUCS[temp].state))
                f.write(" " + (str(board.currentFuel[temp])))
                f.write("\n\n")
                temp += 1
        f.close()
            
        heu = ["h1", "h2", "h3", "h4"]
        for i in heu:
            answerGREEDY, heuristicsGREEDY = Greedy.greedy(board, i) 
            fileSOL = "gbfs-" + i + "-sol-" + str(puzzlenum) + ".txt"
            with open(fileSOL,"w") as f:
                f.write("Inital Board configuration: ")
                for inp in input_array:
                    f.write(str(inp))
                f.write('\n\n')
                f.write("Car Fuel available: " + str(carFuel) + "\n\n")
                f.write("Runtime: " + str(totalTime) + "\n")
                f.write("Solution Path length: " + str(len(board.children)) + "\n")
                f.write("Search Path length: " + str(len(answerGREEDY)) + "\n")
                f.write("Solution Path: " + str(board.path) + "\n")
                f.write('\n\n')
                temp = 0 
                for move in board.path:
                    f.write(move + "  ")
                    f.write(str(board.currentState[temp]) + " ")
                    f.write(str(board.currentFuel[temp]))
                    f.write("\n")
                    temp+=1
            f.close()
            fileSEARCH = "gbfs-" + i + "-search.txt"
            with open(fileSEARCH,"w") as f:
                temp = 0
                for h in heuristicsGREEDY:
                    f.write(str(h) + " ")
                    f.write(str(answerGREEDY[temp].state))
                    f.write(" " + (str(board.currentFuel[temp])))
                    f.write("\n\n")
                    temp += 1
            f.close()
        

        for i in heu:
            answerASTAR, heuristicsASTAR = ASTAR.astar(board, i)
            fileSOL = "a" + i + "-sol-" + str(puzzlenum) + ".txt"
            with open(fileSOL,"w") as f:
                f.write("Inital Board configuration: ")
                for inp in input_array:
                    f.write(str(inp))
                f.write('\n\n')
                f.write("Car Fuel available: " + str(carFuel) + "\n\n")
                f.write("Runtime: " + str(totalTime) + "\n")
                f.write("Solution Path length: " + str(len(board.children)) + "\n")
                f.write("Search Path length: " + str(len(answerASTAR)) + "\n")
                f.write("Solution Path: " + str(board.path) + "\n")
                f.write('\n\n')
                temp = 0 
                for move in board.path:
                    f.write(move + "  ")
                    f.write(str(board.currentState[temp]) + " ")
                    f.write(str(board.currentFuel[temp]))
                    f.write("\n")
                    temp+=1
            f.close()
            fileSEARCH = "a-" + i + "-search.txt"
            with open(fileSEARCH,"w") as f:
                temp = 0
                for h in heuristicsASTAR:
                    f.write(str(h) + " ")
                    f.write(str(answerUCS[temp].state))
                    f.write(" " + (str(board.currentFuel[temp])))
                    f.write("\n\n")
                    temp += 1
                f.close()

    def writeCSV(input_array ,board, puzzlenum):
        with open('C:\\Users\\Krish\\.vscode\\472-MP2\\Output\\spreadsheet.csv', 'a') as fd:
            answerUCS, heuristicsUCS = UCS.shortestPath(board)
            fd.write(str(puzzlenum) +","+"UCS"+","+"NA,"+str(len(board.children))+","+str(len(answerUCS))+str(totalTime)+"\n")
            heu = ["h1", "h2", "h3", "h4"]
            for i in heu:
               answerGREEDY, heuristicsGREEDY = Greedy.greedy(board, i) 
               fd.write(str(puzzlenum) +","+"GBFS,"+i+","+str(len(board.children))+","+str(len(answerGREEDY))+str(totalTime)+"\n")
            for i in heu:
                answerASTAR, heuristicsASTAR = ASTAR.astar(board, i)
                fd.write(str(puzzlenum) +","+"A/A*,"+i+","+str(len(board.children))+","+str(len(answerASTAR))+str(totalTime)+"\n")

                


        