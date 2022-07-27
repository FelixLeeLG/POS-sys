#Python Midterm - Felix Lee
#Program to take orders from a burger menu and then calculate the total

#main function
def main():
    total = 0
    exit = input("To start ordering, type anything or  6 to exit: ")
    while exit != "6":
        displayMenu()
        staffOrStudent, burgerType, qty = retrieveOrders()
        result = computeBill(staffOrStudent, burgerType, qty)
        total += result[1] #this adds the cost of all the burgers ordered
        displayBill(result[0], result[1], qty, burgerType, result[2], staffOrStudent, result[3], total)
        exit = input("To keep ordering, type anthing or 6 to pay: ")
    

def displayMenu():
    print(" 1 - De Anza Burger - $5.25",
    "\n 2 - Bacon Cheese - 5.75",
    "\n 3 - Mushroom Swiss - 5.95",
    "\n 4 - Western Burger - 5.95",
    "\n 5 - Don Cali Burger - 5.95",
    "\n 6 - Done Ordering")

def retrieveOrders():#getting the user's input of what they wanna order
    burgerType = 0
    qty = 0
    #asking if the person ordering is student or staff
    staffOrStudent = ""
    while staffOrStudent != "Staff" and staffOrStudent != "staff" and staffOrStudent != "Student" and staffOrStudent != "student":
        staffOrStudent = input("Please enter Staff or Student: ")
        staffOrStudent = staffOrStudent.strip() #stripping the user's input of unnecessary spaces in the beginning or end of the input

    burgerType = int(input("Which number would you like to order? "))
        #code will run if the burger type the user inputs is of 1 of the 5 options on the menu
    if burgerType >= 1 and burgerType <= 5:
        qty = input("How many would you like to order?")
        try:
            qty = int(qty)#checks to see if it is a numeric value
        except:
              qty = int(input("Please enter a numeric number: "))
              while qty <= 0:
                  qty = int(input("Please enter a positive number: "))
        while qty <= 0: #making sure that the quantity ordered is postive
            qty = int(input("Please enter a positive number: "))
            try:
                qty = int(qty)
            except:
                qty = int(input("Please enter a numeric number: "))
                while qty <= 0:
                    qty = int(input("Please enter a positive number: "))
                    
        #code will run if the burger type the user inputs is NOT one of the numbers the on the menu       
    if burgerType < 1 or burgerType > 5:
        burgerType = input("Please enter a number from 1 to 5: ")
        try:
            burgerType = int(burgerType)
        except:
           burgerType = int(input("Please enter a numeric number"))
        qty = input("How many would you like to order?")
        try:
            qty = int(qty)
        except:
            qty = int(input("Please enter a numeric number: "))
        while qty <= 0:
            qty = int(input("Please enter a positive number: "))
            while qty <= 0:
                qty = input("Please enter a positive number: ")
        
    #returns the inputs of the user
    return (staffOrStudent, burgerType, qty)

    
def computeBill(staffOrStudent, burgerType, qty):#calcuates the cost of the order
    burgerCost = 0
    #associates burger type with the cost of the burger type
    if burgerType == 1:
        burgerCost = 5.25
    elif burgerType == 2:
        burgerCost = 5.75
    elif burgerType == 3 or burgerType == 4 or burgerType == 5:
        burgerCost = 5.95

    taxedResult = 0
    tax = 0
    result = 0

    #caluclating the cost
    result = burgerCost * float(qty)
    #checks if it staff or student for tax
    if staffOrStudent == "Staff" or staffOrStudent == "staff":
        tax = 9
        taxedResult = result * 1.09
    elif staffOrStudent == "Student" or staffOrStudent == "student":
        taxedResult = result

    #returns calculated values and constants
    return (result, taxedResult, burgerCost, tax)


def displayBill(result, taxedResult, qty, burgerType, burgerCost, staffOrStudent, tax, total):#displays the bill with the burger number, the quantity, the tax, cost before and after tax, and the total of the bill so far.
    print("\nThe burger number you ordered is: " + str(burgerType))
    print("The number of burger(s) you ordered is: " + str(qty))
    print("Your cost before tax is: $%.2f" % result)
    print("Your cost after tax is: $%.2f" % taxedResult + " because you were taxed at " + str(tax) + "% for this order.")
    print("Your current total is: $%.2f" % total)#prints the total so far

main()      

'''
Scenario 1:
To start ordering, type anything or  6 to exit: 
 1 - De Anza Burger - $5.25 
 2 - Bacon Cheese - 5.75 
 3 - Mushroom Swiss - 5.95 
 4 - Western Burger - 5.95 
 5 - Don Cali Burger - 5.95 
 6 - Done Ordering
Please enter Staff or Student: sfd
Please enter Staff or Student: Staff
Which number would you like to order? 7
Please enter a number from 1 to 5: 4
How many would you like to order?n
Please enter a numeric number: -1
Please enter a positive number: 1

The burger number you ordered is: 4
The number of burger(s) you ordered is: 1
Your cost before tax is: $5.95
Your cost after tax is: $6.49 because you were taxed at 9% for this order.
Your current total is: $6.49
To keep ordering, type anthing or 6 to pay:6



Scenario 2:
To start ordering, type anything or  6 to exit: 
 1 - De Anza Burger - $5.25 
 2 - Bacon Cheese - 5.75 
 3 - Mushroom Swiss - 5.95 
 4 - Western Burger - 5.95 
 5 - Don Cali Burger - 5.95 
 6 - Done Ordering
Please enter Staff or Student: sdf
Please enter Staff or Student: Staff
Which number would you like to order? 9
Please enter a number from 1 to 5: 1
How many would you like to order?-1
Please enter a positive number: 1

The burger number you ordered is: 1
The number of burger(s) you ordered is: 1
Your cost before tax is: $5.25
Your cost after tax is: $5.72 because you were taxed at 9% for this order.
Your current total is: $5.72
To keep ordering, type anthing or 6 to pay:
 1 - De Anza Burger - $5.25 
 2 - Bacon Cheese - 5.75 
 3 - Mushroom Swiss - 5.95 
 4 - Western Burger - 5.95 
 5 - Don Cali Burger - 5.95 
 6 - Done Ordering
Please enter Staff or Student: Student
Which number would you like to order? 3
How many would you like to order?1

The burger number you ordered is: 3
The number of burger(s) you ordered is: 1
Your cost before tax is: $5.95
Your cost after tax is: $5.95 because you were taxed at 0% for this order.
Your current total is: $11.67
To keep ordering, type anthing or 6 to pay: 6


'''
