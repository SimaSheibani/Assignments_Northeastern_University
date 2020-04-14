# My name is Sima Sheibani
# This program creating username and password
import random


# This program is getting first name, last name, and favorite name from the
# user and playing with them, e.g. capitalize first letter or adding number.
def main():

    print("Welcome to the username and password generator!")
    first_name = input("Please enter your first name : ").lower()
    last_name = input("Please enter your last name : ").lower()
    last_name_2 = last_name
    favorite_name = input("Please enter your favorite name : ").lower()
    print(" ")

    # To creating usernam I put first letter of first name and all last name
    # I add * to last name if it is less than 7 letter.
    # and then add a random number.
    random_number = random.randint(0, 100)
    if (len(last_name) == 6):
        last_name = last_name + "*"
    elif (len(last_name) == 5):
        last_name = last_name + "**"
    elif (len(last_name) == 4):
        last_name = last_name + "***"
    elif (len(last_name) == 3):
        last_name = last_name + "****"
    elif (len(last_name) == 2):
        last_name = last_name + "*****"
    elif (len(last_name) == 1):
        last_name = last_name + "******"

    print("Thanks ", first_name.capitalize(), ", your user name is \
", first_name[0], last_name, random_number, sep="")
    print(" ")
    print("Here are three suggested passwords for you to consider:\n")

    # To creating password 1 I replace some letters of first name and
    # last name with numbers and symbol.e.g. o with 0 or s with $
    # and put random number between first name and last name
    random_number_1 = random.randint(0, 100)
    first_name_1 = first_name.replace("o", "0").replace("s", "$").replace("l\
", "1").replace("a", "@")
    last_name_1 = last_name_2.replace("o", "0").replace("s", "$").replace("l\
", "1").replace("a", "@")
    print("Password 1 : ", first_name_1, random_number_1, last_name_1, sep="")

    # To creating password 2 I put first and last character of each user's
    # first name, last name and favorite name together.
    # In each case, the first letter of them in lower case and the second in
    # upper case.
    print("Password 2 : ", first_name[0], first_name[len(first_name)
          - 1].upper(), last_name_2[0], last_name_2[len(last_name_2)-1].
          upper(), favorite_name[0], favorite_name[len(favorite_name)-1].
          upper(), sep="")
    # To creating password 3, first I creat random number of length of first
    # name, last name name and favorite name.
    # Then I used substring method for each of them. Then print first letter
    # of each in upper case and the rest of substring of random length.
    random_pass_last_name = random.randint(1, len(last_name_2))
    last_name_substr = last_name_2[1:random_pass_last_name]
    random_pass_first_name = random.randint(1, len(first_name))
    first_name_substr = first_name[1:random_pass_first_name]
    random_pass_favorite_name = random.randint(1, len(favorite_name))
    favorite_name_substr = favorite_name[1:random_pass_favorite_name]
    print("Password 3 : ", last_name_2[0].upper(), last_name_substr,
          favorite_name[0].upper(), favorite_name_substr, first_name[0].
          upper(), first_name_substr, sep="")


main()
