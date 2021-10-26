'''3.Write a main menu program for the following- 
Accept an option from the user and required variables. Check whether the values of variables are not zero or -ve.

if option is 's' or 'S' - swapping(using three variables)
if option is 'i' or 'I' - calculate simple interest
if option is 'c' or 'C' - convert from meters to centimeters
if option is 't' or 'C' - find fahrenheit to centigrade
if option is 'p' or 'P'- find perimeter of rectangle
Else if the user gives any other option then print no such option'''




a=str(input("Enter your options(s/i/c/t/p) = "))


if(a=='s' or a=='S'):
    print("Swapping 2 variables")
    b1=int(input("Enter 1st variable "))
    b2=int(input("Enter 2nd variable "))
    temp=b1
    b1=b2
    b2=temp
    print("1st variable after swapped ",b1)
    print("2nd variable after swapped ",b2)
elif(a=='i' or a=='I'):
    print("Calculating simple interest")
    p=int(input("Enter principle amount = "))
    r=float(input("Enter rate of interest = "))
    t=int(input("Enter time period = "))
    si=(p*r*t)/100
    print("Your simple interest is ",si)
elif(a=='c' or a=='C'):
    print("Converting meters into centimeters")
    met=int(input("Enter value in meters "))
    cent=met*100
    print("Value in centimeters is ",cent)
elif(a=='t' or a=='T'):
    print("Converting from fahrenheit to centigrade")
    fah=int(input("Enter value in fahrenheit = "))
    centi=(fah-32)*(5/9)
    print("Temp in centigrade = ",centi)
elif(a=='p' or a=='P'):
    print("Finding perimeter of rectangle")
    length=int(input("Enter length ="))
    breadth=int(input("Enter breadth = "))
    per=2*(lenght+breadth)
    print("Perimeter of rectangle is ",per)
else:
    print("No such options available")
