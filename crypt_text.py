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

final_txt = crypt_text(key, text, encrypt=encrypt)

if encrypt:
	print(f'Encrypted text:\n{final_txt}')
else:
	print(f'Decrypted text:\n{final_txt}')
