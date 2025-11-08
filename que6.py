#Write a program to input the principal, rate, and time, and display the simple interest.
principal_amount=int(input("Enter a principle amount :"))
rate=int(input("Enter a rate of intrest :"))
time=int(input("Enter a time period(in years) :"))
simple_intrest=(principal_amount*rate*time)/100
print("Simple intrest is:",simple_intrest)
