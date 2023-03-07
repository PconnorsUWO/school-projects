# Patrick Connors
# 251313609
# Sorry about longer lines I annotated everything.

# Constant Variables
REBUILTS = [['1', 'Legion Tower Gen 7 with RTX 3080 Ti', 3699.99], ['2',
'SkyTech Prism II Gaming PC', 2839.99], ['3', 'ASUS ROG Strix G10CE Gaming PC',
1099.99]]
SSD = [['1', '250 GB', 69.99], ['2', '500 GB', 93.99], ['3', '4 TB', 219.99]]
HDD = [['1', '500 GB', 106.33], ['2', '1 TB', 134.33]]
CPU = [['1', 'Intel Core i7-11700K', 499.99], ['2', 'AMD Ryzen 7 5800X', 312.99]]
MOTHERBOARD = [['1', 'MSI B550-A PRO', 197.46], ['2', 'MSI Z490-A PRO', 262.30]]
RAM = [['1', '16 GB', 82.99], ['2', '32 GB', 174.99]]
GRAPHICS_CARD = [['1', 'MSI GeForce RTX 3060 12GB', 539.99]]
PSU = [['1', 'Corsair RM750', 164.99]]
CASE = [['1', 'Full Tower (black)', 149.99], ['2', 'Full Tower (red)', 149.99]]

# So I could use my price calculator formula and divide by zero without error
def safeDivide(num, den):
    if den == 0:
        return 0
    else:
        return num / den

# Calculates the cost of either prebuilt or PC from individual parts
# Formula multiplies and divides by number in list as if it is zero i.e no part there will be no added cost.
def calculateCost(items):
    newList = []
    for i in items:
        if i != ("x" or "X"):
            newList.append(int(i))
        elif i == ("x" or "X"):
            newList.append(0)
    if len(items) > 1:
        totalCost = (safeDivide((CPU[newList[0]-1][2])*newList[0], newList[0])+safeDivide((MOTHERBOARD[newList[1]-1][2])*newList[1], newList[1])+safeDivide((RAM[newList[2]-1][2])*newList[2], newList[2])+safeDivide((PSU[newList[3]-1][2])*newList[3], newList[3])+safeDivide((CASE[newList[4]-1][2])*newList[4], newList[4])+safeDivide((SSD[newList[5]-1][2])*newList[5], newList[5])+safeDivide((HDD[newList[6]-1][2])*newList[6], newList[6])+safeDivide((GRAPHICS_CARD[newList[7]-1][2])*newList[7], newList[7]))
        return totalCost
    else:
        totalCost = REBUILTS[newList[0]-1][2]
        return  totalCost

# Prints part details
def letsPrintParts(part, partnumber):
    partSpecs = []
    for indidivialpart in part[partnumber-1]:
        partSpecs.append(indidivialpart)
    print(partSpecs[0] + " : " + partSpecs[1] + ", $" + str("{:.2f}".format(partSpecs[2])))


# Function to check if answer is allowed if not stay false.
def acceptableCases(variable, whatsAllowed):
    isAcceptable = False
    if variable in whatsAllowed:
        isAcceptable = True
    return isAcceptable

