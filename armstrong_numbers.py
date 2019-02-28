
#Var calling int on user input
num = int(input("enter a number: "))

#Var calling length of the string from Var num
order = len(str(num))

#Initializing sum as an int and refering num as temp
sum = 0
temp = num

#Algorithm for checking if the user entered number is a Armstrong Number
while(temp != 0):
    digit = temp % 10
    sum += digit ** order
    temp //= 10


#Print if it is or else print that it is not
if num == sum:
    print(num,"is an armstrong")
else:
    print(num,"is not an armstrong")
