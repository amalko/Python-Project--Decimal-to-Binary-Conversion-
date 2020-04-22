
x=[]


num= int(input("Enter a decimal number: "))


while num>0:
    a=num % 2
    x.append(a)
    num= int(num/2)

print("Binary representation of the given decimal number is : ")
x.reverse()
l= len(x)

for i in range(l):
    print(x[i], end='')
print()




