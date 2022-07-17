#Prime number generator

m = int(input("Enter upper range (exclusive): "))

for n in range(2,m):
    if n > 1:
      for i in range (2,n):
        if n % i == 0:
          break
      else:
        print(n)