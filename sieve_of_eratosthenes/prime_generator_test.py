from prime_generator import PrimeGenerator


def test_primes_to_max():
    ''' Test the Prime to max method'''

    pr = PrimeGenerator()
    assert pr.primes_to_max(6) == [2, 3, 5]
    assert pr.primes_to_max(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    assert pr.primes_to_max(50) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
                                    41, 43, 47]
