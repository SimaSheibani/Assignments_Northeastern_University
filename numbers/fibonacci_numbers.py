import sys


def main(number):

    a = 0
    b = 1
    list_c = [0, 1]
    for i in range(int(number-2)):
        c = a + b
        a = b
        b = c
        list_c.append(c)

    print(list_c)


main(int(sys.argv[1]))
