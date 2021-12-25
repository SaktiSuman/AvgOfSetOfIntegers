count = int(input("Enter the count of integers: "))
sum = 0
for i in range(count):
    x = int(input("Enter the integer: "))
    sum = sum + x
avg = round(sum / count)
print("The average of provided integers is ",avg)