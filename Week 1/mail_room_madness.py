donors_amt = {'Surname': 100, 'Cardholder':200}
donors_ct = {'Surname':1, 'Cardholder':2}

"""Menu Interface"""
def mail_room():
    reply = None
    while reply is not 3:
        print("Message")
        print("1: Process a Donation & Send a Thank You")
        print("2: Create a Report")
        print("3. Quit this program")
        print("(Enter 'q' at any time to return to this menu.)")
        reply = int(input("1, 2 or 3?")) #Input
        if reply == 1:
            add_amount()
        if reply == 2:
            report()

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
        donors_amt[name] += int(amount)
        donors_ct[name] += 1
    else: 
        donors_amt[name] = int(amount)
        donors_ct[name] = 1
    print_letter(name, amount)

"""This will print out the report"""   
def report():
    print(donors_amt)
    print(donors_ct)
    print("\tName\t\t\tTimes\tAmount\tAverage")
    for donor in donors_amt:
        print("\t{}\t\t{}\t${}\t${}".format(donor,donors_ct[donor], donors_amt[donor], donors_amt[donor]/donors_ct[donor] ))

def print_letter(to, contribution):
    print("""Dear Mr. or Mrs. {},
    \nThank you very much for your generous donation of ${}. It's thanks to people like you that we are able to continue our noble cause of shaving cats. Without your generous contribution even more cats would be living on the streets with a full coat of hair
    """.format(to, contribution))    

mail_room()
    