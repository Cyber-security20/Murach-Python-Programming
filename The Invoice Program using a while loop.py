import sys

discount_percent = 0
customer_type_flag = False
invoice_total_flag = False

# Display user entries
while customer_type_flag == False and invoice_total_flag == False:
    print(f"'R' or 'r' for Retail. 'W' or 'w' for Wholesale")
    customer_type = str(input(f"\nEnter Customer Type?  (R:W) or (r:w)\n"))
    if customer_type == "r" or customer_type == "R" or customer_type == "W" or customer_type == "w":
        customer_type_flag = True
    else:
        print("Invalid customer type. Please enter 'R' for Retail or 'W' for Wholesale.")

    try:
        invoice_total = float(input("\nEnter the total amount for or invoice: "))
        if invoice_total:
            invoice_total_flag = True
    except ValueError:
        # print(f"\n!!! Wrong Input detected !!!"
        #      f"\nIf you are receiving this message, add the required input or the correct format "
        #      "for the input")
        sys.exit(f"\n!!! Wrong Input detected !!!"
                 f"\nTerminating program due to invalid input.")


    if customer_type_flag == True and invoice_total_flag == True:
        # Determine discounts for Retail Customers
        if customer_type.lower() == "r":
            if invoice_total < 100:
                discount_percent = 0
            elif 100 <= invoice_total < 250:
                discount_percent = 0.1
            elif invoice_total >= 250:
                discount_percent = 0.2

        # Determine discounts for Wholesale Customers
        elif customer_type.lower() == "w":
            if invoice_total < 500:
                discount_percent = .4
            elif invoice_total >= 500:
                discount_percent = .5

        # Set discount to zero if neither retail nor wholesale
        else:
            print("No discount added")
            discount_percent = 0

        # Calculate discount amount and new invoice total
        discount_amount = round(invoice_total * discount_percent, 2)
        new_invoice_total = invoice_total - discount_amount

        # Display Results
        print(f"\nInvoice Total:\t\t{str(invoice_total)}")
        print(f"Discount Percent:\t{str(discount_percent)}")
        print(f"Discount amount:\t{str(discount_amount)}")
        print(f"New Invoice total:\t{str(new_invoice_total)}")
        print(f"\nBye!")