# Main function
def pickItems():

    # Variables for function
    possibleReset = True
    checkoutCost = []
    partsList = []
    checkAnswer1,checkAnswer2,checkAnswer3,checkAnswer4,checkAnswer5,checkAnswer6,checkAnswer7,checkAnswer8,checkAnswer9,checkAnswer10,checkAnswer11 = 0,0,0,0,0,0,0,0,0,0,0

    # While loop that contains everything
    while possibleReset == True:

        # Asking and getting inputs for computer parts
        while acceptableCases(checkAnswer1, ["1","2","3"]) != True:
            checkAnswer1 = input("Would you like to build a custom PC (1), purchase a pre-built PC (2), or would you like to checkout (3)? ")


        if checkAnswer1 == "1":
            print("\nGreat! Let's start building your PC!\n\nFirst, let's pick a CPU.")
            letsPrintParts(CPU, 1)
            letsPrintParts(CPU, 2)
            while acceptableCases(checkAnswer2, ["1","2"]) != True:
                checkAnswer2 = input("Choose the number that corresponds with the part you want: ")

            print("\nNext, let's pick a compatible motherboard.")
            if checkAnswer2 == "1":
                letsPrintParts(MOTHERBOARD, 2)
                while acceptableCases(checkAnswer3, ["2"]) != True:
                    checkAnswer3 = input("Choose the number that corresponds with the part you want: ")
            else:
                letsPrintParts(MOTHERBOARD, 1)
                while acceptableCases(checkAnswer3, ["1"]) != True:
                    checkAnswer3 = input("Choose the number that corresponds with the part you want: ")

            print("\nNext, let's pick your RAM.")
            letsPrintParts(RAM, 1)
            letsPrintParts(RAM, 2)
            while acceptableCases(checkAnswer4, ["1","2"]) != True:
                checkAnswer4 = input("Choose the number that corresponds with the part you want: ")

            print("\nNext, let's pick your PSU.")
            letsPrintParts(PSU, 1)
            while acceptableCases(checkAnswer5, ["1"]) != True:
                checkAnswer5 = input("Choose the number that corresponds with the part you want: ")

            print("\nNext, let's pick your case.")
            letsPrintParts(CASE, 1)
            letsPrintParts(CASE, 2)
            while acceptableCases(checkAnswer6, ["1","2"]) != True:
                checkAnswer6 = input("Choose the number that corresponds with the part you want: ")

            print("\nNext, let's pick an SSD (optional, but you must have at least one SSD or HDD).")
            letsPrintParts(SSD, 1)
            letsPrintParts(SSD, 2)
            letsPrintParts(SSD, 3)
            while acceptableCases(checkAnswer7, ["1","2","3","x","X"]) != True:
                checkAnswer7 = input("Choose the number that corresponds with the part you want: ")

            print("\nNext, let's pick an HDD (optional, but you must have at least one SSD or HDD).")
            letsPrintParts(HDD, 1)
            letsPrintParts(HDD, 2)
            if checkAnswer7 != "x":
                while acceptableCases(checkAnswer8,["1","2","x","X"]) != True:
                    checkAnswer8 = input("Choose the number that corresponds with the part you want: ")
            else:
                while acceptableCases(checkAnswer8, ["1", "2"]) != True:
                    checkAnswer8 = input("Choose the number that corresponds with the part you want: ")

            print("\nFinally, let's pick your graphics card (or X to not get a graphics card)")
            letsPrintParts(GRAPHICS_CARD, 1)
            while acceptableCases(checkAnswer11, ["1","x","X"]) != True:
                checkAnswer11 = input("Choose the number that corresponds with the part you want: ")

            partsList += [checkAnswer2, checkAnswer3, checkAnswer4, checkAnswer5, checkAnswer6, checkAnswer7, checkAnswer8,
                          checkAnswer11, checkAnswer10]

            # Calling calculateCost function and adding price to checkoutList
            print("\nYou have selected all of the required parts! Your total for this PC is $" + str(calculateCost(partsList)))
            checkoutCost.append(calculateCost(partsList))

            # Same thing for prebuilt
        if checkAnswer1 == "2":
            print("\nGreat! Let's pick a pre-built PC!")
            print("\nWhich prebuilt would you like to order?")
            letsPrintParts(REBUILTS, 1)
            letsPrintParts(REBUILTS, 2)
            letsPrintParts(REBUILTS, 3)
            while acceptableCases(checkAnswer10, ["1","2","3"]) != True:
                checkAnswer10 = input("Choose the number that corresponds with the part you want: ")
            partsList += [checkAnswer10]
            print("\nYour total price for this prebuilt is $" + str(calculateCost(partsList)))
            checkoutCost.append(calculateCost(partsList))

            # When checkout end loop
        if checkAnswer1 == "3":
            possibleReset = False
            print(checkoutCost)

            # Reset my variables
        checkAnswer1, checkAnswer2, checkAnswer3, checkAnswer4, checkAnswer5, checkAnswer6, checkAnswer7, checkAnswer8, checkAnswer9, checkAnswer10, checkAnswer11 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        partsList = []

# Calling function
pickItems()

