# RULES FOR VALID CREDIT CARD
# 1. Remove any '-' or ' '
# 2. Add all digits in the odd places from right to left
# 3. Double every second digit from right to left.
# (if result is a two-digit number, add the two-digit number together to get a single digit.)
# 4. sum the totals of steps 2 & 3
# 5. if sum is divisible by 10, the credit card # is valid.

sum_odd_digits = 0
sum_even_digits = 0
total = 0

# Step1:

card_number = input('Enter a credit a card #: ')
card_number = card_number.replace("-", "")
card_number = card_number.replace(" ", "")
card_number = card_number[::-1]

# Step2
for num in card_number[::2]:
    sum_odd_digits += int(num)

# Step3

for num in card_number[1::2]:
    num = int(num) * 2
    if num >= 10:
        sum_even_digits += (1 + (num % 10))
    else:
        sum_even_digits += num

# Step4

total = sum_odd_digits + sum_even_digits

# Step5

if total % 10 == 0:
    print('valid credit card')
else:
    print('Invalid credit card')










