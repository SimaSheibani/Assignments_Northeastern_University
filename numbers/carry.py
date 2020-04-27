'''
This program gives 2 input from user. adding them and return the
number of sum and the number of times the
"carry" operation needs to be carried out.
'''
number_1 = input("Enter the first number ")
number_2 = input("Enter the first number ")


def toList(number):
    '''
    This function get number and a list.
    '''

    list_number = []
    list_number = list(str(number))
    return list_number


def sum():
    '''
    Function of sum add two list number and return the sum list. Convert sum
    list to string and calculate the number of carry out
    '''
    counter = 0
    list_1_string = toList(number_1)
    list_2_string = toList(number_2)
    diff_length = len(list_1_string) - len(list_2_string)

    if(diff_length > 0):
        list_max = convert_list_to_number(list_1_string, 1)
        list_min = convert_list_to_number(list_2_string, diff_length+1)
    else:
        list_max = convert_list_to_number(list_2_string, 1)
        list_min = convert_list_to_number(list_1_string, abs(diff_length)+1)

    list_carry = [0] * (len(list_max))
    list_sum = [0] * (len(list_max))

    for i in range(len(list_max)-1, -1, -1):
        p = list_max[i] + list_min[i] + list_carry[i]
        if p >= 10:
            list_carry[i-1] = 1
            counter += 1
            list_sum[i] = p-10
        else:
            list_sum[i] = p
    if list_sum[0] == 0:
        list_sum.pop(0)
    number_str_sum = ""
    for i in range(len(list_sum)):
        number_str_sum += str(list_sum[i])

    print(number_1, "+", number_2, "=", number_str_sum)
    print("Numer of carries :", counter)


def convert_list_to_number(list_number, additional):
    '''
    This function get string list number. Add 0 to the list of number
    to have the same size of list and return int list.
    '''

    list_temp = [0] * additional
    list_num = list_temp + list_number
    list_res = list(map(int, list_num))

    return list_res


def main():
    sum()


main()
