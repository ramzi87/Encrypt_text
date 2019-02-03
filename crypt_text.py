

def crypt_text(mytext):

	key = input("Enter your Key :")
	mylst = []
	mode = "Encrypt" # or Decrypt

	for x in range(0,len(mytext)):

		if mode == "Encrypt":
			n_letter = ord(mytext[x])+int(key)
			c_item = chr(n_letter)
			mylst.append(c_item)

		if mode == "Decrypt":
			n_letter = ord(mytext[x])-int(key)
			ch = chr(n_letter)
			mylst.append(ch)

	return "".join(mylst)

print(crypt_text("""Once you stop learning, you start dying."""))