n = int(input("digite um numero"))
def numtri (n):
    if n <= 1:
        return 1
    else:
        return n * numtri(n - 1)
print (numtri (n))








             