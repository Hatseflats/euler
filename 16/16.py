from decimal import Decimal
i = str(Decimal(2**1000))
total = 0

for ch in i:
	total += int(ch)

print total


