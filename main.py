from currency_conversion import currency_conversion
import os
os.system("cls")
# Print a welcome message and list of valid currencies

# Ask the user for the currency they want to convert from

# Ask the user for the amount they want to convert

# Call the currency_conversion function with the user's currency and amount

print(f"{'<<================================================================================================>>': ^150}")
print(f"{'||                       Welcome to the AUPP RIEL CURRENCY CONVERSION APP                         ||': ^150}")
print(f"{'<<================================================================================================>>': ^150}\n")

print(f"{'<<==============================>>': ^150}")
print(f"{'||      AUPP Exchange Rate      ||': ^150}")
print(f"{'||         USD  = 4075៛         ||': ^150}")
print(f"{'||         YUAN = 575៛          ||': ^150}")
print(f"{'||         BAHT = 115៛          ||': ^150}")
print(f"{'<<==============================>>': ^150}\n")

print(f"{'<<==============================================================================>>': ^150}")
print(f"{'||                                 Instructions:                                ||': ^150}")
print(f"{'||                                                                              ||': ^150}")
print(f"{'||  >> Enter the currency that you want to exchange from (USD, YUAN, BAHT).     ||': ^150}")
print(f"{'||  >> Enter the amount that you want to convert.                               ||': ^150}")
print(f"{'||  >> Make sure to enter the currency and amount correctly.                    ||': ^150}")
print(f"{'||  >> The amount will be converted to RIEL(៛).                                 ||': ^150}")
print(f"{'||                                                                              ||': ^150}")
print(f"{'<<==============================================================================>>': ^150}\n\n")

x = " "
print(f"{'<<============================================================>>': ^150}")
print(52*x, ">> Enter the currency(USD, YUAN, BAHT):", end=" ") ; currency = input()
print(52*x, ">> Enter the amount:", end=" ") ; amount = input()
print(f"{'<<============================================================>>': ^150}\n")

total = currency_conversion(currency, amount)

print(f"{'<<============================================================>>': ^150}\n")
print(48*x, f">> Your Total in RIEL after conversion is: ៛{total}")
print(f"\n{'<<============================================================>>': ^150}\n")

