from prime_generator import PrimeGenerator


def main():

    number = int(input("Enter a number: \n"))
    prime_list = PrimeGenerator()

    print(prime_list.primes_to_max(number))


main()
