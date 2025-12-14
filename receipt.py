sum=0
count=1
bill=''
while (True):
    user_input=input("Enter the price or q to quit:\n")
    if (user_input!='q'):
        sum=sum+int(user_input)
            bill=bill+f"{count}:{int(user_input)}\n"
            count=count+1
    else:
        print("Thanks for shopping with us")
        print(f"Your total bill is {sum}")     
        break   
print(bill)
