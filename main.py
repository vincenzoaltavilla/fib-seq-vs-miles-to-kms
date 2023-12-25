CONV_FACTOR = 1.609344
TEST_NUMBER = 13


def miles_to_kms(miles):
    km = miles * CONV_FACTOR
    trunk_digits = 6
    int_part, decimal_part = str(km).split('.')
    km = float(f"{int_part}.{decimal_part[:trunk_digits]}")
    km = int(round(km, 0))
    return km


def fibonacci(n):
    fib_sequence = [0, 1]

    for i in range(2, n):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])

    return fib_sequence[:n]


fib_seq = fibonacci(TEST_NUMBER)

for i in range(3, TEST_NUMBER+1):
    if fib_seq[i] != miles_to_kms(fib_seq[i-1]):
        print(fib_seq[i])
        break

# Breaks at 89, miles_to_kms(89) = 143, whereas the number after 89 in the Fibonacci sequence is 144.
