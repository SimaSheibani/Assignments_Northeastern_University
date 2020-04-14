# This class contain a method that it takes an integer argument
# and return a list of all primes from 2 to the argument value.


class PrimeGenerator:

    def primes_to_max(self, number):

        prime_list = []
        not_prime_set = set()

        for i in range(2, number+1):
            if i in not_prime_set:
                continue

            for j in range(i*i, number+1, i):
                not_prime_set.add(j)

            prime_list.append(i)

        return prime_list
