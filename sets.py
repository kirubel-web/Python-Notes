odd = {1, 3, 5, 7, 9}
even = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}
u = odd.union(even)
print(u)

i = even.intersection(primes)
print(i)

diff = odd.difference(primes)
print(diff)

