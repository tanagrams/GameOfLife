import random
import numpy as np
import time

import pygame
import pygame as py

WIDTH = 5
HEIGHT = 5
MARGIN = 1

DIMENSION = 100


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)


py.init()

WIN_SIZE = (600, 600)

screen = py.display.set_mode(WIN_SIZE)
py.display.set_caption("Conways Game of Life")

clock = py.time.Clock()


def dead_state(width, height):
    #dead_state is a function that creates an array containing 0's of given size
    #Input: Width of the array
    #       Height of the array
    #Output: Returns an array of 0's
    board = (np.zeros((width, height), dtype=int))

    return board

def random_state(width, height):
    # random_state is a function that creates an array containing 0's of given size
    # Input: Width of the array
    #       Height of the array
    # Output: Returns an array of 1 and 0 in random order

    board = dead_state(width, height)

    for r in range(height - 1):
        for c in range (width - 1):
            board[r][c] = random.randint(0, 1)
    #render(board)
    return board

def count_neighbours(board, r, c):
    count = 0

    for i in range(-1, 2):
            for j in range(-1, 2):
                r_offset = i
                c_offset = j
                if 0 <= (r + r_offset) < len(board) and 0 <= (c + c_offset) < len(board[0]) and board[r+r_offset][c+c_offset] == 1:
                    count += 1

    return count


def next_board_state(board):
    old_board = board
    new_board = dead_state(len(board), len(board[0]))

    for r in range(0, len(board)):
        for c in range(0, len(board[0])):
            current_cell = old_board[r][c]


            if current_cell == 1:
                neighbours = count_neighbours(old_board, r, c) - 1
                if neighbours <= 1:
                    current_cell = 0
                elif neighbours > 3:
                    current_cell = 0
            elif current_cell == 0:
                neighbours = count_neighbours(old_board, r, c)
                if neighbours == 3:
                    current_cell = 1

            new_board[r][c] = current_cell


    return new_board



def render(board):
    #Prints 2d array
    #print(np.matrix(board))
    rows = len(board)
    col = len(board[0])

    for r in range(rows):
        for c in range(col):
            #Choose which character
            if board[r][c] == 1:
                character = '#'
            else:
                character = " "


            if c == 0:
                print("|  " + str(character), end=" ")
            elif c == col - 1:
                print(str(character) + "  |\n")
            else:
                print(" " + str(character) + " ", end=" ")




def main():

    board = random_state(DIMENSION, DIMENSION)
    done = False

    while not done:

        for event in py.event.get():
            if event.type == pygame.QUIT:
                done = True

        screen.fill(BLACK)

        for r in range(DIMENSION):
            for c in range(DIMENSION):
                colour = WHITE
                if board[r][c] == 1:
                    colour = GREEN
                    py.draw.rect(screen, colour, [(MARGIN + WIDTH) * c + MARGIN,
                              (MARGIN + HEIGHT) * r + MARGIN,
                              WIDTH,
                              HEIGHT])

        # render(board)
        board = next_board_state(board)
        clock.tick(60)
        py.display.flip()
        #time.sleep(0.1)



if __name__ == '__main__':
    main()



    # # TEST 1: dead cells with no live neighbors
    # # should stay dead.
    # init_state1 = [
    #     [0, 0, 0],
    #     [0, 0, 0],
    #     [0, 0, 0]
    # ]
    # expected_next_state1 = [
    #     [0, 0, 0],
    #     [0, 0, 0],
    #     [0, 0, 0]
    # ]
    # actual_next_state1 = next_board_state(init_state1)
    #
    # if np.all(expected_next_state1 == actual_next_state1):
    #     print("PASSED 1")
    # else:
    #     print("FAILED 1!")
    #     print("Expected:")
    #     print(expected_next_state1)
    #     print("Actual:")
    #     print(actual_next_state1)
    #
    # # TEST 2: dead cells with exactly 3 neighbors
    # # should come alive.
    # init_state2 = [
    #     [0, 0, 1],
    #     [0, 1, 1],
    #     [0, 0, 0]
    # ]
    # expected_next_state2 = [
    #     [0, 1, 1],
    #     [0, 1, 1],
    #     [0, 0, 0]
    # ]
    # actual_next_state2 = next_board_state(init_state2)
    #
    # if np.all(expected_next_state2 == actual_next_state2):
    #     print("PASSED 2")
    # else:
    #     print("FAILED 2!")
    #     print("Expected:")
    #     print(expected_next_state2)
    #     print("Actual:")
    #     print(actual_next_state2)
