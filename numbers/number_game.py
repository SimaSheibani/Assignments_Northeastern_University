import random


def main():
    print("Welcome to the Guessing Game!")
    secret = random.randint(1, 50)
    guess = int(input("I picked a number between 1 and 50. Try and guess!\n"))
    print("You guessed", guess)
    times = 1
    scalding_hot = 1
    extremely_warm = 2
    very_warm = 3
    warm = range(4, 6)
    cold = range(6, 9)
    very_cold = range(9, 14)
    extremely_cold = range(14, 21)
    while (guess != secret):
        times += 1
        diff = abs(guess - secret)
        if (diff == scalding_hot):
            guess = int(input("Your guess is scalding hot\n"))
        elif (diff == extremely_warm):
            guess = int(input("your guess is extremely warm\n"))
        elif (diff == very_warm):
            guess = int(input("Your guess is very warm\n"))
        elif (diff in warm):
            guess = int(input("Your guess is warm\n"))
        elif (diff in cold):
            guess = int(input("Your guess is cold\n"))
        elif (diff in very_cold):
            guess = int(input("Your guess is very cold\n"))
        elif (diff in extremely_cold):
            guess = int(input("Your guess is extremely cold\n"))
        else:
            guess = int(input("Your guess is freezing miserably cold\n"))
    if times == 1:
        print("That was lucky. You figured it out in", times, "tries!")
    elif (times > 1 and times < 5):
        print("That was amazing! You figured it out in", times, "tries!")
    elif (times == 6 or times == 5):
        print("That was okay. You figured it out in", times, "tries!")
    elif times == 7:
        print("Meh. You figured it out in", times, "tries!")
    elif times == 8 or times == 9:
        print("This is not your game. You figured it out in", times, "tries!")
    else:
        print("You are the worst guesser I'e ever seen. You \
figured it out in", times, "tries!")


main()
