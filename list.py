List1 = []
Length = int(input('Enter the range of list'))
for i in range(length):
        X = int(input("Enter the elememts of lists"))
        List1.append(X)
print(List1)
print('before finding',List1)
Positive_Numbers =list(filter(lambda Y: Y>0,List1))
print('The positive numbers are = ',Positive_Numbers)
