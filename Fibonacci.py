limit = int(input("Enter the required number of terms in the Fibonacci series : ")) 
i = -1
j = 1
n = 0
while n < limit:
    k = i + j
    print(k)
    i = j
    j = k
    n += 1
