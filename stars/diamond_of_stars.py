import sys


def main(number):

    my_range = (number / 2)

    for i in range(int(my_range)):
        print(' ' * int((number/2)-i), '*' * ((2 * i)+1))
    for j in range(int((my_range)+(number % 2)), 0, -1):
        print(' ' * int(number/2 - j + 1), '*' * ((2 * j)-1))


main(int(sys.argv[1]))
