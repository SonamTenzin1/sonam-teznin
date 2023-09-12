while True:
    print ("welcome to my converter.I am here to help you convert temperature on celsius and fahrenheit scale")
    print ("temperature conversion menu:")
    print ("1.celsius to fahrenheit")
    print ("2.fahrenheit to celsius")
    print ("3.quit")

    choice = int(input("please enter your choice(1/2/3): "))

    if choice == 1:
        celsius = float(input("please enter the temperature value in celsius: "))
        fahrenheit = ((celsius* 9//5) + 32)
        print(celsius,"°C is equal to ", fahrenheit, "°F")

    elif choice == 2:
        fahrenheit = float(input("please enter the temperature value in fahrenheit: "))
        celsius = (fahrenheit - 32)*5//9
        print(fahrenheit,"°F is equal to ", celsius, "°C")

    elif choice == 3:
        print("see you again")
        break
        
    else:
        print("invalid choice please select 1,2 or 3")
