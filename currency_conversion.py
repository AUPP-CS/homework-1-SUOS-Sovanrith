def currency_conversion(currency, amount):
    # Add your code here
    
    # Reminders: 
    # - currency is a string that tells us what currency to change to. It can be 'usd', 'yuan', or 'baht'.
    # - amount is a number that tells us how much money to change into riel.
    
    # 1. add a check to ensure that 'amount' is a number.
    # 2. convert the 'amount' to the right 'currency'.
    try: 
        amount = float(amount)
        if currency.lower() == "usd":
            total = amount * 4075
        elif currency.lower() == "yuan":
            total = amount * 575
        elif currency.lower() == "baht":
            total = amount * 115  
        else:
            return "not found"
        
        if total.is_integer() == True:
            return int(total)
        else:
            return total
    
    except ValueError:
        return "invalid amount"
            