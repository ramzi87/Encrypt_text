import sys

key = sys.argv[1]

encrypt = True if sys.argv[2].lower().strip() == 'encrypt' else False

text = "".join(sys.argv[3:])

def crypt_text(key, text, encrypt=True):
	my_list = []

	if encrypt:
		for x in range(len(text)):
			n_letter = ord(text[x])+int(key)
			c_item = chr(n_letter)
			my_list.append(c_item)

	else:
		for x in range(len(text)):
			n_letter = ord(text[x])-int(key)
			ch = chr(n_letter)
			my_list.append(ch)

	return "".join(my_list)

encrypted = crypt_text(key, text, encrypt=encrypt)

with open('encrypted_text.txt', 'w') as file:
	file.write(encrypted)
	file.write('\nsuccess!')
