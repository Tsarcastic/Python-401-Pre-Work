def add_amount():
    amount = ""
    name = input("Enter the donor's name: ")
    while amount != float or int:
        amount =  float(input("Enter their donation"))
    if input in donors:
        donors[name] += amount
    else:
        donors[name] = amount
   
def report():
    """This will print out the report"""
    for donor, amount in donors:
        print('{}\t${}').format(donor, amount)

def mail_room():
    donors = {'example': 100, 'other':200}
    reply = None
    while reply is not quit:
        print("Message")
        print("1: Send a Thank You")
        print("2: Create a Report")
        print("3. Quit this program")
        reply = int(input("1 or 2?"))
        if reply == 1:
            add_amount()
        if reply == 2:
            report()

      
mail_room()           
    