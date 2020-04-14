def main():

    height = int(input("Please enter an odd number:"))
    while (height < 3) or (height % 2 == 0):
        height = int(input("It was not an odd number, pick another one:"))

    widt = height
    for row in range(height):
        if (row == 0):
            print(' '*int(widt/2), '*')
        elif (row == height - 1):
            print('/', '_' * (widt-1), '\\')
        else:
            if (row % 2 != 0):
                print(' ')
            else:
                print(' '*((int(widt/2))-(int(row/2))), '/', ' '*(row-2), '\\')


main()
