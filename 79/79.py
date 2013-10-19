import string

f = open('keylog.txt','r')
log = []

for line in f:
	log.append((string.strip(line)))

f.close()

passcode = []

i = 0

while True:

	empty = True

	for attempt in log:
		if len(attempt) != 0:
			passcode.append(attempt[0])
			empty = False
			break

	if empty: break

	for attempt in log:
		if (len(attempt) > 1 and attempt[1] == passcode[i]) or (len(attempt) > 2 and attempt[2] == passcode[i]):
			passcode[i] = attempt[0]

	log = map(lambda each:each.strip(passcode[i]), log)

	i += 1

print passcode

