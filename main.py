#take
print("Half pyramid patter is start(*):")
n = int(input("Enter the number of row:"))
#outer
for i in range(n):
    #inner
    for j in range(i + 1):
        #display result
        print("* ", end = "")
    print()
