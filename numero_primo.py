import math

def isPrime(n):
    start = 2;

    while start <= math.sqrt(n):
        if n % start < 1:
            return False;
        start += 1;

    return n > 1;

if __name__ == "__main__":
    print("Eh primo:")

    print(isPrime(12962962592588887))
