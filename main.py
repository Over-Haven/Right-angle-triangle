#take
row = int(input("Please enter the total number of rows :"))
number = 1 # 1


print("Floyd's Triangle")
#output
for i in range(1, row + 1):
    #inner
    for j in range(i, i + 1):
        #display
        print(number,end = ' ')
        number = number + 1
    print()