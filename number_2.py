print([i**2 for i in [int(n) for n in input().split()]
       if ((i**2 - 9) % 10 != 0) and (i%2 != 0)])

