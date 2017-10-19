donors_amt = {'example': 100, 'other':200}
donors_ct = {'example':1, 'other':2}

"""Menu Interface"""
def mail_room():
    reply = None
    while reply is not quit:
        print("Message")
        print("1: Process a Donation & Send a Thank You")
        print("2: Create a Report")
        print("3. Quit this program")
        print("(Enter 'q' at any time to return to this menu.)")
        reply = int(input("1 or 2?")) #Input
        if reply == 1:
            add_amount()
        if reply == 2:
            report()
        if reply == 3:
            reply = quit

"""Adds the amount to the donor's total"""
def add_amount():
    amount = ""
    name = input("Enter the donor's name: ") #Input
    if name == "q":
        return
    while not amount.isdigit():
        amount = input("Enter their donation: ") #Input
        if amount == "q":
            return
    if name in donors_amt:
        donors_amt[name] += amount
        donors_ct[name] += 1
    else: 
        donors_amt[name] = amount
        donors_ct[name] = 1
    print_letter()

"""This will print out the report"""   
def report():
    print("\tName\t\tTimes\tAmount\tAverage")
    for donor in donors_amt:
        print("\t{}\t\t{}\t${}\t${}".format(donor,donors_ct[donor], donors_amt[donor], donors_amt[donor]/donors_ct[donor] ))

#def print_letter():
    
    #This is where we'll print the letter


mail_room()
    