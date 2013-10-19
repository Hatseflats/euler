import string

f = open('cipher1.txt','r')

cipher = map(int, f.read().split(','))

f.close()

frequencies = [
	{},
	{},
	{},
]

for key, val in enumerate(cipher):
	if frequencies[key % 3].get(val) is None:
		frequencies[key % 3][val] = 1
	else:
		frequencies[key % 3][val] += 1

# assume the most used character is a space (32 in ascii)
encode = [
	max(frequencies[0], key = frequencies[0].get) ^ 32,
	max(frequencies[1], key = frequencies[1].get) ^ 32,
	max(frequencies[2], key = frequencies[2].get) ^ 32
]

value = 0
text = ''

for key, char in enumerate(cipher):
	value 	+= encode[key % 3] ^ char
	text 	+= unichr(encode[key % 3] ^ char)

print value
# print text











