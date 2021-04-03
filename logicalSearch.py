# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 12:37:16 2021

@author: Brandon Parker
"""

import nqueens


def schFunction(T, decayRate):
  return T * decayRate
  

def simulatedAnnealing(initBoard, decayRate, T_Threshold):
  current = initBoard
  T = 100

  while T > T_Threshold:
    current.h = nqueens.numAttackingQueens(current)
    T = schFunction(T, decayRate)
    suState = nqueens.getSuccessorStates(current)
    for x in suState:
      if(current.h > nqueens.numAttackingQueens(x)):
        current = x
  
  return current


def Main():
    for i in range(2, 5):
        print("********************\n", "Board Size: ", 2**i,
              "\n********************\n", "######################################\n",
              "Decay Rate: 0.9 T Threshold: 0.000001\n", "######################################")
        b = nqueens.Board(2**i)
        
        bhAvg = 0
        for j in range(1, 11):
            print("Run ", j)
            b.rand()
            print("Initial Board:")
            b.printBoard()
            b.h = nqueens.numAttackingQueens(b)
            print("Initial h-value: ", b.h)
            b = simulatedAnnealing(b, 0.9, 0.000001)
            print("Final Board:")
            b.printBoard()
            print("Final h-value: ", b.h, "\n")
            bhAvg = bhAvg + b.h
        bhAvg = bhAvg/10
        print("********************\n", "Average H-Value: ", bhAvg,
          "\n********************\n")
        print("######################################\n",
              "Decay Rate: 0.75 T Threshold: 0.0000001\n", "######################################")
        bhAvg = 0
        for j in range(1, 11):
            print("Run ", j)
            b.rand()
            print("Initial Board:")
            b.printBoard()
            b.h = nqueens.numAttackingQueens(b)
            print("Initial h-value: ", b.h)
            b = simulatedAnnealing(b, 0.75, 0.0000001)
            print("Final Board:")
            b.printBoard()
            print("Final h-value: ", b.h, "\n")
            bhAvg = bhAvg + b.h
        bhAvg = bhAvg/10
        print("********************\n", "Average H-Value: ", bhAvg,
          "\n********************\n")    
        print("######################################\n",
              "Decay Rate: 0.5 T Threshold: 0.00000001\n", "######################################")
        bhAvg = 0
        for j in range(1, 11):
            print("Run ", j)
            b.rand()
            print("Initial Board:")
            b.printBoard()
            b.h = nqueens.numAttackingQueens(b)
            print("Initial h-value: ", b.h)
            b = simulatedAnnealing(b, 0.5, 0.00000001)
            print("Final Board:")
            b.printBoard()
            print("Final h-value: ", b.h, "\n")
            bhAvg = bhAvg + b.h
        bhAvg = bhAvg/10
        print("********************\n", "Average H-Value: ", bhAvg,
          "\n********************\n")


if __name__ == '__main__':
    Main()