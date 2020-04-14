import sys


def main(width, height, symbol):

    if (width < 2) or (height < 2):
        print("The value is too low.")
    else:
        for row in range(height):
            if(row == 0) or (row == height - 1):
                print(symbol * width)
            else:
                print(symbol+' '*(width-2)+symbol)


main(int(sys.argv[1]), int(sys.argv[2]), str(sys.argv[3]))
