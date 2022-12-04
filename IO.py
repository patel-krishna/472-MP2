from search import UCS, Greedy, ASTAR
class IO:

    def writeSolSearch(board, puzzlenum):
        #CREATING TEXT FILE TO OUTPUT INFO FROM SEARCH ALGOS
        answerUCS, heuristicsUCS = UCS(board)
        fileSOL = "ucs-sol-" + str(1) + ".txt"
        with open(fileSOL,"w") as f:
            f.write("Inital Board configuration: ")
            for i in input_array:
                f.write(str(i))
            f.write('\n\n')
            f.write("Car Fuel available: " + str(origfuel) + "\n\n")
            f.write("Runtime: " + totalTime + "\n")
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
            file = "gbfs-" + i + "-sol-" + str(puzzlenum) + ".txt"
            with open(file,"w") as f:
                f.write("Inital Board configuration: ")
                for i in input_array:
                    f.write(str(i))
                f.write('\n\n')
                f.write("Car Fuel available: " + str(origfuel) + "\n\n")
                f.write("Runtime: " + totalTime + "\n")
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
        

        for i in heu:
            answerASTAR, heuristicsASTAR = ASTAR.astar(board, i)
            file = "a" + i + "-sol-" + str(puzzlenum) + ".txt"
            with open(file,"w") as f:
                f.write("Inital Board configuration: ")
                for i in input_array:
                    f.write(str(i))
                f.write('\n\n')
                f.write("Car Fuel available: " + str(origfuel) + "\n\n")
                f.write("Runtime: " + totalTime + "\n")
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