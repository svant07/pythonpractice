primes = []
not_primes = []
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
is_prime = True
for i in numbers:
    if i == 1:
        continue
    #print(i)
    for j in range(2, i):
        if i % j == 0:
            not_primes.append(i)
            #is_prime = False
            break
    if i not in not_primes:
            primes.append(i)
            #is_prime = True
print('Primes: ', primes)
print('Not primes: ', not_primes)
