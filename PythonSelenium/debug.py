num = int(input("how many numbers: "))
total_sum = 0
for i in range(num):
    number = float(input("enter any number: "))
    total_sum = total_sum + number
print(total_sum)
avg= total_sum/num
print(avg)
#av = float(((n*(n+1))/2)/n)
#print(av)
