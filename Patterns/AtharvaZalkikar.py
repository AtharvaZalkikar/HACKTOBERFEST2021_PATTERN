## Read input as specified in the question
## Print the required output in given format
n = int(input())
i = 1
while i <= n:
    j = 1
    while j <= i:
        print(i+1-j,end='')         #We need to find what to print by observation fro eg (i+1-j)
        j = j+1
    print()
    i = i + 1                       #It is important to note that the iteration of i here should be outside the while loop of j 
