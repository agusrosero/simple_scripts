import random
import time


def matrix_rain(width, height):
    symbols = "0123456789!@#$%^&*QWERTYUIOPASDFGHJKLZXCVBNM"
    matrix = []
    for _ in range(height):
        row = []
        for _ in range(width):
            row.append(random.choice(symbols))
        matrix.append(row)
    
    while True:
        for row in matrix:
            print("".join(row))
        time.sleep(0.1)
        print("\033[H")


matrix_rain(60, 20)        