primes = []
not_primes = []
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
is_prime = True
for i in range(1,16):
    for j in range(2, i):
        if i % j == 0:
            not_primes.append(i)
            continue

        else:
            #i = is_prime
            primes.append(i)
            break
print('Primes: ', primes)
print('Not primes: ', not_primes)

