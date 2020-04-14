def main():

    row_1 = (input("Enter a magic number:\n"))
    row_2 = (input())
    row_3 = input()

    row_1_list = [int(d) for d in str(row_1)]
    row_2_list = [int(d) for d in str(row_2)]
    row_3_list = [int(d) for d in str(row_3)]

    check = True

    lsit_of_rows = [row_1_list, row_2_list, row_3_list]
    for row in lsit_of_rows:
        if(row[0] + row[1] + row[2] != 15):
            check = False
    for i in range(len(lsit_of_rows)):
        if(row_1_list[i] + row_2_list[i] + row_3_list[i] != 15):
            check = False
    if (row_1_list[0] + row_2_list[1] + row_3_list[2] != 15):
        check = False
    elif (row_1_list[2] + row_2_list[1] + row_3_list[0] != 15):
        check = False
    if(check):
        print("This is a magic number!")
    else:
        print("This is not a magic square!")


main()
