import heapq
import math
import sys
from pdb import Restart
import random
import ReadCSV as csv
from Board import Board
from queue import PriorityQueue
from copy import deepcopy
import time
import UD
import fourD
import HillClimbing as HC

while True:
    print("Please choose a mode to run:")
    print("UDA for Vertical Only A Star")
    print("UDG for Vertical Only Greedy")
    print("4DA for Four Directions A Star")
    print("4DG for Four Directions Greedy")
    print("HC for Vertical Only Hill Climbing")
    print("HC4D for Four Directions Hill Climbing")
    print("Q to quit")
    mode = input("Type the mode now:")

    if mode == "Q":
        break

    print()
    file = input("Input the filename to run(press Enter to Run board.csv): ")
    print()
    if file == "":
        file = "board.csv"

    initialBoard = csv.readCSV(file)

    if (mode == "UDA"):
        print("Vertical Only A Star")
        st, nextBoard, nodeCount, level, cost = UD.aStar(initialBoard)
        UD.printResults(st, nextBoard, nodeCount, level, cost)

    elif (mode == "UDG"):
        print("Vertical Only Greedy")
        st, nextBoard, nodeCount, level, cost = UD.greedy(initialBoard)
        UD.printResults(st, nextBoard, nodeCount, level, cost)

    elif (mode == "4DA"):
        print("Four Directions A Star")
        st, nextBoard, nodeCount, level, cost = fourD.aStar4D(initialBoard)
        UD.printResults(st, nextBoard, nodeCount, level, cost)

    elif (mode == "4DG"):
        print("Four Directions Greedy")
        st, nextBoard, nodeCount, level, cost = fourD.greedy4D(initialBoard)
        UD.printResults(st, nextBoard, nodeCount, level, cost)

    elif (mode == "HC"):
        print("Vertical Only Hill Climbing")
        HC.hillClimb(initialBoard)

    elif (mode == "HC4D"):
        print("Four Directions Hill Climbing")
        HC.hillClimb4D(initialBoard)

    else:
        print("Mode not recognized")

    print()
    print()