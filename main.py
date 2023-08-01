print("Welcome to ETC Credit Card Bank!")
print("This is a bill generation application.")

creditInputLoop = True

while creditInputLoop:
    credit_limit = float(input("Enter credit limit: "))
    if credit_limit >= 0:
        creditInputLoop = False

exitLoop = True

billing_cycle = 1
outstanding_balance = 0.00 #CANT CHANGE WHEN PURCHASING/PAYING
purchase = 0.00
payment = 0.00
previous_min_amount_due = 0.00
previous_balance = 0.00
finance_charge = 0.00
late_payment_charge = 0.00
total_amount_due = 0.00
minimum_amount_due = 0.00
annual_fee = 0.00

#Reward points values
previous_points_balance = 0.00 
current_points_earned = 0.00 
total_credit_points = 0.00 
points_used = 0.00 


while exitLoop:
    actionLoop = True
    print("\n")
    print("Billing Cycle {}".format(billing_cycle))
    print("Credit Limit {}".format(credit_limit))
    print("Outstanding Balance {}".format(outstanding_balance))

    while actionLoop:
        print(
    """
What is the transaction? 
1 - Add purchase
2 - View previous statement
3 - Make payment
4 - View reward points
5 - Use reward points
6 - End billing cycle
7 - Exit
    """)
        action = int(input("Enter the number of your choice: "))

        if action == 1:
            actionOneLoop = True
            while actionOneLoop:
                newPurchase = float(input("Enter the amount of purchase: "))
                if newPurchase > 0:
                    purchase = purchase + newPurchase
                    outstanding_balance = outstanding_balance + newPurchase
                    print("Purchase successful! Your new balance is", outstanding_balance)      
                    actionOneLoop = False
                else:
                    print("Purchase can't be a negative value.")
        elif action == 2:
            print("Your previous balance is {}".format(previous_balance))
            print("Your previous minimum amount due is {}".format(previous_min_amount_due))
        elif action == 3:
            actionThreeLoop = True
            while actionThreeLoop:
                newPayment = float(input("Enter the amount of payment: "))
                if newPayment > 0:
                    payment = newPayment + payment
                    print("Thank you for you payment! Redirecting you to the main menu")      
                    actionThreeLoop = False
                else:
                    print("Payment can't be a negative value.")
        elif action == 4:
            print("Your total rewards points is {}".format(total_credit_points))
        elif action == 5:
            if total_credit_points - points_used >= 1000:
                actionFiveLoop = True
                print(
        """
        What will be claimed?
        1 - PHP 100 eGift voucher for 1000 points
        2 - PHP 100 credits for 1000 points
        3 - Cancel
        """)
                while actionFiveLoop:
                    actionFiveInput = int(input("Which would you like to redeem?: "))
                    if actionFiveInput == 1:
                        print("Your eGift voucher has been sent to your registered mobile number")
                        points_used = points_used + 1000
                        activeFiveLoop = False
                    elif actionFiveInput == 2:
                        print("Php 100 has been credited to your account")
                        points_used = points_used + 1000
                        activeFiveLoop = False
                    elif actionFiveInput == 3:
                        activeFiveLoop = False
                    else:
                        print("Please choose a valid option")
            else:
                print("You currently don't have enough points to redeem anything. Your current points are: {}".format(total_credit_points))
        elif action == 6:
            print("Previous Balance: {}".format(previous_balance))
            print("(-) Payments / Credits: {}".format(payment))
            print("(+) Purchases: {}".format(purchase))

            current_finance_charge = 0
            if purchase > credit_limit:
                current_finance_charge = 500
            if outstanding_balance > 0:
                current_finance_charge = current_finance_charge + (outstanding_balance * 0.03) 
            finance_charges = current_finance_charge

            print("Finance Charges: {}".format(finance_charge))

            if previous_min_amount_due - payment > 0:
                    if  previous_min_amount_due - payment > 850:
                        current_late_charge = 850
                    else:
                        current_late_charge = previous_min_amount_due - payment
            late_payment_charge = current_late_charge

            print("Late Payment Charges: {}".format(late_payment_charge))

            total_amount_due = outstanding_balance + purchase + annual_fee + finance_charges + late_payment_charge - payment
            print("Total Amount Due: {}".format(total_amount_due))

            current_min_due = 0
            if total_amount_due <= 850:
                minimum_amount_due = total_amount_due
            elif current_min_due <= 850:
                current_min_due = total_amount_due * 0.0357
                minimum_amount_due = 850
            else:
                minimum_amount_due = current_min_due
            print("Minimum Amount Due: {}".format(minimum_amount_due))
            print("Previous Cards Points Balance: {}".format(previous_points_balance))
            current_points_earned = int(purchase / 30)
            print("(+) Current Points Earned: {}".format(current_points_earned))
            print("(-) Current Points Used: {}".format(points_used))
            total_credit_points = total_credit_points + current_points_earned - points_used
            print("Total Credit Points: {}".format(total_credit_points))

            billing_cycle = billing_cycle + 1
            current_points_earned = 0
            points_used = 0
            previous_balance = total_amount_due
            previous_min_amount_due = minimum_amount_due
            purchase = 0
            payment = 0
            if billing_cycle % 12 == 0:
                annual_fee = 4000

        elif action == 7:
            actionLoop = False
            exitLoop = False
        

