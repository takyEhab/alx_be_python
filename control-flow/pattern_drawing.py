side = int(input("Enter the size of the pattern: "))
i = 1
while i <= side: 
    for j in range(side):
        print("*", end="") 
    print()
    i += 1
