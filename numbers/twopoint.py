import math


def main():
    x1 = int(input("X1 ="))
    y1 = int(input("Y1 ="))
    x2 = int(input("X2 ="))
    y2 = int(input("Y2 ="))

    distance = math.sqrt((y2-y1)**2 + (x2-x1)**2)
    print("Distance between (x1.y1) and (x2,y2) is", distance)


main()
