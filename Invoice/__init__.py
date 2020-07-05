"""
Program:  Invoice.py
author:  Lisa Kilmer
last modified:  July 5, 2020
This program is a class Invoice,  It makes an instance of Invoice that adds the item and price to a dictionary
named item_with_price{} with the add_item function. The create invoice function makes an invoice of the items, adds
prices, calculates the tax, adds it to the total prices of items and prints the tax and the total price.
create invoice doesn't work yet, ran out of time
"""
class Customer:
    def __init__(self, customer_id, lname, fname, phone, address):
        self.customer_id = customer_id
        self.last_name = lname
        self.first_name = fname
        self.phone = phone
        self.address = address

    def set_customer_id(self, customer_id):
        self.customer_id = customer_id

    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def set_address(self, address):
        self.address = address

    def __str__(self):
        return "Customer #" + self.customer_id + ':' + self.last_name + ', ' + self.first_name + '\n' + self.phone\
               + " in the verse" + '\n' + self.address

    def display(self):
        return "Customer #" + str(self.customer_id) +':' + self.last_name + ', ' + self.first_name + '\n' + self.phone \
               + " in the verse" + '\n' + self.address


item_with_price = {}
class Invoice:


    def __init__(self, invoice_id, customer):
        self.invoice_id = invoice_id
        self.customer = customer

    def set_invoice_id(self, invoice_id):
        self.invoice_id = invoice_id

    def set_customer(self, customer):
        self.customer = customer

    def add_item(self, items):  #add items to dictionary
        for item in items:
            item_with_price.update(items)

    def create_invoice(self, item_with_price ):  #create invoice
        values = item_with_price.values
        prices = sum(values)
        tax = prices * .06
        total = prices + tax
        return tax and total


# Driver
captain_mal = Customer(1, 'Reynolds', 'Mel', 'No phones', 'Firefly, somewhere in the verse')
invoice = Invoice(1, captain_mal)
print(captain_mal.display())
invoice.add_item({'iPad': 799.99})
invoice.add_item({'Surface': 999.99})
for kv in item_with_price.items():
    print(kv[0], '\t', kv[1])
invoice.create_invoice(item_with_price)
print("Tax...... " + str(tax))
print("Total...... " + str(total))