sum = 0

for i in range (1, 10**6, 2): # steps of two because the palindrome cant contain leading zero's
	decPalindrome = str(i)[::-1] == str(i) # check if number is a decimal palindrome

	binPalindrome = bin(i)[2::] == bin(i)[2::][::-1] # check if number is a binary palindrome
													 # remove the two leading characters ('0b') with [2::]
													 # and revert the string with [::-1]
													 
	if(decPalindrome and binPalindrome):
		sum += i	

print sum


