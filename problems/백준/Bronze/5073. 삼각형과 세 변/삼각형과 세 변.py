import sys

while True:
    sides = sorted(list(map(int, sys.stdin.readline().split())))
    if sides[0] == sides[1] == sides[2] == 0:
        break

    if sides[2] >= sides[0] + sides[1]:
        print("Invalid")
    else:
        if sides[0] == sides[1] == sides[2]:
            print("Equilateral")
        elif sides[1] == sides[2] or sides[0] == sides[1] or sides[2] == sides[0]:
            print("Isosceles")
        else:
            print("Scalene")
