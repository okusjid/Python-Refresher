import re

patterns = ['term1', 'term2']
text = 'This is a string with term1, but it does not have the other term.'

for pattern in patterns:
	print(f"Searching the pattern: {pattern} IN '{text}'")
	
	res = re.search(pattern, text)
	if res:
		print("Yay Found!!!")
		print(res.start())
	if not res:
		print("Nah")
		print(res)
