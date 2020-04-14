'''This program check the validity of numbers.
we double each second digits from right to left.
If the resulting number is more than 10, adding two digits of number.
Adding all numbers together.
If the resulting sum is evenly divisible by 10, the sequence is valid. If the
resulting sum is not divisible by 10, the sequence is not valued
'''


def list_input():
    code_number = input("Enter your code Id : ")
    '''list_1 is the string list of code_number
    and list_2 is the int list list_2 '''
    list_1 = []
    list_1 = list(str(code_number))
    list_2 = list(map(int, list_1))
    j = 0
    '''In this for loop we double the second number from right'''
    for i in range(len(list_2)-1, -1, -1):
        j += 1
        if j % 2 == 0:
            list_2[i] = list_2[i] * 2
    '''In this for loop we used method sum_in_list'''
    for i in range(len(list_2)):
        list_2[i] = sum_in_list(list_2[i])
    '''In this for loop we find the sum of digit and if it is
    diivded by 10 or not!'''
    x = 0
    for i in list_2:
        x += i
    if x % 10 == 0:
        print("Your Id number (", code_number, ") is valid")
    else:
        print("Your Id number (", code_number, ") is not valid")
    '''This method retuen the sum of two digits of numbers more than 10'''


def sum_in_list(number):
    list_number = []
    if number >= 10:
        list_number = [int(i) for i in str(number)]
        sum = list_number[0] + list_number[1]
        return sum
    else:
        return number

    '''The main function just call the list_input fnction.'''


def main():
    list_input()


main()
