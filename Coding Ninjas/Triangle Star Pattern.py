## Read input as specified in the question
## Print the required output in given format
N = int(input())

for i in range(N):
    for j in range(i+1):
        print("*", end="")
    print()