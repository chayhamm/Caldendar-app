import calendar


new = bool(True)

while new == True:
    mm = int(input("Enter the year you would like to view: "))
    yy = int(input("Enter the number value of the month you would like to view: "))
    print("Here is your Year & Month: ")
    print(calendar.month(mm, yy))
    again = input("Would you like to go again? Y/N: ")
    againLower = again.lower()
    if againLower == "y":
        print("")
    else:
        new = False
        break