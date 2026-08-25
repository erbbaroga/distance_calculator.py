#Distance calculator
##This program converts distance in kilometers into miles.

##Ask the user to enter the distance in kilometers
km1=float(input("Enter distance in kilometers: "))

##Convert it from kilometers to miles using its formula
mile1=0.612371
mile2=km1*mile1

##Display the result
print("Distance in miles:",mile2)

##Ask the user if they want to convert another distance
a=input("Do you want to convert another distance? (yes/no): ")
##If yes, then ask the user to enter the distance in kilometers
if a=="yes":
    km2=float(input("Enter distance in kilometers: "))
    r=km2*mile1

    ## Display the result
    print("Distance in miles:", r)

    ##If not, then the program will end.
else:
    print("Program ended.")