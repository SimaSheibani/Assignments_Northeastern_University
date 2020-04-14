def triangular_number():
    '''
    Takes a number and calculates the triangular of that number
    Input: Integer -> Return: Integer
    when done printed, It return the list of triangular numbers
    '''

    number = input("Enter a number, or enter 'done' :")
    list_sum_number = []
    while (number != 'done'):
        n = int(number)
        if n > 0:
            sum_number = int((n * (n + 1))/2)
            print("The triangular number for", n, "is", sum_number)
            list_sum_number.append(sum_number)
        number = input("Enter a number, or enter 'done'")
    print(list_sum_number)


def main():

    triangular_number()


main()
