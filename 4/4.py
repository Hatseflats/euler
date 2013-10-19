def palindromeChecker (palindrome):

	palindromeCheck = True
	palindrome = str(palindrome)

	for i in range(len(palindrome)/2+1):
		if palindrome[i] != palindrome[len(palindrome) - i - 1]:
			palindromeCheck = False
			break

	return palindromeCheck

palindrome = 0

for x in range(1, 1000):
	for y in range (1, 1000):
		if(palindromeChecker(x * y) and palindrome < (x * y)):
			palindrome = x * y

print palindrome