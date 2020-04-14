def cube_print():
    # drawing the cube with 2 for-loop. The first one in the range of haf of
    # the cube size plus one
    # And the second one in the range of cube suze plus 2.
    number = int(input("Input cube size (multiple of 2): "))
    haf_num = int(number/2)
    range_n_1 = haf_num + 1
    for i in range(range_n_1):
        if i == 0:

            print(" " * haf_num + "+" + "-" * number + "+")
        else:
            print(" " * (haf_num - i) + "/" + " " * number + "/" + (i-1) * " "
                  + "|")

    for i in range(number + 2):
        if i == 0:
            print("+" + "-" * number + "+" + (haf_num - 1) * " " + "|")
        elif i == number + 1:
            print("+" + "-" * number + "+")
        elif i < haf_num:
            print("|" + " " * number + "|" + (haf_num - 1) * " " + "|")
        elif (i == haf_num):
            print("|" + " " * number + "|" + (haf_num - 1) * " " + "+")
        else:
            print("|" + " " * number + "|" + (number - i) * " " + "/")

    print()

# The main function just call the cube_print function.


def main():

    cube_print()


main()
